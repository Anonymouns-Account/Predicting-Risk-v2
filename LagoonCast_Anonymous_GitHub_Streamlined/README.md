# Parkside Aquatic Park: machine-learning classification of bacteria exceedances

This repository contains the data, Python code, notebooks, saved predictions, and analysis outputs for a retrospective study of *E. coli* and *Enterococcus* at Parkside Aquatic Park (San Mateo, California). It is a research archive, separate from any public-facing LagoonCast application.

## Repository layout

```text
code/         E. coli and Enterococcus research pipelines; result verification
data/         October 2026 model-ready dataset
docs/         Model metadata and methodological limitations
figures/      Model diagnostics and EDA plots generated from observed data
notebooks/    Notebook entry points for the same Python pipelines
outputs/      Selected models, predictions, validation, metrics and diagnostics
```

## Reproduce the analyses

Use Python 3.13 where possible. Install the tested dependency set:

```bash
python -m pip install -r requirements.txt
python code/verify_saved_results.py
python code/e_coli_v19.py
python code/enterococcus_v16_2.py
```

Run from the repository root, so that the scripts locate `data/Aquacast20Years_Weekly_UPDATED_TO_2026_10(2).csv`. Alternatively, open `notebooks/e_coli_v19.ipynb` or `notebooks/enterococcus_v16_2.ipynb` from a checkout of the repository. Both pipelines are computationally heavier than the saved-result verification script.

## Research scope

The two final models are **not identical pipelines**:

- **E. coli V19:** Extra Trees with 23 environmental predictors, annual five-year retraining, and an additional adjustment using older laboratory measurements (minimum 28-day assumed publication lag). Historical development period: 2018–2023. Threshold: 0.47455.
- **Enterococcus V16.2:** Extra Trees with 11 environmental predictors and historical six-fold chronological evaluation. No laboratory-history adjustment. Threshold: 0.425.

Measured bacteria values are labeled using single-sample research thresholds of 400 MPN/100 mL for E. coli and 104 MPN/100 mL for Enterococcus. The 2024–2026 reported outcomes are **retrospective**, not prospective seven-day forecasts. The E. coli result assumes historical laboratory findings were available after 28 days, which has not been independently verified against publication timestamps.

## Saved performance

| Indicator | Retrospective n | Recall | Precision | TP / FP / FN / TN |
|---|---:|---:|---:|---:|
| E. coli | 144 | 86.8% | 63.9% | 46 / 26 / 7 / 65 |
| Enterococcus | 144 | 70.3% | 47.3% | 26 / 29 / 11 / 78 |

The per-sample probability outputs, validation tables, uncertainty estimates, and selected trained models are in `outputs/`. `code/verify_saved_results.py` checks that the saved predictions reproduce the table above and that the dataset matches the expected SHA-256.

See `docs/REPRODUCIBILITY_NOTES.md` and `DATA_SOURCES.md` for data and methodological limitations. Refer to `AI_USE_STATEMENT.md` for the AI-assistance disclosure; confirm that the submitted manuscript carries an accurate matching statement.
