# Nepal: Data quality notes

- Country: Nepal (NPL). Analysis period: 2010–2024.
- Working dataset: data/processed/nepal_wdi_2010_2024_working.csv.
- All 15 implemented structural and plausibility checks passed.
- Secondary school enrollment is missing for 2018.
- Forest area is missing for 2024.
- Exact-year API rechecks returned no value for both missing observations.
- Missing observations remain missing; no interpolation or imputation was applied.
- Each calculation uses the available observations for its indicator.
- The assigned CO2 code EN.ATM.CO2E.PC failed to download.
- The working dataset uses EN.GHG.CO2.PC.CE.AR5 as a clearly labelled alternative:
  CO2 emissions excluding LULUCF per capita, measured in t CO2e/capita.
- This alternative is downloaded through World Bank WDI; its metadata identifies
  EDGAR/JRC–European Commission and IEA as underlying sources.
- Instructor acceptance of the CO2 substitution remains to be confirmed.
- Raw responses, download records and variable definitions are preserved.
