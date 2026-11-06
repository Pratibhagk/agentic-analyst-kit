# Review: $2M campaign recommendation (`runs/telco/recommendation.md`)

Reviewer: independent check. Brief: `briefs/2m-campaign.md`. All numbers below come from my own code on `data/raw/telco_v2.csv`.

## 1. Verdict

**Fix first.** All the main numbers are correct and `do_not_fund` follows the brief rule for this file. But the analyst did not stop at a brief stop rule, and the headline does not make clear that the result depends on the size of this file.

### Top issues, ranked by how much they could change the recommendation

| Rank | Issue | Could it change the recommendation? |
|---|---|---|
| 1 | The headline "do not fund" depends on the file size. The base size is unknown (see 5.1). | Yes, at business scale. It cannot change for this file. |
| 2 | Brief stop rule 1 was triggered. The analyst did not stop and ask (see 5.2). | No for this file. The analyst's own workaround makes the value higher, not lower. |
| 3 | The churn definition was changed from "last month" to "within 12 months" without asking (stop rule 4) (see 5.3). | No for this file (see the bound in 5.3). Unknown at business scale. |
| 4 | Brief question 1 is only partly answered. The report does not show churn by internet type alone (see 5.4). | No. |
| 5 | Labels and one wrong count: "8 of 12 segments" is 7. Some ratios are labeled **data**. The tenure bands are said to come from the brief, but they do not (see section 2 and 5.5). | No. |

## 2. Number check table

"Mine" = my value from the raw file. Tolerance: 0.1 percentage point or 1%.

### 2.1 Summary and charts

| Number as written | Where | My value | Result | Label correct? |
|---|---|---|---|---|
| 42.8% M2M churn | Summary, 3.4 | 42.83% (1,616 / 3,773) | match | No. It is a ratio, so label it **derived** (1,616 / 3,773). |
| 1,616 of 3,773 | Summary | 1,616 / 3,773 | match | Yes (**data**) |
| 11.3% 1-year churn | Summary, 3.4 | 11.34% (161 / 1,420) | match | No. Label it **derived**. |
| 161 of 1,420 | Summary | 161 / 1,420 | match | Yes |
| 2 to 5 times higher | Summary, chart 1 title | 2.05 to 4.76 (band ratios) | match | Partly. **Derived**, but no formula is shown. |
| Low $12,925 | Summary, value table | $12,925 | match | Yes |
| Mid $51,700 | Summary, value table | $51,700 | match | Yes |
| High $206,799 | Summary, value table | $206,799 | match | Yes |
| 5%, 10%, 20% conversion | Value table, 3.5 | from brief | match | Yes (**assumption**, analyst) |
| 25%, 50%, 100% share kept | Value table, 3.5 | from brief | match | Yes (**assumption**, brief owner) |
| $1,033,996 at 100% conversion | Summary, 3.4 | $1,033,996 | match | Yes |
| $1,417,774 maximum possible | Summary, 3.4, chart 2 | $1,417,774 | match | Yes |
| 422 rows removed | Data issues, 3.3 | 422 | match | Yes |
| 211 repeated IDs | Data issues, 3.3 | 211 (all pairs have opposite `Churn`; all other columns are the same) | match | Yes |
| 200 rows with charges about 100 times too high | Data issues | 200 (ratio TotalCharges / tenure / MonthlyCharges: median 0.0100) | match | Yes |
| 11 blank `TotalCharges` | Data issues, 3.3 | 11 (all are a single space; all have tenure = 0) | match | Yes |
| 145,958 M2M customers for mid case | Risk 1 | 145,958 | match | Partly. **Derived**, no formula. Formula: $2M / mid × 3,773. |
| 38.7 times this file | Risk 1 | 38.68 | match | Partly. No formula. |
| 36,490 for high case | Risk 1, next step | 36,490 | match | Partly. No formula. |
| 9.7 times | Risk 1 | 9.67 | match | Partly. No formula. |
| 26.3% vs 12.8% (49–72) | Chart 1 caption | 26.27% vs 12.79% | match | Not labeled |
| 51.6% vs 10.8% (0–12) | Chart 1 caption | 51.60% vs 10.83% | match | Not labeled |
| $0.21M high case | Chart 2 title and caption | $0.207M | match | Not labeled |
| $1.42M maximum | Chart 2 caption | $1.418M | match | Not labeled |
| $1.03M at 100% conversion | Chart 3 title | $1.034M | match | Not labeled |

### 2.2 Appendix

| Number as written | Where | My value | Result | Label correct? |
|---|---|---|---|---|
| 7,254 rows | 3.1 | 7,254 | match | Yes |
| 7,043 unique IDs | 3.1 | 7,043 | match | Yes |
| 23 columns | 3.1 | 23 | match | Not labeled |
| 6,832 after cleaning | 3.1, 3.3 | 6,832 | match | Yes |
| 26.7% churn (1,822 / 6,832) | 3.1 | 26.67% | match | Yes |
| 18.25–118.75 normal `MonthlyCharges`; up to 11,515 | 3.2 | 18.25–118.75; outliers 1,870–11,515 | match | Not labeled |
| tenure 0–72 | 3.2 | 0–72 | match | Not labeled |
| 5,221 blank `RetentionOfferAccepted` | 3.3 | 5,221 (all have Churn = "No") | match | Yes |
| Two-year: 1,639 / 45 / 2.7% | 3.4 | 1,639 / 45 / 2.75% | match | Rate should be **derived** |
| Tenure band table (8 counts, 8 rates) | 3.4 | 1,934 / 51.6%, 120 / 10.8%; 722 / 37.5%, 193 / 8.3%; 782 / 33.1%, 497 / 10.9%; 335 / 26.3%, 610 / 12.8% | all match | Table says **data**; rates are **derived** |
| Segment table: 12 rows × (M2M customers, M2M churn, 1-year rate used, churn drop, revenue per customer, value at 100%) | 3.4 | Every cell matches to the shown decimal (for example 0–12 Fiber: 892, 70.2%, 10.8%, 59.3 pp, $983.8, $520,765) | all match | Yes; formulas shown |
| Total 3,773 | 3.4 | 3,773 | match | Yes |
| Break-even 774% / 387% / 193% | 3.4 | 773.7% / 386.9% / 193.4% | match | Yes (formula shown) |
| First row kept: $12,675 / $50,702 / $202,808 | 3.4 | $12,675 / $50,702 / $202,808 | match | Yes |
| Driver gaps: 20 variables × 4 gaps (80 numbers) | 3.4 | All 80 match to 0.1 point | all match | Yes (definition shown) |
| Median `MonthlyCharges` 71.65 | 3.4 | 71.65 (includes the 200 outliers) | match | See 5.7 |
| Median `TotalCharges` 1,391.4 | 3.4 | 1,391.4 | match | Not labeled |
| 85.8% of app users on M2M; 28.9% of non-users | 3.4 note | 85.84%; 28.93% | match | No. Ratios, so **derived**, not **data**. |
| 8 of 12 segments too small | 3.5 | **7 of 12** one-year segments have fewer than 100 customers | **mismatch** | Analyst assumption |
| Fiber 0–12 has 7 | 3.5 | 7 one-year customers | match | Not labeled |
| Threshold 200 for outliers | 3.5 | No values between 118.75 and 200 | match | Yes (assumption) |
| Driver "none" if gap < 2 points | 3.5 | – | not checked (it is a rule, not a result) | Yes (assumption) |

## 3. Causal claims

The report uses "associated with" for the main finding. Good. But the value sentences say the campaign "keeps" revenue as if the effect is proven.

| Quote | Location | Suggested wording |
|---|---|---|
| "The campaign keeps $12,925 (low), $51,700 (mid), or $206,799 (high) of revenue in 12 months" | Summary, bullet 4 | "The model estimates $12,925 (low), $51,700 (mid), or $206,799 (high), if switched customers churn like similar 1-year customers." |
| "At 100% conversion with the full churn drop kept, the campaign keeps $1,033,996" | Summary, bullet 5 | "At 100% conversion and the full churn drop, the model estimates $1,033,996." |
| "Even the high case keeps only $0.21M, far below the $2M cost" | Chart 2 title | "Even the high-case estimate is $0.21M, far below the $2M cost" |
| "even 100% conversion keeps $1.03M at most" | Chart 3 title | "even at 100% conversion the estimate is $1.03M at most" |
| "Revenue kept rises with the conversion rate" | Chart 3 caption | Keep, but add "in the model". |
| "Customers saved" / "revenue kept" (model terms) | 3.4 formulas | Keep (brief terms). Add one sentence: "These are model estimates, not measured effects." |

No sentence uses "causes", "drives" or "leads to" as a claim. The sentence "The data does not show that a contract change causes lower churn" is correct.

## 4. Missed data problems

The analyst found and handled all four issues in the brief. I found no new data problem that changes the result.

| Column | Problem | Rows affected | Why it matters |
|---|---|---|---|
| `MonthlyCharges` | The 200 outliers are exactly 100 times the true value. TotalCharges / tenure / MonthlyCharges has median 0.0100 (range 0.0075 to 0.0144). | 200 | The values can be fixed (divide by 100). With that fix the mid case is $51,709, not $51,700. Tell the data owner this pattern. |
| `MonthlyCharges` | The driver median (71.65) includes the 200 outliers. Without them the median is 70.425. | 200 | Small. The overall gap changes from +15.8 to +16.6 points. The direction does not change. |
| `customerID` | The 211 pairs are the same in every column except `Churn`. | 422 | Confirms the brief: the conflict is only in the answer column. With the **last** row kept, the result is $13,003 / $52,012 / $208,048. Still `do_not_fund`. |
| `TotalCharges` | The blanks are a single space, not empty. | 11 | Handled. Note it in the log so others do not miss it. |
| `LoyaltyAppUser` | Not leakage. 85.8% of app users are on M2M. | 3,321 raw | Handled well in the report (the direction reverses within contract). |

Checks with no problem: no exact repeated rows; no blanks in other columns; no category spelling errors; no conflict between `InternetService` and the add-on columns; no conflict between `PhoneService` and `MultipleLines`; tenure 0–72; `SeniorCitizen` only 0/1.

## 5. Other issues (brief and standards)

### 5.1 The headline depends on the file size (rank 1)
- The brief sets the target group as all M2M customers in the file. So `do_not_fund` is correct by the brief rule.
- But the full yearly revenue of all 3,773 M2M customers is about $3.01M (**derived**: 3,773 × mean non-outlier `MonthlyCharges` × 12). The $2M cost is about 66% of it.
- So the result is close to certain for this file. It says little about a real base, if this file is a sample.
- **Fix:** In the first line, write "Do not fund, for the 3,773 M2M customers in this file." Ask the brief owner one question: is this file the full base or a sample?

### 5.2 Stop rule 1 was triggered, but the analyst did not stop (rank 2)
- The brief says: stop and ask if "a segment you use has fewer than 100 customers".
- 7 of 12 one-year segments have fewer than 100 customers. 4 of 12 M2M segments also do (79, 52, 70 and 2).
- The analyst made a new rule (use the band rate) and labeled it as an analyst assumption. That is a choice the brief owner must make.
- Effect: with the real segment rates, the mid case is $40,520 and the high case is $162,080. The fallback makes the value higher. So the decision does not change.
- **Fix:** Report the stop rule to the brief owner. Show both versions.

### 5.3 Churn window assumption (rank 3)
- `Churn` means "left in the last month". The analyst treats it as "left within 12 months". That is a number not in the data or brief (stop rule 4).
- The assumption is labeled. But it was not raised with the brief owner.
- Bound: revenue kept cannot be more than conversion × all M2M yearly revenue. At 20% conversion that is about $0.60M (**derived**: 0.20 × $3.01M). So the high case stays below $2M for any churn window.
- **Fix:** Add this bound to the summary. It makes "no assumption in the brief can change it" provable.

### 5.4 Brief question 1 is only partly answered (rank 4)
- The brief asks for the gap "overall, and within each tenure band and internet type".
- The report shows tenure bands. It does not show internet type alone. The segment table shows the "1-year rate used", not the real 1-year rate in each segment.
- My values by internet type (M2M vs 1-year churn): DSL 32.2% vs 9.5%; Fiber optic 54.7% vs 19.3%; No internet 19.2% vs 2.5%. M2M is higher in all three.
- **Fix:** Add an internet-type table. Add the real 1-year rate and count to the segment table.

### 5.5 Labels (rank 5)
- Percentages are labeled **data**. Under `CLAUDE.md` a ratio is **derived**, with the formula.
- The tenure bands are labeled "Set by Brief owner". The brief does not define bands. Label them as analyst assumption.
- "8 of 12 segments are too small" is wrong. The correct count is 7.
- The scale numbers in risk 1 (145,958; 38.7; 36,490; 9.7) need a formula.

### 5.6 Driver directions in `findings.json`
- The format of `findings.json` is correct.
- The 2-point "none" rule is used for overall gaps only. The rule for `direction_within_contract` is not stated, and it is not consistent:
  - `DeviceProtection`: M2M gap +0.7 (under 2 points) but marked "higher".
  - `PhoneService`: two-year gap +0.9 but marked "higher".
  - `gender`: +2.4, −1.5, −0.3, marked "mixed". Under a 2-point rule it would be "higher" or "none".
- **Fix:** State the within-contract rule. Apply it the same way to all variables.

### 5.7 Smaller items
- Chart 3 caption: "no line reaches $2M before 100% conversion" suggests a line reaches it at 100%. None does. Write "no line reaches $2M, even at 100% conversion".
- The brief formula uses "their average `MonthlyCharges`" (saved customers). The analyst uses the mean of all M2M customers in the segment. With churners' charges, the value at 100% is $1,032,987, not $1,033,996. No effect on the decision. State the choice.
- Some sentences have more than 20 words (for example the chart 1 caption, 26 words). Split them.
- Required parts are present: summary, charts with one-sentence captions, appendix with source, dictionary, cleaning summary, result tables, assumptions with low/mid/high, and the run command. `cleaning_log.md` lists all 633 row actions (422 + 200 + 11).

## 6. How to check again

Run from any folder. The scripts read only `data/raw/telco_v2.csv`.

```bash
R=/tmp/claude-0/-home-user-agentic-analyst-kit/6e7275fb-af88-5692-ac6c-60a9bdb66852/scratchpad/reviewer
cd $R && python3 profile.py && python3 recompute.py && python3 drivers.py && python3 extra.py
```

- `profile.py`: profile of the raw file (blanks, types, ranges, repeated IDs, conflicts, outliers).
- `recompute.py`: cleaning, churn tables, segment model, low/mid/high, break-even, and sensitivity runs.
- `drivers.py`: segment table and all driver gaps.
- `extra.py`: segment counts under 100, total M2M revenue, and the churner-charge check.
