# Brief: $2M campaign to move month-to-month customers to 1-year contracts

Follow `CLAUDE.md` for every rule not in this brief.

## 1. Decision
Should we fund a $2M campaign to move month-to-month customers to 1-year contracts?

Measure: revenue kept in the 12 months after the campaign, compared with the $2M cost.

| Result | Recommendation |
|---|---|
| Mid case ≥ $2M | `fund` |
| Mid case < $2M and high case ≥ $2M | `test_first` |
| High case < $2M | `do_not_fund` |

## 2. Questions to answer
1. How much more do month-to-month customers churn than 1-year customers? Show it overall, and within each tenure band and internet type.
2. How many month-to-month customers can the campaign target?
3. How much revenue does each saved customer keep in 12 months?
4. What conversion rate does the campaign need to break even? Is that rate realistic?

Say "associated with", never "causes". The data is not from an experiment.

## 3. Data
- Source: `data/raw/telco_v2.csv`. Never change it. Write cleaned data to `runs/telco/`.
- Profile the data first (see `CLAUDE.md`).

The first profile found these issues. Fix them as shown and log every row in `cleaning_log.md`.

| Column | Issue | Rows (data) | Action |
|---|---|---|---|
| `customerID` | 211 IDs appear twice, with opposite `Churn` values | 422 | Remove both rows of each pair. Also run the result with the first row of each pair kept, and compare. |
| `MonthlyCharges` | Values from 1,870 to 11,515. Normal values stop at 118.75. | 200 | Remove these rows from revenue numbers. Ask the data owner to confirm the correct values. |
| `TotalCharges` | Stored as text, with blanks. All blanks have tenure = 0. | 11 | Convert to a number. Set blanks to 0. |
| `RetentionOfferAccepted` | Filled only when `Churn` = "Yes", so it reveals the answer | 5,221 blank | Do not use it as a driver. |

## 4. Analysis
**Target group:** all month-to-month customers after cleaning (**assumption**, set in this brief).

**Churn after a switch:** a switched customer gets the 1-year churn rate of similar customers. "Similar" means the same tenure band and the same internet type.

**Formulas (derived):**
- Churn drop per segment = month-to-month churn rate − 1-year churn rate (same segment)
- Customers saved = targeted customers × conversion rate × churn drop × share of drop kept
- Revenue kept = customers saved × their average `MonthlyCharges` × 12
- Break-even conversion rate = conversion rate at which revenue kept = $2M

Sum the results over all segments.

**Assumptions:**

| Assumption | Low | Mid | High | Set by | Why |
|---|---|---|---|---|---|
| Conversion rate (share of targeted customers who switch) | 5% | 10% | 20% | Analyst, not tested | No past campaign data exists |
| Share of the churn drop kept after a switch | 25% | 50% | 100% | Brief owner | Customers chose their own contracts. 1-year customers may be more loyal by nature, so the full drop is a maximum. |
| Monthly charge after a switch | Same as before | Same as before | Same as before | Brief owner | No price change is planned in this brief |
| Months of revenue kept per saved customer | 12 | 12 | 12 | Brief owner | The decision window is 12 months |

Also check every driver within each contract type, for the `findings.json` field `direction_within_contract`.

## 5. When to stop and ask the brief owner
Stop and ask before you continue if:
1. Fewer than 6,000 customers remain after cleaning, or a segment you use has fewer than 100 customers.
2. In any tenure band, month-to-month churn is not higher than 1-year churn.
3. The recommendation changes when you keep the 211 repeated IDs instead of removing them.
4. The answer needs a number that is not in the data or in this brief (for example, campaign cost per customer or a price change).

## 6. Deliverables
Use the standard deliverables from `CLAUDE.md`, in `runs/telco/`:
- `recommendation.md`
- Charts as PNG files (the analyst chooses the charts)
- `cleaning_log.md`
- `findings.json`

In `recommendation.md`, show the break-even conversion rate and the low, mid, and high revenue kept.
