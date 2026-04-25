# DSCI 644: Data Cleaning Approaches in Data Engineering Tasks with LLM Integrations

This project was done as a part of the semester-long project for RIT's DSCI 644 course using
software engineering principles and data science approaches. We chose the MTP challenge, and
evaluated byLLM's Meaning-Typed Programming approach for automated data cleaning compared to 
traditional prompt-based and regex-based methods. 

---

## Research Question
For dirty datasets, can the `by` operator (via byLLM) detect and repair dirty records 
(e.g., inconsistent date formats, missing labels) with a lower misinterpretation rate 
and comparable or better precision/recall than regex-based scripts and prompt-based 
LLM calls?

---

## Datasets
- **FDIC-Insured Banks and Branches:**
- **Iowa Liquor Sales:**

Both datasets were subsetted to 250 rows for LLM-based cleaning to stay within 
free-tier API limits.

---

## Approaches Used
| Approach         | Description                                                                      | Model          |
|------------------|----------------------------------------------------------------------------------|----------------|
| Manual Typing    | Regex-based pandas scripts and used as ground truth dataset                      | N/A            |
| Manual Prompting | Detailed prompt used via Gemini web interface and generated pipeline run locally | Gemini 3       |
| byLLM            | `by` operator with MTP used and one API call per column                          | Gemini 3 Flash |

---

## Environment Setup

### Requirements
pandas  
numpy  
scikit-learn  
byllm  


Install requirements with:
```bash
pip install -r requirements.txt
```

### API Key
byLLM requires a Google Gemini API key. You will want to set it as an environment variable in your own API key file.

---

## How to Run and Do the Project

### 1. Subset the data
```bash
python data/data_subset.py
```

### 2. Run cleaning notebooks
Open and run in order for each dataset:
1. `cleaning/fdic_cleaning/manual_cleaning.ipynb`, which will creat ethe ground truth set
2. `cleaning/fdic_cleaning/manual_prompting.ipynb`, which will create the manual prompting set
3. `cleaning/fdic_cleaning/byLLM_cleaning.ipynb`, which will create the byLLM set. 

Repeat all three for the `iowa_cleaning/` datasets.

### 3. Run analysis notebooks
1. `analysis/fdic_analysis/manual_analysis.ipynb`
2. `analysis/fdic_analysis/byLLM_analysis.ipynb`

Repeat for `iowa_liquor_analysis/`. For a brief combined summary of both sets, run `analysis/analysis.ipynb`.

---

_DSCI 644 Spring 2026_