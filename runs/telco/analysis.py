"""$2M campaign analysis: move month-to-month customers to 1-year contracts.

Brief: briefs/2m-campaign.md. Run from the repo root:
    python3 runs/telco/analysis.py
Reads data/raw/telco_v2.csv (never changed). Writes every output to runs/telco/.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAW = Path("data/raw/telco_v2.csv")
OUT = Path("runs/telco")

# Brief settings
COST = 2_000_000
BANDS = [-1, 12, 24, 48, 72]
BAND_LABELS = ["0-12", "13-24", "25-48", "49-72"]
OUTLIER_CHARGE = 200          # normal MonthlyCharges stop at 118.75
MIN_GROUP = 100               # stop-check size
CASES = {"low": (0.05, 0.25), "mid": (0.10, 0.50), "high": (0.20, 1.00)}  # (conversion, share of drop kept)
DRIVER_NONE_PP = 2.0          # gap under 2 percentage points = "none"

# Chart style: one accent, the rest gray
ACCENT, GRAY, INK, INK2 = "#2a78d6", "#bdbcb6", "#0b0b0b", "#52514e"
plt.rcParams.update({"font.size": 11, "axes.edgecolor": INK2, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white"})


def profile(df):
    rows = []
    for c in df.columns:
        s = df[c].str.strip()
        num = pd.to_numeric(s.replace("", None), errors="coerce")
        is_num = num.notna().sum() == (s != "").sum() and num.notna().any()
        rows.append({"column": c, "type": "number" if is_num else "text",
                     "min": num.min() if is_num else "", "max": num.max() if is_num else "",
                     "blanks": int((s == "").sum()), "distinct": int(s.nunique())})
    return pd.DataFrame(rows)


def clean(raw, keep_first=False):
    """Return cleaned data and a log of every removed or changed row."""
    df = raw.copy()
    df["raw_row"] = df.index + 2  # line number in the CSV (header is line 1)
    log = []
    rep = df.customerID.duplicated(keep=False)
    drop = df.customerID.duplicated(keep="first") if keep_first else rep
    for _, r in df[drop].iterrows():
        log.append([r.raw_row, r.customerID, "all", "row", "removed",
                    "customerID appears twice with opposite Churn values"])
    df = df[~drop].copy()

    blank = df.TotalCharges.str.strip() == ""
    for _, r in df[blank].iterrows():
        log.append([r.raw_row, r.customerID, "TotalCharges", "(blank)", "0",
                    f"blank and tenure = {r.tenure}: new customer, no charges yet"])
    df["TotalCharges"] = pd.to_numeric(df.TotalCharges.str.strip().replace("", "0"))
    df["tenure"] = df.tenure.astype(int)
    df["SeniorCitizen"] = df.SeniorCitizen.astype(int)
    df["MonthlyCharges"] = df.MonthlyCharges.astype(float)

    df["charge_outlier"] = df.MonthlyCharges > OUTLIER_CHARGE
    for _, r in df[df.charge_outlier].iterrows():
        log.append([r.raw_row, r.customerID, "MonthlyCharges", f"{r.MonthlyCharges:g}",
                    "kept, flagged charge_outlier",
                    "about 100 times the normal range; left out of revenue numbers"])
    df["churn"] = df.Churn == "Yes"
    df["band"] = pd.cut(df.tenure, BANDS, labels=BAND_LABELS).astype(str)
    log = pd.DataFrame(log, columns=["raw_row", "customerID", "column", "before", "after", "reason"])
    return df, log


def value_model(df, band_fallback=True):
    """Per-segment churn drop and 12-month revenue kept; segment = tenure band x internet type.

    band_fallback=False uses each segment's own 1-year rate, however small the group.
    """
    m2m = df[df.Contract == "Month-to-month"]
    one = df[df.Contract == "One year"]
    band_one = one.groupby("band").churn.agg(["size", "mean"])
    rows = []
    for (b, i), g in m2m.groupby(["band", "InternetService"]):
        o = one[(one.band == b) & (one.InternetService == i)]
        seg_r1 = o.churn.mean() if len(o) else float("nan")
        if len(o) >= MIN_GROUP or (not band_fallback and len(o)):
            r1, src = seg_r1, "segment"
        else:
            r1, src = band_one.loc[b, "mean"], "tenure band"
        rev12 = g.loc[~g.charge_outlier, "MonthlyCharges"].mean() * 12
        drop = max(g.churn.mean() - r1, 0)
        rows.append({"band": b, "internet": i, "m2m_customers": len(g),
                     "m2m_churned": int(g.churn.sum()), "m2m_churn_rate": g.churn.mean(),
                     "one_year_customers": len(o), "one_year_rate_segment": seg_r1,
                     "one_year_rate_used": r1, "rate_source": src,
                     "churn_drop": drop, "revenue_12m_per_customer": rev12,
                     "full_drop_value": len(g) * drop * rev12,
                     "ceiling_value": g.churn.sum() * rev12, "all_revenue_12m": len(g) * rev12})
    seg = pd.DataFrame(rows)
    base = seg.full_drop_value.sum()   # revenue kept at 100% conversion, 100% of drop kept
    res = {"targeted_customers": int(seg.m2m_customers.sum()),
           "full_drop_value": base, "ceiling_value": seg.ceiling_value.sum(),
           "all_m2m_revenue_12m": seg.all_revenue_12m.sum(),
           "small_one_year_segments": int((seg.one_year_customers < MIN_GROUP).sum()),
           "small_m2m_segments": int((seg.m2m_customers < MIN_GROUP).sum())}
    # Upper bound for any churn window: converted customers x all their 12-month revenue
    for k, (conv, _) in CASES.items():
        res[f"bound_any_churn_window_{k}"] = conv * res["all_m2m_revenue_12m"]
    for k, (conv, keep) in CASES.items():
        res[k] = base * conv * keep
        res[f"breakeven_conversion_{k}_keep"] = COST / (base * keep)
    res["base_multiple_needed"] = COST / res["ceiling_value"]
    # How many times larger the month-to-month base must be for each rule to pass
    for k in ["mid", "high"]:
        res[f"scale_for_{k}_to_reach_cost"] = COST / res[k]
        res[f"m2m_customers_for_{k}_to_reach_cost"] = COST / res[k] * res["targeted_customers"]
    return seg, res


def recommend(res):
    if res["mid"] >= COST:
        return "fund"
    if res["high"] >= COST:
        return "test_first"
    return "do_not_fund"


def drivers(df):
    """Does the focus group churn more (higher) or less (lower) than everyone else?"""
    med_m, med_t = df.MonthlyCharges.median(), df.TotalCharges.median()
    focus = {
        "gender": df.gender == "Female", "SeniorCitizen": df.SeniorCitizen == 1,
        "Partner": df.Partner == "Yes", "Dependents": df.Dependents == "Yes",
        "tenure": df.tenure <= 12, "PhoneService": df.PhoneService == "Yes",
        "MultipleLines": df.MultipleLines == "Yes",
        "InternetService": df.InternetService == "Fiber optic",
        **{c: df[c] == "Yes" for c in ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
                                        "TechSupport", "StreamingTV", "StreamingMovies"]},
        "Contract": df.Contract == "Month-to-month", "PaperlessBilling": df.PaperlessBilling == "Yes",
        "PaymentMethod": df.PaymentMethod == "Electronic check",
        "MonthlyCharges": df.MonthlyCharges > med_m, "TotalCharges": df.TotalCharges > med_t,
        "LoyaltyAppUser": df.LoyaltyAppUser == "Yes",
    }
    labels = {"tenure": "tenure <= 12 months", "InternetService": "Fiber optic",
              "Contract": "Month-to-month", "PaymentMethod": "Electronic check",
              "gender": "Female", "SeniorCitizen": "SeniorCitizen = 1",
              "MonthlyCharges": f"MonthlyCharges > median ({med_m:g})",
              "TotalCharges": f"TotalCharges > median ({med_t:g})"}
    out, table = [], []
    for col, f in focus.items():
        gap = (df.churn[f].mean() - df.churn[~f].mean()) * 100
        overall = "none" if abs(gap) < DRIVER_NONE_PP else ("higher" if gap > 0 else "lower")
        signs, gaps = [], {}
        if col == "Contract":
            within = "not_checked"
        else:
            for c, g in df.groupby("Contract"):
                fg = f[g.index]
                if fg.sum() < 30 or (~fg).sum() < 30:
                    continue
                gaps[c] = (g.churn[fg].mean() - g.churn[~fg].mean()) * 100
                signs.append(gaps[c] > 0)
            within = "not_checked" if not signs else (
                "higher" if all(signs) else "lower" if not any(signs) else "mixed")
        out.append({"variable": col, "direction_overall": overall, "direction_within_contract": within})
        table.append({"variable": col, "focus_group": labels.get(col, f"{col} = Yes"),
                      "gap_overall_pp": gap, **{f"gap_{k}_pp": v for k, v in gaps.items()},
                      "overall": overall, "within_contract": within})
    return out, pd.DataFrame(table)


def chart_contract(df):
    t = df[df.Contract.isin(["Month-to-month", "One year"])].pivot_table(
        index="band", columns="Contract", values="churn", aggfunc="mean").loc[BAND_LABELS] * 100
    ratio = t["Month-to-month"] / t["One year"]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    x = range(len(t))
    ax.bar([i - 0.2 for i in x], t["Month-to-month"], 0.38, color=ACCENT, label="Month-to-month")
    ax.bar([i + 0.2 for i in x], t["One year"], 0.38, color=GRAY, label="One year")
    for i, (a, b) in enumerate(zip(t["Month-to-month"], t["One year"])):
        ax.text(i - 0.2, a + 1, f"{a:.0f}%", ha="center", color=INK)
        ax.text(i + 0.2, b + 1, f"{b:.0f}%", ha="center", color=INK2)
    ax.set_xticks(list(x), [f"{b} months" for b in BAND_LABELS])
    ax.set_ylabel("Churn rate (%)")
    ax.set_title(f"Month-to-month customers churn {ratio.min():.0f} to {ratio.max():.0f} times\n"
                 "more than 1-year customers in every tenure band", loc="left", color=INK)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "chart_churn_by_contract.png", dpi=150)
    plt.close(fig)


def chart_value(res):
    names = ["Low", "Mid", "High", "Maximum possible"]
    vals = [res["low"], res["mid"], res["high"], res["ceiling_value"]]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(names, [v / 1e6 for v in vals], 0.55, color=[ACCENT] * 3 + [GRAY])
    for i, v in enumerate(vals):
        ax.text(i, v / 1e6 + 0.04, f"${v / 1e6:.2f}M", ha="center", color=INK)
    ax.axhline(COST / 1e6, color=INK, lw=1.5, ls="--")
    ax.text(3.3, COST / 1e6 + 0.04, "$2M cost", ha="right", color=INK)
    ax.set_ylim(0, 2.3)
    ax.set_ylabel("Revenue kept in 12 months ($M)")
    ax.set_title(f"Even the high case keeps only ${res['high'] / 1e6:.2f}M,\n"
                 "far below the $2M cost", loc="left", color=INK)
    fig.tight_layout()
    fig.savefig(OUT / "chart_value_vs_cost.png", dpi=150)
    plt.close(fig)


def chart_breakeven(res):
    conv = [c / 100 for c in range(0, 101)]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for k, color in [("low", GRAY), ("high", GRAY), ("mid", ACCENT)]:
        keep = CASES[k][1]
        ax.plot([c * 100 for c in conv], [res["full_drop_value"] * keep * c / 1e6 for c in conv],
                color=color, lw=2)
        end = res["full_drop_value"] * keep / 1e6
        ax.text(101, end, f"{keep:.0%} of drop kept", va="center", color=INK if k == "mid" else INK2)
    ax.axhline(COST / 1e6, color=INK, lw=1.5, ls="--")
    ax.text(0, COST / 1e6 + 0.05, "$2M cost", color=INK)
    ax.set_xlim(0, 125)
    ax.set_ylim(0, 2.3)
    ax.set_xticks(range(0, 101, 20))
    ax.set_xlabel("Conversion rate (%)")
    ax.set_ylabel("Revenue kept in 12 months ($M)")
    ax.set_title("No conversion rate reaches $2M: even 100% conversion\n"
                 f"keeps ${res['full_drop_value'] / 1e6:.2f}M at most", loc="left", color=INK)
    fig.tight_layout()
    fig.savefig(OUT / "chart_breakeven.png", dpi=150)
    plt.close(fig)


def md(df, floatfmt=".1f"):
    return df.to_markdown(index=False, floatfmt=floatfmt)


def main():
    raw = pd.read_csv(RAW, dtype=str, keep_default_na=False)
    prof = profile(raw)
    df, log = clean(raw)
    df_sens, _ = clean(raw, keep_first=True)
    seg, res = value_model(df)
    seg_s, res_s = value_model(df_sens)
    seg_strict, res_strict = value_model(df, band_fallback=False)
    rec_strict = recommend(res_strict)
    internet = df[df.Contract.isin(["Month-to-month", "One year"])].pivot_table(
        index="InternetService", columns="Contract", values="churn", aggfunc=["size", "mean"])
    internet.columns = [f"{'customers' if a == 'size' else 'churn_rate'}_{b}" for a, b in internet.columns]
    internet = internet.reset_index()
    for c in internet.columns:
        if c.startswith("churn_rate_"):
            internet[c] *= 100
    rec, rec_s = recommend(res), recommend(res_s)
    drv, drv_table = drivers(df)

    # Stop checks
    seg_sizes = df.groupby(["band", "InternetService"]).size()
    by_band = df[df.Contract.isin(["Month-to-month", "One year"])].pivot_table(
        index="band", columns="Contract", values="churn", aggfunc=["size", "mean"]).loc[BAND_LABELS]
    checks = {
        "1_customers": len(df), "1_smallest_segment": int(seg_sizes.min()),
        "1_pass": bool(len(df) >= 6000 and seg_sizes.min() >= MIN_GROUP),
        "2_pass": bool((by_band["mean"]["Month-to-month"] > by_band["mean"]["One year"]).all()),
        "3_recommendation_main": rec, "3_recommendation_keep_first": rec_s, "3_pass": rec == rec_s,
    }

    # Data files
    df.drop(columns=["churn"]).to_csv(OUT / "telco_clean.csv", index=False)
    contract_overall = df.groupby("Contract").churn.agg(customers="size", churned="sum", churn_rate="mean")
    contract_overall["churn_rate"] *= 100
    band_tbl = by_band.copy()
    band_tbl.columns = [f"{a}_{b}" for a, b in band_tbl.columns]
    band_tbl = band_tbl.reset_index()
    for c in band_tbl.columns:
        if c.startswith("mean_"):
            band_tbl[c] *= 100

    issues = [
        {"column": "customerID", "issue": "211 IDs appear twice with opposite Churn values",
         "rows_affected": int(raw.customerID.duplicated(keep=False).sum()),
         "action": "removed both rows of each pair; result checked with first row kept"},
        {"column": "MonthlyCharges", "issue": f"values above {OUTLIER_CHARGE} (1,870 to 11,515); normal max is 118.75",
         "rows_affected": int((raw.MonthlyCharges.astype(float) > OUTLIER_CHARGE).sum()),
         "action": "kept for churn rates, left out of revenue numbers, flagged charge_outlier"},
        {"column": "TotalCharges", "issue": "stored as text with blanks; all blanks have tenure = 0",
         "rows_affected": int((raw.TotalCharges.str.strip() == "").sum()),
         "action": "converted to number; blanks set to 0"},
        {"column": "RetentionOfferAccepted", "issue": "filled only when Churn = Yes, so it reveals the answer",
         "rows_affected": int((raw.RetentionOfferAccepted.str.strip() == "").sum()),
         "action": "not used as a driver"},
    ]
    findings = {"recommendation": rec, "data_issues": issues, "drivers": drv}
    (OUT / "findings.json").write_text(json.dumps(findings, indent=2) + "\n")

    # Cleaning log
    counts = log.groupby(["column", "after"]).size().reset_index(name="rows")
    (OUT / "cleaning_log.md").write_text(
        "# Cleaning log\n\nMade by `runs/telco/analysis.py`. Raw file: `data/raw/telco_v2.csv` (not changed).\n\n"
        f"- Rows before: {len(raw):,}\n- Rows after: {len(df):,}\n"
        f"- Rows removed: {(log.after == 'removed').sum():,}\n"
        f"- Rows changed: {(log.column == 'TotalCharges').sum():,}\n"
        f"- Rows flagged (kept): {(log.column == 'MonthlyCharges').sum():,}\n\n"
        "`RetentionOfferAccepted` is not changed. It is left out of the driver analysis because it is "
        "filled only for churned customers.\n\n## Summary\n\n" + md(counts) +
        "\n\n## Every row\n\n`raw_row` is the line number in the raw CSV (the header is line 1).\n\n" + md(log) + "\n")

    # Charts
    chart_contract(df)
    chart_value(res)
    chart_breakeven(res)

    # Results for the report
    results = {"rows_raw": len(raw), "ids_raw": int(raw.customerID.nunique()), "rows_clean": len(df),
               "churn_rate_clean": df.churn.mean(), "recommendation": rec, "checks": checks,
               "main": res, "keep_first": res_s,
               "segment_rates_only": res_strict, "recommendation_segment_rates_only": rec_strict}
    (OUT / "results.json").write_text(json.dumps(results, indent=2, default=float) + "\n")
    seg_out = seg.copy()
    for c in ["m2m_churn_rate", "one_year_rate_segment", "one_year_rate_used", "churn_drop"]:
        seg_out[c] *= 100
    (OUT / "results.md").write_text(
        "# Result tables\n\nMade by `runs/telco/analysis.py`. Rates are in %. Money is in $.\n\n"
        "## Profile (raw file)\n\n" + md(prof, ".2f") +
        "\n\n## Churn by contract (clean data)\n\n" + md(contract_overall.reset_index()) +
        "\n\n## Churn by tenure band and contract\n\n" + md(band_tbl) +
        "\n\n## Churn by internet type and contract\n\n" + md(internet) +
        "\n\n## Segments (month-to-month)\n\n" + md(seg_out, ",.1f") +
        "\n\n## Drivers (gap = focus group churn rate minus the rest, in percentage points)\n\n" + md(drv_table) +
        "\n\n## Contract mix by LoyaltyAppUser (% of row)\n\n" +
        md((pd.crosstab(df.LoyaltyAppUser, df.Contract, normalize="index") * 100).reset_index()) +
        "\n\n## Key results\n\n```json\n" + json.dumps(results, indent=2, default=float) + "\n```\n")
    print(json.dumps(results, indent=2, default=float))


if __name__ == "__main__":
    main()
