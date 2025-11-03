# Humanitarian Aid — Data Dictionary

This data dictionary documents the fields used in the project’s humanitarian aid dataset.

## Table: humanitarian_clean.csv

| Column          | Type    | Example           | Description                                                             | Rules / Quality Notes                                   |
|-----------------|---------|-------------------|-------------------------------------------------------------------------|---------------------------------------------------------|
| country         | string  | Kenya             | Recipient country                                                       | Title-cased, trimmed, non-null                          |
| year            | int     | 2022              | Calendar year of aid allocation                                         | 2000–2030, non-null                                     |
| aid_type        | string  | Health            | Category of aid (Health, Education, Shelter, Food, WASH, etc.)         | Controlled list, title-cased                            |
| organization    | string  | Red Cross         | Donor/implementing org                                                  | Defaults to “Unknown” if missing                        |
| amount_usd      | float   | 1250000.0         | Allocation amount in USD                                                | >= 0, non-null                                          |
| region          | string  | Sub-Saharan Africa| Optional geographic region                                              | Optional                                                |

### Data Quality Checks
- No nulls in: `country`, `year`, `aid_type`, `amount_usd`
- Value ranges: `year ∈ [2000, 2030]`, `amount_usd ≥ 0`
- Normalization: `country`, `aid_type` are title-cased and trimmed
- Defaults: `organization = "Unknown"` when missing

### Provenance
- Source: Open humanitarian datasets (e.g., UN OCHA, World Bank) — sample synthetic for demo
- Transformations: see `scripts/ingest.py`
