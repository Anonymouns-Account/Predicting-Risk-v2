# Reproducibility notes

## Randomness

Both pipelines set `SEED = 42`. The selected Extra Trees models and other stochastic estimators use `random_state=SEED`. The saved models were independently inspected and their `random_state` values were 42. E. coli uses deterministic annual refits; Enterococcus performs chronological historical candidate comparisons. Running the same environment and exact CSV is required for exact numerical reproduction.

## Two distinct research procedures

**E. coli V19:** 23-feature hybrid rainfall set, Extra Trees, previous five years of training for each evaluation year (2024, 2025, 2026), with a 12-month lagged laboratory-prevalence odds adjustment using a minimum 28-day assumed release lag. Publication dates are not verified. Cutoff: 0.4745500067334312 chosen from 2018–2023 historical predictions. Saved `.joblib` contains base annual estimators; the odds adjustment is applied in code, not embedded in those estimators.

**Enterococcus V16.2:** 11-feature seasonal set, Extra Trees, historical chronological validation using 2012–2023, trained on pre-2024 records for retrospective evaluation. Probability cutoff: 0.425. No lagged laboratory-history adjustment in the final Enterococcus model.

## Why the evaluation is retrospective

The 2024–2026 period was inspected during earlier model experiments. It is not an untouched independent test or a validated seven-day-ahead prediction. Weather predictors are observed variables aligned with sample dates. Calibration and threshold sensitivity in the exports describe model behavior but do not justify retuning the final decision cutoff on the evaluation period.

## Verified counts

| Indicator | Samples | TN | FP | FN | TP | Recall | Precision |
|---|---:|---:|---:|---:|---:|---:|---:|
| E. coli | 144 | 65 | 26 | 7 | 46 | 86.8% | 63.9% |
| Enterococcus | 144 | 78 | 29 | 11 | 26 | 70.3% | 47.3% |

The `code/verify_saved_results.py` script recalculates these counts from the saved prediction CSVs. Other output tables and diagnostic figures are archived under `outputs/` and `figures/`.
