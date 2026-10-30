# Cleaning log

Made by `runs/telco/analysis.py`. Raw file: `data/raw/telco_v2.csv` (not changed).

- Rows before: 7,254
- Rows after: 6,832
- Rows removed: 422
- Rows changed: 11
- Rows flagged (kept): 200

`RetentionOfferAccepted` is not changed. It is left out of the driver analysis because it is filled only for churned customers.

## Summary

| column         | after                        |   rows |
|:---------------|:-----------------------------|-------:|
| MonthlyCharges | kept, flagged charge_outlier |    200 |
| TotalCharges   | 0                            |     11 |
| all            | removed                      |    422 |

## Every row

`raw_row` is the line number in the raw CSV (the header is line 1).

|   raw_row | customerID   | column         | before   | after                        | reason                                                        |
|----------:|:-------------|:---------------|:---------|:-----------------------------|:--------------------------------------------------------------|
|         3 | 8582-KRHPJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|        26 | 2169-RRLFW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|        42 | 7029-RPUAV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|        47 | 6685-XSHHU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|        52 | 5244-IRFIH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|        88 | 2344-JMOGN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       124 | 9500-LTVBP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       163 | 9227-YBAXE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       179 | 8356-WUAOJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       199 | 5802-ADBRC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       206 | 2616-FLVQC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       217 | 8756-RDDLT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       218 | 8205-MQUGY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       231 | 2656-TABEH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       240 | 8146-QQKZH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       241 | 1114-CENIM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       312 | 5884-FBCTL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       314 | 9040-KZVWO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       343 | 9530-EHPOH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       359 | 4654-DLAMQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       363 | 4767-HZZHQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       374 | 8707-RMEZH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       389 | 2230-XTUWL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       416 | 6872-HXFNF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       495 | 0363-SVHYR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       496 | 4186-ZBUEW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       500 | 0225-ZORZP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       507 | 1905-OEILC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       512 | 8097-OMULG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       525 | 2882-WDTBA   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       545 | 8748-HFWBO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       554 | 3115-JPJDD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       570 | 3810-DVDQQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       613 | 0897-FEGMU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       616 | 9239-GZHZE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       624 | 9448-REEVD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       643 | 7951-QKZPL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       681 | 2309-OSFEU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       713 | 0048-LUMLS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       771 | 1905-OEILC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       775 | 7216-EWTRS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       780 | 7216-EWTRS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       802 | 0052-DCKON   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       807 | 7951-QKZPL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       822 | 3694-GLTJM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       825 | 5712-VBOXD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       830 | 2599-CZABP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       848 | 7356-AYNJP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       858 | 2180-DXNEG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       877 | 8917-FAEMR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       922 | 0533-UCAAU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       925 | 9029-FEGVJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       926 | 6088-BXMRG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       930 | 3658-KIBGF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       944 | 8146-QQKZH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       982 | 0568-ONFPC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|       996 | 6305-YLBMM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1001 | 8879-ZKJOF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1015 | 8443-WVPSS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1054 | 4727-MCYZG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1063 | 8883-ANODQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1066 | 4039-HEUNW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1081 | 2737-YNGYW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1089 | 8670-MEFCP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1133 | 7410-KTVFV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1160 | 3658-KIBGF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1166 | 5220-AGAAX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1167 | 3642-GKTCT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1181 | 0023-XUOPT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1203 | 6242-SGYTS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1206 | 1849-RJYIG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1241 | 5174-ITUMV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1255 | 6981-TDRFT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1272 | 8582-KRHPJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1308 | 5093-FEGLU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1344 | 5802-ADBRC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1362 | 8756-RDDLT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1480 | 5774-XZTQC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1486 | 3644-QXEHN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1491 | 0533-UCAAU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1528 | 7029-RPUAV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1562 | 8883-ANODQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1565 | 2533-QVMSK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1584 | 3034-ZBEQN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1607 | 5337-IIWKZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1617 | 5895-QSXOD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1624 | 9780-FKVVF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1629 | 6518-LGAOV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1640 | 3115-JPJDD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1644 | 6574-MCOEH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1660 | 8205-MQUGY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1799 | 5839-SUYVZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1805 | 1173-XZPYF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1845 | 9448-REEVD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1869 | 3798-EPWRR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1885 | 1936-CZAKF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1887 | 6734-GMPVK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1896 | 2169-RRLFW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1939 | 3785-NRHYR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1942 | 1137-DGOWI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1946 | 5018-LXQQG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1951 | 5093-FEGLU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1963 | 9239-GZHZE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2008 | 6080-TCMYC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2015 | 5701-GUXDC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2021 | 0459-SPZHJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2023 | 0428-AXXLJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2031 | 8748-HFWBO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2037 | 6981-TDRFT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2048 | 2446-PLQVO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2050 | 9091-WTUUY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2056 | 8461-EFQYM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2066 | 9027-TMATR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2094 | 3750-RNQKR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2100 | 3635-QQRQD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2126 | 7674-YTAFD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2131 | 3694-GLTJM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2136 | 7929-SKFGK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2204 | 8259-DZLIZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2214 | 7647-GYYKX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2242 | 0486-LGCCH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2263 | 2230-XTUWL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2289 | 8356-WUAOJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2296 | 4201-JMNGR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2310 | 4947-DSMXK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2318 | 6088-BXMRG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2339 | 3034-ZBEQN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2347 | 5186-PEIZU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2358 | 7319-VENRZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2362 | 3301-VKTGC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2369 | 9158-VCTQB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2378 | 5244-IRFIH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2389 | 2480-SQIOB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2423 | 9693-XMUOB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2430 | 2325-WINES   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2438 | 4039-HEUNW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2446 | 5134-IKDAY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2453 | 8707-RMEZH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2494 | 3317-VLGQT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2507 | 3955-JBZZM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2521 | 5712-VBOXD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2543 | 1571-SAVHK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2549 | 6618-RYATB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2567 | 2533-QVMSK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2574 | 9764-REAFF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2576 | 6127-ISGTU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2579 | 4986-MXSFP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2580 | 9530-EHPOH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2589 | 9962-BFPDU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2595 | 4808-YNLEU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2609 | 4986-MXSFP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2641 | 7693-QPEFS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2655 | 5916-QEWPT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2684 | 5442-XSDCW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2720 | 7693-QPEFS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2748 | 8076-FEZKJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2764 | 2040-VZIKE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2779 | 6734-GMPVK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2787 | 4547-LYTDD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2799 | 5478-JJVZK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2818 | 2309-OSFEU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2841 | 4785-FCIFB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2854 | 8945-MUQUF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2874 | 8443-WVPSS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2943 | 8879-ZKJOF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2964 | 2599-CZABP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2979 | 0732-OCQOC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      2994 | 6408-OTUBZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3000 | 0799-DDIHE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3008 | 5478-JJVZK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3022 | 5884-FBCTL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3040 | 9158-VCTQB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3048 | 5150-LJNSR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3056 | 5150-LJNSR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3059 | 3930-ZGWVE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3066 | 1163-VIPRI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3074 | 7929-SKFGK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3080 | 1241-FPMOF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3093 | 3009-JWMPU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3119 | 0640-YJTPY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3170 | 1452-UZOSF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3188 | 6061-GWWAV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3222 | 5220-AGAAX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3228 | 3580-HYCSP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3258 | 4039-PIMHX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3283 | 3301-VKTGC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3323 | 2325-WINES   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3333 | 6127-ISGTU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3354 | 0640-YJTPY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3356 | 0788-DXBFY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3379 | 4039-PIMHX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3398 | 8076-FEZKJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3401 | 5134-IKDAY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3402 | 7802-EFKNY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3405 | 0602-DDUML   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3407 | 9040-KZVWO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3419 | 9753-OYLBX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3432 | 9046-DQMTP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3466 | 0363-SVHYR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3471 | 3955-JBZZM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3472 | 1741-WTPON   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3496 | 1741-WTPON   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3535 | 2636-OHFMN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3539 | 0557-ASKVU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3553 | 7427-AUFPY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3556 | 1061-PNTHC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3597 | 6285-FTQBF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3598 | 8468-FZTOE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3643 | 1241-FPMOF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3667 | 2882-WDTBA   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3673 | 5774-XZTQC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3719 | 4727-MCYZG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3758 | 0967-BMLBD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3760 | 0023-XUOPT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3766 | 6897-UUBNU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3769 | 6897-UUBNU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3796 | 1596-BBVTG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3832 | 0225-ZORZP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3834 | 8259-DZLIZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3847 | 1061-PNTHC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3897 | 8468-FZTOE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3930 | 4785-FCIFB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3935 | 8190-ZTQFB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3953 | 9693-XMUOB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3975 | 3363-EWLGO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      3980 | 8915-NNTRC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4023 | 6000-APYLU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4059 | 4903-CNOZC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4065 | 4994-OBRSZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4072 | 4229-CZMLL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4084 | 4877-TSOFF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4139 | 6408-WHTEF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4146 | 3810-DVDQQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4150 | 7140-ADSMJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4152 | 0052-DCKON   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4190 | 1937-OTUKY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4197 | 0315-LVCRK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4231 | 7527-QNRUS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4280 | 3317-VLGQT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4281 | 9314-IJWSQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4295 | 0877-SDMBN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4326 | 1163-VIPRI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4329 | 6736-DHUQI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4370 | 2054-PJOCK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4381 | 8461-EFQYM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4395 | 6000-APYLU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4403 | 6872-HXFNF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4406 | 5839-SUYVZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4418 | 7993-NQLJE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4436 | 7527-QNRUS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4470 | 8097-OMULG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4472 | 7410-YTJIK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4486 | 3642-GKTCT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4502 | 1452-UZOSF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4506 | 8084-OIVBS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4510 | 8190-ZTQFB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4533 | 9053-JZFKV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4550 | 2656-TABEH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4561 | 0557-ASKVU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4562 | 7427-AUFPY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4642 | 9227-YBAXE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4645 | 1173-XZPYF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4663 | 4201-JMNGR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4699 | 3930-ZGWVE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4724 | 5337-IIWKZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4727 | 1996-DBMUS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4749 | 4229-CZMLL   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4753 | 3785-NRHYR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4774 | 8652-YHIYU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4786 | 7140-ADSMJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4790 | 8670-MEFCP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4798 | 5916-QEWPT   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4832 | 0723-VSOBE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4864 | 0048-LUMLS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4876 | 2480-SQIOB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4929 | 6408-OTUBZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4932 | 4994-OBRSZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4938 | 8189-XRIKE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4954 | 1571-SAVHK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4959 | 8559-WNQZS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4976 | 1927-QEWMY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4989 | 6061-GWWAV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      4997 | 0788-DXBFY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5002 | 6701-DHKWQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5017 | 8084-OIVBS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5059 | 0877-SDMBN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5100 | 7727-SHVZV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5104 | 0733-VUNUW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5105 | 6305-YLBMM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5122 | 3195-TQDZX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5158 | 1775-KWJKQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5159 | 0459-SPZHJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5167 | 7410-YTJIK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5229 | 4654-DLAMQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5235 | 8945-MUQUF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5237 | 4947-DSMXK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5244 | 1927-QEWMY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5251 | 1596-BBVTG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5287 | 6518-LGAOV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5315 | 0784-GTUUK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5320 | 5010-IPEAQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5324 | 6701-DHKWQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5348 | 5186-PEIZU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5350 | 6685-XSHHU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5352 | 3780-YVMFA   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5364 | 5510-BOIUJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5384 | 9314-IJWSQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5385 | 3580-HYCSP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5393 | 2054-PJOCK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5396 | 5442-XSDCW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5397 | 5842-POCOP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5410 | 3644-QXEHN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5444 | 4159-NAAIX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5446 | 9068-VPWQQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5447 | 8559-WNQZS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5448 | 7647-GYYKX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5480 | 9029-FEGVJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5488 | 2616-FLVQC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5497 | 5174-ITUMV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5499 | 1937-OTUKY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5514 | 0967-BMLBD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5515 | 5701-GUXDC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5516 | 9962-BFPDU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5534 | 7410-KTVFV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5549 | 9068-VPWQQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5574 | 4159-NAAIX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5580 | 2187-PKZAY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5596 | 6285-FTQBF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5598 | 9761-XUJWD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5643 | 7017-VFHAY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5681 | 7017-VFHAY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5710 | 1585-MQSSU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5714 | 9046-DQMTP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5723 | 5537-UXXVS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5732 | 7802-EFKNY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5733 | 3750-RNQKR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5745 | 4808-YNLEU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5755 | 3363-EWLGO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5757 | 2040-VZIKE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5763 | 3009-JWMPU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5771 | 9089-UOWJG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5797 | 7599-NTMDP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5805 | 0732-OCQOC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5818 | 4767-HZZHQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5820 | 4186-ZBUEW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5865 | 3635-QQRQD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5883 | 9089-UOWJG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5916 | 7599-NTMDP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5918 | 5895-QSXOD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5932 | 2027-DNKIV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5946 | 9500-LTVBP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5975 | 0784-GTUUK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5985 | 3798-EPWRR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5987 | 6242-SGYTS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      5996 | 4903-CNOZC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6008 | 0897-FEGMU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6014 | 1775-KWJKQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6021 | 2180-DXNEG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6066 | 9027-TMATR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6082 | 4877-TSOFF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6119 | 2344-JMOGN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6120 | 5183-KLYEM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6137 | 7356-AYNJP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6153 | 6844-DZKRF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6160 | 3195-TQDZX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6185 | 8915-NNTRC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6193 | 2737-YNGYW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6202 | 5183-KLYEM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6213 | 7459-IMVYU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6214 | 1585-MQSSU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6226 | 7319-VENRZ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6227 | 3780-YVMFA   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6250 | 2519-TWKFS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6258 | 7674-YTAFD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6278 | 5010-IPEAQ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6325 | 2446-PLQVO   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6355 | 5537-UXXVS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6416 | 6736-DHUQI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6437 | 9191-MYQKX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6439 | 5510-BOIUJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6493 | 9191-MYQKX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6501 | 6844-DZKRF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6526 | 8184-WMOFI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6549 | 9091-WTUUY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6579 | 2027-DNKIV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6606 | 9761-XUJWD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6608 | 5141-ZUVBH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6612 | 1996-DBMUS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6625 | 0723-VSOBE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6649 | 5141-ZUVBH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6664 | 8189-XRIKE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6667 | 4547-LYTDD   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6670 | 6618-RYATB   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6673 | 9753-OYLBX   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6692 | 0428-AXXLJ   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6693 | 2636-OHFMN   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6711 | 1849-RJYIG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6735 | 7459-IMVYU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6736 | 5018-LXQQG   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6748 | 8917-FAEMR   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6783 | 1114-CENIM   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6823 | 9053-JZFKV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6874 | 0799-DDIHE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6889 | 0486-LGCCH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6917 | 6408-WHTEF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6931 | 1137-DGOWI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6945 | 7993-NQLJE   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6998 | 0602-DDUML   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      6999 | 2187-PKZAY   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7055 | 9764-REAFF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7090 | 0315-LVCRK   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7100 | 6080-TCMYC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7118 | 9780-FKVVF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7120 | 2519-TWKFS   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7137 | 1936-CZAKF   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7152 | 5842-POCOP   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7166 | 7727-SHVZV   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7177 | 6574-MCOEH   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7193 | 8652-YHIYU   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7211 | 0733-VUNUW   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7244 | 0568-ONFPC   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      7246 | 8184-WMOFI   | all            | row      | removed                      | customerID appears twice with opposite Churn values           |
|      1013 | 4075-WKNIU   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      1469 | 3213-VVOLG   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      1738 | 2520-SGTTA   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      1747 | 4472-LVYGI   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      2742 | 4367-NUYAO   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      2929 | 2923-ARZLG   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      3697 | 2775-SEFEE   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      4425 | 1371-DWPAZ   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      6035 | 5709-LVOEQ   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      6659 | 3115-CZMZD   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|      6898 | 7644-OMVMY   | TotalCharges   | (blank)  | 0                            | blank and tenure = 0: new customer, no charges yet            |
|        31 | 0254-WWRKD   | MonthlyCharges | 5055     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|        57 | 5039-LZRQT   | MonthlyCharges | 2020     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|        63 | 6620-JDYNW   | MonthlyCharges | 6060     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|        76 | 5126-RCXYW   | MonthlyCharges | 4600     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|        77 | 6891-JPYFF   | MonthlyCharges | 10525    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|        81 | 2933-FILNV   | MonthlyCharges | 2440     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       156 | 1093-YSWCA   | MonthlyCharges | 1955     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       162 | 3415-TAILE   | MonthlyCharges | 6570     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       280 | 4530-NDRKU   | MonthlyCharges | 1905     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       305 | 6729-FZWSY   | MonthlyCharges | 1945     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       308 | 4415-IJZTP   | MonthlyCharges | 7450     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       331 | 4869-EPIUS   | MonthlyCharges | 8090     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       394 | 1918-ZBFQJ   | MonthlyCharges | 7925     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       401 | 0383-CLDDA   | MonthlyCharges | 8535     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       427 | 5649-TJHOV   | MonthlyCharges | 3650     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       482 | 3669-WHAFY   | MonthlyCharges | 11515    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       553 | 5966-EMAZU   | MonthlyCharges | 10850    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       610 | 2832-SCUCO   | MonthlyCharges | 1990     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       687 | 9575-IWCAZ   | MonthlyCharges | 2510     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       696 | 6899-PPEEA   | MonthlyCharges | 9655     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       710 | 1429-UYJSV   | MonthlyCharges | 1970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       776 | 3981-QSVQI   | MonthlyCharges | 1970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       800 | 4343-EJVQB   | MonthlyCharges | 7435     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       845 | 9102-OXKFY   | MonthlyCharges | 5415     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       851 | 2037-SGXHH   | MonthlyCharges | 9465     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|       883 | 4369-NYSCF   | MonthlyCharges | 7575     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1004 | 1925-LFCZZ   | MonthlyCharges | 5005     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1016 | 8466-PZBLH   | MonthlyCharges | 10460    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1019 | 5108-ADXWO   | MonthlyCharges | 7350     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1079 | 4881-JVQOD   | MonthlyCharges | 3455     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1115 | 6867-ACCZI   | MonthlyCharges | 5250     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1128 | 4682-BLBUC   | MonthlyCharges | 7095     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1135 | 0254-KCJGT   | MonthlyCharges | 8140     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1154 | 5020-ZSTTY   | MonthlyCharges | 8245     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1179 | 2978-XXSOG   | MonthlyCharges | 5905     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1221 | 0742-LAFQK   | MonthlyCharges | 9915     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1225 | 8270-RKSAP   | MonthlyCharges | 7050     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1349 | 2959-FENLU   | MonthlyCharges | 8530     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1387 | 9048-JVYVF   | MonthlyCharges | 6935     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1399 | 8631-XVRZL   | MonthlyCharges | 2015     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1433 | 8364-TRMMK   | MonthlyCharges | 5065     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1475 | 7693-LCKZL   | MonthlyCharges | 8015     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1500 | 6103-QCKFX   | MonthlyCharges | 5625     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1524 | 5651-CRHKQ   | MonthlyCharges | 8620     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1550 | 1777-JYQPJ   | MonthlyCharges | 2430     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1567 | 0311-QYWSS   | MonthlyCharges | 4945     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1608 | 5736-YEJAX   | MonthlyCharges | 7945     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1637 | 5948-UJZLF   | MonthlyCharges | 4925     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1647 | 4385-ZKVNW   | MonthlyCharges | 5490     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1819 | 2645-QTLMB   | MonthlyCharges | 9425     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1848 | 8630-QSGXK   | MonthlyCharges | 7520     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1900 | 2120-SMPEX   | MonthlyCharges | 2015     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1937 | 7771-ZONAT   | MonthlyCharges | 5675     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      1982 | 7047-FWEYA   | MonthlyCharges | 10315    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2072 | 5494-HECPR   | MonthlyCharges | 8025     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2108 | 8065-QBYTO   | MonthlyCharges | 9965     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2156 | 1409-PHXTF   | MonthlyCharges | 11045    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2220 | 2026-TGDHM   | MonthlyCharges | 7930     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2254 | 8967-SZQAS   | MonthlyCharges | 5045     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2295 | 6838-HVLXG   | MonthlyCharges | 2030     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2314 | 5197-YPYBZ   | MonthlyCharges | 2525     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2337 | 6177-PEVRA   | MonthlyCharges | 5550     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2350 | 1328-EUZHC   | MonthlyCharges | 2010     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2354 | 7079-QRCBC   | MonthlyCharges | 9875     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2384 | 1400-WIVLL   | MonthlyCharges | 10795    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2388 | 5614-DNZCE   | MonthlyCharges | 6490     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2399 | 1009-IRMNA   | MonthlyCharges | 2000     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2436 | 8849-PRIQJ   | MonthlyCharges | 10940    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2447 | 2866-IKBTM   | MonthlyCharges | 1955     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2525 | 3537-HPKQT   | MonthlyCharges | 7775     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2539 | 3566-HJGPK   | MonthlyCharges | 4555     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2594 | 9357-UJRUN   | MonthlyCharges | 5835     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2606 | 4489-SNOJF   | MonthlyCharges | 7225     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2631 | 4115-BNPJY   | MonthlyCharges | 7555     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2668 | 9993-LHIEB   | MonthlyCharges | 6785     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2680 | 5641-DMBFJ   | MonthlyCharges | 8430     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2683 | 0114-PEGZZ   | MonthlyCharges | 10755    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2698 | 1202-KKGFU   | MonthlyCharges | 5420     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2702 | 8118-LSUEL   | MonthlyCharges | 10640    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2734 | 1697-NVVGY   | MonthlyCharges | 6640     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2827 | 0909-SELIE   | MonthlyCharges | 8080     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2839 | 8755-IWJHN   | MonthlyCharges | 9535     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2867 | 5583-SXDAG   | MonthlyCharges | 7000     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2887 | 7858-GTZSP   | MonthlyCharges | 8655     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2935 | 9504-YAZWB   | MonthlyCharges | 2025     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      2956 | 7969-FFOWG   | MonthlyCharges | 1990     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3028 | 0058-EVZWM   | MonthlyCharges | 8980     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3034 | 4381-MHQDC   | MonthlyCharges | 6500     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3091 | 3022-BEXHZ   | MonthlyCharges | 11120    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3141 | 4770-QAZXN   | MonthlyCharges | 1945     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3148 | 9867-JCZSP   | MonthlyCharges | 2075     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3168 | 2974-GGUXS   | MonthlyCharges | 9195     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3245 | 4626-GYCZP   | MonthlyCharges | 9385     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3249 | 0795-XCCTE   | MonthlyCharges | 2540     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3252 | 4086-YQSNZ   | MonthlyCharges | 8040     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3358 | 9940-HPQPG   | MonthlyCharges | 9175     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3425 | 4999-IEZLT   | MonthlyCharges | 2945     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3501 | 5286-YHCVC   | MonthlyCharges | 10480    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3554 | 3656-TKRVZ   | MonthlyCharges | 5535     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3585 | 5018-GWURO   | MonthlyCharges | 8560     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3610 | 7517-LDMPS   | MonthlyCharges | 8460     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3675 | 3097-NNSPB   | MonthlyCharges | 4905     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3679 | 9526-BIHHD   | MonthlyCharges | 2970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3699 | 5569-OUICF   | MonthlyCharges | 10130    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3703 | 4412-YLTKF   | MonthlyCharges | 7805     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3715 | 8050-WYBND   | MonthlyCharges | 4945     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3732 | 6874-SGLHU   | MonthlyCharges | 9700     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3772 | 5499-ECUTN   | MonthlyCharges | 6605     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3810 | 0320-DWVTU   | MonthlyCharges | 9950     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3842 | 0516-WJVXC   | MonthlyCharges | 5420     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3866 | 7361-YPXFS   | MonthlyCharges | 6445     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3869 | 0103-CSITQ   | MonthlyCharges | 10940    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3952 | 3482-ABPKK   | MonthlyCharges | 5430     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      3955 | 1384-RCUXW   | MonthlyCharges | 8055     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4003 | 7594-LZNWR   | MonthlyCharges | 6915     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4082 | 4198-VFOEA   | MonthlyCharges | 3360     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4127 | 8884-FEEWR   | MonthlyCharges | 2060     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4183 | 8191-XWSZG   | MonthlyCharges | 2065     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4202 | 4713-ZBURT   | MonthlyCharges | 9970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4216 | 3724-UCSHY   | MonthlyCharges | 1955     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4271 | 4565-NLZBV   | MonthlyCharges | 2465     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4285 | 2856-HYAPG   | MonthlyCharges | 6865     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4373 | 8439-LTUGF   | MonthlyCharges | 2000     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4471 | 0604-THJFP   | MonthlyCharges | 7595     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4624 | 5539-TMZLF   | MonthlyCharges | 6975     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4691 | 6259-WJQLC   | MonthlyCharges | 8110     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4726 | 3417-TSCIC   | MonthlyCharges | 2485     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4780 | 0228-MAUWC   | MonthlyCharges | 5955     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4827 | 0277-BKSQP   | MonthlyCharges | 5440     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4877 | 4927-WWOOZ   | MonthlyCharges | 9145     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4907 | 7994-UYIVZ   | MonthlyCharges | 8565     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4952 | 3460-TJBWI   | MonthlyCharges | 2420     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      4978 | 5014-GSOUQ   | MonthlyCharges | 1995     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5053 | 5774-QPLTF   | MonthlyCharges | 2035     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5054 | 1485-YDHMM   | MonthlyCharges | 9325     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5064 | 3244-DCJWY   | MonthlyCharges | 7025     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5119 | 6988-CJEYV   | MonthlyCharges | 9870     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5128 | 7065-YUNRY   | MonthlyCharges | 4530     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5140 | 5447-VYTKW   | MonthlyCharges | 5345     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5198 | 4307-KWMXE   | MonthlyCharges | 3575     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5317 | 6681-ZSEXG   | MonthlyCharges | 5950     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5347 | 4686-UXDML   | MonthlyCharges | 9985     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5351 | 9172-ANCRX   | MonthlyCharges | 9870     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5382 | 2806-MLNTI   | MonthlyCharges | 10510    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5443 | 4716-MRVEN   | MonthlyCharges | 2000     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5495 | 2621-UDNLU   | MonthlyCharges | 2085     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5562 | 2576-HXMPA   | MonthlyCharges | 1955     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5614 | 3247-MHJKM   | MonthlyCharges | 2020     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5770 | 1740-CSDJP   | MonthlyCharges | 3525     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5785 | 3870-MQAMG   | MonthlyCharges | 11035    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5834 | 6999-CHVCF   | MonthlyCharges | 10210    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5878 | 5397-NSKQG   | MonthlyCharges | 5090     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5886 | 5228-EXCET   | MonthlyCharges | 8085     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5944 | 5498-IBWPI   | MonthlyCharges | 4940     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5945 | 4067-HLYQI   | MonthlyCharges | 7040     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5955 | 9475-NNDGC   | MonthlyCharges | 11315    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5964 | 6987-XQSJT   | MonthlyCharges | 7950     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5979 | 3547-LQRIK   | MonthlyCharges | 2690     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5986 | 1172-VIYBP   | MonthlyCharges | 6970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      5997 | 0825-CPPQH   | MonthlyCharges | 1910     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6003 | 4324-AHJKS   | MonthlyCharges | 5580     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6009 | 9732-EQMWY   | MonthlyCharges | 9940     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6031 | 1401-FTHFQ   | MonthlyCharges | 2000     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6044 | 9236-NDUCW   | MonthlyCharges | 3510     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6104 | 4208-UFFGW   | MonthlyCharges | 4495     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6110 | 9592-ERDKV   | MonthlyCharges | 7925     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6116 | 3181-VTHOE   | MonthlyCharges | 5105     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6136 | 6260-ONULR   | MonthlyCharges | 6280     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6178 | 4335-UPJSI   | MonthlyCharges | 1975     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6221 | 0655-YDGFJ   | MonthlyCharges | 4895     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6298 | 4554-YGZIH   | MonthlyCharges | 9005     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6313 | 0125-LZQXK   | MonthlyCharges | 10135    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6324 | 6368-NWMCE   | MonthlyCharges | 6815     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6383 | 9114-VEPUF   | MonthlyCharges | 9610     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6403 | 8640-SDGKB   | MonthlyCharges | 7440     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6494 | 7025-WCBNE   | MonthlyCharges | 5960     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6509 | 5875-YPQFJ   | MonthlyCharges | 6990     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6598 | 5073-RZGBK   | MonthlyCharges | 8005     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6643 | 2038-YSEZE   | MonthlyCharges | 6745     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6714 | 0621-CXBKL   | MonthlyCharges | 1870     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6727 | 0661-KQHNK   | MonthlyCharges | 1900     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6744 | 4129-LYCOI   | MonthlyCharges | 10400    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6775 | 3134-DSHVC   | MonthlyCharges | 9800     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6792 | 1583-IHQZE   | MonthlyCharges | 11295    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6887 | 9244-ZVAPM   | MonthlyCharges | 4560     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6900 | 2186-QZEYA   | MonthlyCharges | 5855     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6911 | 1153-GNOLC   | MonthlyCharges | 3910     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6915 | 8473-VUVJN   | MonthlyCharges | 7365     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6937 | 4115-UMJFQ   | MonthlyCharges | 3575     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      6979 | 9873-MNDKV   | MonthlyCharges | 4465     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7006 | 4851-BQDNX   | MonthlyCharges | 8505     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7024 | 8292-TYSPY   | MonthlyCharges | 5500     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7076 | 0831-JNISG   | MonthlyCharges | 1980     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7111 | 2796-NNUFI   | MonthlyCharges | 1995     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7147 | 0247-SLUJI   | MonthlyCharges | 1970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7154 | 6859-RKMZJ   | MonthlyCharges | 5505     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7206 | 7105-MXJLL   | MonthlyCharges | 6070     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7217 | 2843-CQMEG   | MonthlyCharges | 4970     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7240 | 9330-IJWIO   | MonthlyCharges | 10035    | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
|      7253 | 4116-TZAQJ   | MonthlyCharges | 7425     | kept, flagged charge_outlier | about 100 times the normal range; left out of revenue numbers |
