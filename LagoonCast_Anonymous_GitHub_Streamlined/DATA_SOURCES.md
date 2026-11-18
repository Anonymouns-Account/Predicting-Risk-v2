# Data sources and compilation

The master dataset is `data/Aquacast20Years_Weekly_UPDATED_TO_2026_10(2).csv`.

- Laboratory measurements: California Water Boards / California Open Data Portal, *Surface Water Fecal Indicator Bacteria Results*. https://publish.data.ca.gov/dataset/surface-water-fecal-indicator-bacteria-results
- Weather measurements: NOAA/NCEI daily summaries. https://www.ncei.noaa.gov/access/search/data-search/daily-summaries/
- Weather station identifiers in the compiled records include Redwood City (`USC00047339`) and a supplementary Foster City precipitation station (`US1CASM0006`).

## File identity

- SHA-256: `6ee536b6e0051d087277726ae02ecc7d2bf23960752febc2160e6f884aa52485`
- 1,890 combined sampling records, 137 source columns.
- E. coli: 955 observations, 283 exceedance labels (>=400 MPN/100 mL).
- Enterococcus: 935 observations, 225 exceedance labels (>=104 MPN/100 mL).

The CSV is a model-ready compilation. The source record aggregation and all upstream weather-feature engineering are not fully reconstructed from raw state and NOAA downloads in this repository. Historical laboratory method, censoring, and exact posting-date metadata are incomplete. Do not treat the date-aligned retrospective results as a seven-day-ahead forecast validation.
