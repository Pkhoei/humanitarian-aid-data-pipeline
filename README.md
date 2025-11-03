![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

# Humanitarian Aid Data Pipeline

### 🧭 Overview
An end-to-end data pipeline designed to analyze humanitarian aid distribution across countries and regions.  
This project demonstrates how data engineering and analysis can support better humanitarian decision-making — in line with the mission of organizations like the Red Cross.

---

### 🎯 Objectives
- Collect and clean open humanitarian datasets (e.g., UN OCHA, World Bank)  
- Ensure **data quality and governance** through structured ETL  
- Design **dbt data models** for better traceability  

---

### 🧰 Tech Stack
- **Programming:** Python (Pandas, NumPy, Matplotlib, Scikit-learn)  
- **Data Visualization:** Power BI  
- **Workflow & Storage:** Azure, GitHub Actions  
- **Documentation:** Markdown, PowerPoint  

---

### 📊 Dataset
- **Source:** Open humanitarian datasets (e.g., UN OCHA, World Bank)  
- **Format:** CSV / Excel files containing country, aid type, and allocation amount  
- **Size:** ~50MB (to be updated)  

---

### 🔄 Pipeline (ETL/ELT)
1. **Ingest**  
   - Sources: UN OCHA FTS (CSV), World Bank Indicators (CSV/API)  
   - Store → `data/raw/`  

2. **Quality & Validation**  
   - Handle missing values, type checks, duplicates  
   - Store → `data/clean/`  

3. **Transform & Model**  
   - Pandas transforms / dbt models (`staging` → `core` → `marts`)  
   - Store → `models/` (or `data/processed/`)  

4. **Load & Analytics**  
   - Export curated tables for BI  
   - Power BI dashboard in `dashboards/`  

5. **Orchestration (CI/CD)**  
   - Placeholder workflow: `.github/workflows/pipeline.yml`  
   - Triggers: on push + optional daily schedule  

---

### 📁 Repository Structure
