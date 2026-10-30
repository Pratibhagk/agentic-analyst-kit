# Result tables

Made by `runs/telco/analysis.py`. Rates are in %. Money is in $.

## Profile (raw file)

| column                 | type   |   min |      max |   blanks |   distinct |
|:-----------------------|:-------|------:|---------:|---------:|-----------:|
| customerID             | text   |       |          |        0 |       7043 |
| gender                 | text   |       |          |        0 |          2 |
| SeniorCitizen          | number |  0.00 |     1.00 |        0 |          2 |
| Partner                | text   |       |          |        0 |          2 |
| Dependents             | text   |       |          |        0 |          2 |
| tenure                 | number |  0.00 |    72.00 |        0 |         73 |
| PhoneService           | text   |       |          |        0 |          2 |
| MultipleLines          | text   |       |          |        0 |          3 |
| InternetService        | text   |       |          |        0 |          3 |
| OnlineSecurity         | text   |       |          |        0 |          3 |
| OnlineBackup           | text   |       |          |        0 |          3 |
| DeviceProtection       | text   |       |          |        0 |          3 |
| TechSupport            | text   |       |          |        0 |          3 |
| StreamingTV            | text   |       |          |        0 |          3 |
| StreamingMovies        | text   |       |          |        0 |          3 |
| Contract               | text   |       |          |        0 |          3 |
| PaperlessBilling       | text   |       |          |        0 |          2 |
| PaymentMethod          | text   |       |          |        0 |          4 |
| MonthlyCharges         | number | 18.25 | 11515.00 |        0 |       1758 |
| TotalCharges           | number | 18.80 |  8684.80 |       11 |       6531 |
| Churn                  | text   |       |          |        0 |          2 |
| LoyaltyAppUser         | text   |       |          |        0 |          2 |
| RetentionOfferAccepted | text   |       |          |     5221 |          3 |

## Churn by contract (clean data)

| Contract       |   customers |   churned |   churn_rate |
|:---------------|------------:|----------:|-------------:|
| Month-to-month |        3773 |      1616 |         42.8 |
| One year       |        1420 |       161 |         11.3 |
| Two year       |        1639 |        45 |          2.7 |

## Churn by tenure band and contract

| band   |   size_Month-to-month |   size_One year |   mean_Month-to-month |   mean_One year |
|:-------|----------------------:|----------------:|----------------------:|----------------:|
| 0-12   |                  1934 |             120 |                  51.6 |            10.8 |
| 13-24  |                   722 |             193 |                  37.5 |             8.3 |
| 25-48  |                   782 |             497 |                  33.1 |            10.9 |
| 49-72  |                   335 |             610 |                  26.3 |            12.8 |

## Churn by internet type and contract

| InternetService   |   customers_Month-to-month |   customers_One year |   churn_rate_Month-to-month |   churn_rate_One year |
|:------------------|---------------------------:|---------------------:|----------------------------:|----------------------:|
| DSL               |                       1191 |                  547 |                        32.2 |                   9.5 |
| Fiber optic       |                       2077 |                  518 |                        54.7 |                  19.3 |
| No                |                        505 |                  355 |                        19.2 |                   2.5 |

## Segments (month-to-month)

| band   | internet    |   m2m_customers |   m2m_churned |   m2m_churn_rate |   one_year_customers |   one_year_rate_segment |   one_year_rate_used | rate_source   |   churn_drop |   revenue_12m_per_customer |   full_drop_value |   ceiling_value |   all_revenue_12m |
|:-------|:------------|----------------:|--------------:|-----------------:|---------------------:|------------------------:|---------------------:|:--------------|-------------:|---------------------------:|------------------:|----------------:|------------------:|
| 0-12   | DSL         |             670 |           286 |             42.7 |                   42 |                    16.7 |                 10.8 | tenure band   |         31.9 |                      572.6 |         122,212.7 |       163,777.4 |         383,674.4 |
| 0-12   | Fiber optic |             892 |           626 |             70.2 |                    7 |                    28.6 |                 10.8 | tenure band   |         59.3 |                      983.8 |         520,765.3 |       615,828.5 |         877,506.4 |
| 0-12   | No          |             372 |            86 |             23.1 |                   71 |                     5.6 |                 10.8 | tenure band   |         12.3 |                      243.3 |          11,119.8 |        20,925.6 |          90,515.3 |
| 13-24  | DSL         |             228 |            52 |             22.8 |                   77 |                    14.3 |                  8.3 | tenure band   |         14.5 |                      630.8 |          20,880.1 |        32,804.2 |         143,833.7 |
| 13-24  | Fiber optic |             415 |           211 |             50.8 |                   22 |                    18.2 |                  8.3 | tenure band   |         42.6 |                    1,050.1 |         185,450.4 |       221,579.6 |         435,808.1 |
| 13-24  | No          |              79 |             8 |             10.1 |                   94 |                     1.1 |                  8.3 | tenure band   |          1.8 |                      248.5 |             360.6 |         1,988.2 |          19,633.9 |
| 25-48  | DSL         |             223 |            36 |             16.1 |                  227 |                     9.3 |                  9.3 | segment       |          6.9 |                      642.7 |           9,878.7 |        23,138.0 |         143,326.8 |
| 25-48  | Fiber optic |             507 |           221 |             43.6 |                  149 |                    20.8 |                 20.8 | segment       |         22.8 |                    1,095.8 |         126,582.6 |       242,170.6 |         555,567.7 |
| 25-48  | No          |              52 |             2 |              3.8 |                  121 |                     1.7 |                  1.7 | segment       |          2.2 |                      253.5 |             289.1 |           506.9 |          13,180.5 |
| 49-72  | DSL         |              70 |             9 |             12.9 |                  201 |                     6.5 |                  6.5 | segment       |          6.4 |                      641.2 |           2,867.9 |         5,771.0 |          44,885.4 |
| 49-72  | Fiber optic |             263 |            78 |             29.7 |                  340 |                    18.5 |                 18.5 | segment       |         11.1 |                    1,141.6 |          33,413.0 |        89,047.5 |         300,249.9 |
| 49-72  | No          |               2 |             1 |             50.0 |                   69 |                     2.9 |                 12.8 | tenure band   |         37.2 |                      236.4 |             175.9 |           236.4 |             472.8 |

## Drivers (gap = focus group churn rate minus the rest, in percentage points)

| variable         | focus_group                     |   gap_overall_pp |   gap_Month-to-month_pp |   gap_One year_pp |   gap_Two year_pp | overall   | within_contract   |
|:-----------------|:--------------------------------|-----------------:|------------------------:|------------------:|------------------:|:----------|:------------------|
| gender           | Female                          |              1.0 |                     2.4 |              -1.5 |              -0.3 | none      | mixed             |
| SeniorCitizen    | SeniorCitizen = 1               |             18.2 |                    15.1 |               4.9 |               1.6 | higher    | higher            |
| Partner          | Partner = Yes                   |            -13.5 |                    -6.1 |               1.8 |              -0.7 | lower     | mixed             |
| Dependents       | Dependents = Yes                |            -15.6 |                   -12.1 |              -2.7 |              -0.9 | lower     | lower             |
| tenure           | tenure <= 12 months             |             30.5 |                    18.0 |              -0.6 |              -2.9 | higher    | mixed             |
| PhoneService     | PhoneService = Yes              |              1.9 |                     2.4 |               2.3 |               0.9 | none      | higher            |
| MultipleLines    | MultipleLines = Yes             |              3.3 |                     9.1 |               6.7 |               2.2 | higher    | higher            |
| InternetService  | Fiber optic                     |             27.5 |                    26.4 |              12.5 |               5.7 | higher    | higher            |
| OnlineSecurity   | OnlineSecurity = Yes            |            -16.8 |                   -16.3 |              -0.7 |               0.3 | lower     | mixed             |
| OnlineBackup     | OnlineBackup = Yes              |             -7.7 |                    -6.7 |               6.1 |               1.1 | lower     | mixed             |
| DeviceProtection | DeviceProtection = Yes          |             -6.3 |                     0.7 |               5.7 |               2.7 | lower     | higher            |
| TechSupport      | TechSupport = Yes               |            -16.1 |                   -14.7 |               4.1 |               1.3 | lower     | mixed             |
| StreamingTV      | StreamingTV = Yes               |              5.7 |                    11.9 |              13.0 |               3.5 | higher    | higher            |
| StreamingMovies  | StreamingMovies = Yes           |              5.6 |                    11.5 |              15.0 |               3.1 | higher    | higher            |
| Contract         | Month-to-month                  |             36.1 |                   nan   |             nan   |             nan   | higher    | not_checked       |
| PaperlessBilling | PaperlessBilling = Yes          |             17.1 |                    16.4 |               7.6 |               2.5 | higher    | higher            |
| PaymentMethod    | Electronic check                |             28.3 |                    21.2 |               9.3 |               5.1 | higher    | higher            |
| MonthlyCharges   | MonthlyCharges > median (71.65) |             15.8 |                    19.5 |              11.0 |               3.3 | higher    | higher            |
| TotalCharges     | TotalCharges > median (1391.4)  |            -15.6 |                   -10.6 |               8.7 |               2.7 | lower     | mixed             |
| LoyaltyAppUser   | LoyaltyAppUser = Yes            |              9.6 |                   -22.9 |              -5.4 |              -2.0 | higher    | lower             |

## Contract mix by LoyaltyAppUser (% of row)

| LoyaltyAppUser   |   Month-to-month |   One year |   Two year |
|:-----------------|-----------------:|-----------:|-----------:|
| No               |             28.9 |       31.9 |       39.1 |
| Yes              |             85.8 |        7.8 |        6.4 |

## Key results

```json
{
  "rows_raw": 7254,
  "ids_raw": 7043,
  "rows_clean": 6832,
  "churn_rate_clean": 0.2666861826697892,
  "recommendation": "do_not_fund",
  "checks": {
    "1_customers": 6832,
    "1_smallest_segment": 236,
    "1_pass": true,
    "2_pass": true,
    "3_recommendation_main": "do_not_fund",
    "3_recommendation_keep_first": "do_not_fund",
    "3_pass": true
  },
  "main": {
    "targeted_customers": 3773,
    "full_drop_value": 1033996.0552157165,
    "ceiling_value": 1417773.8196520137,
    "all_m2m_revenue_12m": 3008655.0636689942,
    "small_one_year_segments": 7,
    "small_m2m_segments": 4,
    "bound_any_churn_window_low": 150432.7531834497,
    "bound_any_churn_window_mid": 300865.5063668994,
    "bound_any_churn_window_high": 601731.0127337988,
    "low": 12924.950690196456,
    "breakeven_conversion_low_keep": 7.736973424266118,
    "mid": 51699.802760785824,
    "breakeven_conversion_mid_keep": 3.868486712133059,
    "high": 206799.2110431433,
    "breakeven_conversion_high_keep": 1.9342433560665295,
    "base_multiple_needed": 1.410662245470784,
    "scale_for_mid_to_reach_cost": 38.68486712133059,
    "m2m_customers_for_mid_to_reach_cost": 145958.00364878032,
    "scale_for_high_to_reach_cost": 9.671216780332648,
    "m2m_customers_for_high_to_reach_cost": 36489.50091219508
  },
  "keep_first": {
    "targeted_customers": 3875,
    "full_drop_value": 1014039.0187252291,
    "ceiling_value": 1458876.637607143,
    "all_m2m_revenue_12m": 3086923.355226827,
    "small_one_year_segments": 7,
    "small_m2m_segments": 4,
    "bound_any_churn_window_low": 154346.16776134135,
    "bound_any_churn_window_mid": 308692.3355226827,
    "bound_any_churn_window_high": 617384.6710453654,
    "low": 12675.487734065364,
    "breakeven_conversion_low_keep": 7.889242772982224,
    "mid": 50701.950936261455,
    "breakeven_conversion_mid_keep": 3.944621386491112,
    "high": 202807.80374504582,
    "breakeven_conversion_high_keep": 1.972310693245556,
    "base_multiple_needed": 1.370917833930366,
    "scale_for_mid_to_reach_cost": 39.44621386491112,
    "m2m_customers_for_mid_to_reach_cost": 152854.0787265306,
    "scale_for_high_to_reach_cost": 9.86155346622778,
    "m2m_customers_for_high_to_reach_cost": 38213.51968163265
  },
  "segment_rates_only": {
    "targeted_customers": 3773,
    "full_drop_value": 810401.7584740596,
    "ceiling_value": 1417773.8196520137,
    "all_m2m_revenue_12m": 3008655.0636689942,
    "small_one_year_segments": 7,
    "small_m2m_segments": 4,
    "bound_any_churn_window_low": 150432.7531834497,
    "bound_any_churn_window_mid": 300865.5063668994,
    "bound_any_churn_window_high": 601731.0127337988,
    "low": 10130.021980925747,
    "breakeven_conversion_low_keep": 9.87164689161527,
    "mid": 40520.08792370299,
    "breakeven_conversion_mid_keep": 4.935823445807635,
    "high": 162080.35169481195,
    "breakeven_conversion_high_keep": 2.4679117229038177,
    "base_multiple_needed": 1.410662245470784,
    "scale_for_mid_to_reach_cost": 49.358234458076346,
    "m2m_customers_for_mid_to_reach_cost": 186228.61861032207,
    "scale_for_high_to_reach_cost": 12.339558614519087,
    "m2m_customers_for_high_to_reach_cost": 46557.15465258052
  },
  "recommendation_segment_rates_only": "do_not_fund"
}
```
