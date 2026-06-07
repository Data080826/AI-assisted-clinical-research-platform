# 📚 Clinical Research Copilot

An AI-powered clinical research assistant that helps researchers move from literature discovery to study design and preliminary statistical analysis in a single workflow.

Built with **Python**, **Streamlit**, **OpenAI**, and **PubMed (NCBI Entrez API)**.

---

## 🚀 Features

### 🔎 Literature Search

Search PubMed directly from the application using any clinical research topic.

Examples:

* Semaglutide chronic kidney disease
* Heart failure and SGLT2 inhibitors
* Cardiovascular outcomes in rare diseases

The application retrieves:

* Article titles
* Journals
* Publication dates
* PMIDs
* Abstracts

---

### 🧠 AI Literature Review

Automatically analyzes retrieved publications and generates:

* Literature overview
* Major findings
* Areas of agreement
* Areas of disagreement
* Current limitations
* Knowledge gaps
* Future research directions

---

### 🔍 Research Gap Identification

Uses large language models to identify:

* Major knowledge gaps
* Understudied populations
* Unanswered clinical questions
* High-impact future research opportunities

Each gap is ranked by:

* Clinical impact
* Novelty
* Feasibility

---

### 🎯 Research Question Generator

Transforms identified research gaps into:

* Primary research questions
* PICO framework
* Hypotheses
* Primary outcomes
* Secondary outcomes
* Recommended study designs

---

### 📋 Study Design Generator

Creates detailed clinical study protocols including:

* Study design selection
* Population definition
* Inclusion criteria
* Exclusion criteria
* Exposure definition
* Comparator groups
* Outcomes
* Statistical analysis plan
* Database requirements
* TriNetX/Epic Cosmos cohort recommendations

---

### 📊 Dataset Analysis

Upload CSV or Excel datasets for automated review.

Generates:

* Dataset overview
* Variable inventory
* Missing value assessment
* Dataset structure summary

---

### 📈 Statistical Analysis

Built-in analytics include:

#### Descriptive Statistics

* Mean
* Standard deviation
* Quartiles
* Min/Max values

#### Categorical Variable Analysis

* Counts
* Percentages
* Frequency tables

#### Group Comparisons

Welch's Two-Sample T-Test:

* Mean comparison
* P-value calculation
* Automatic validation of binary grouping variables

---

## 🛠 Technology Stack

### Frontend

* Streamlit

### AI

* OpenAI GPT Models

### Biomedical Data

* PubMed
* NCBI Entrez API

### Data Analysis

* Pandas
* NumPy
* SciPy
* Statsmodels

---

## 📂 Project Structure

```text
clinical-research-copilot/

├── app.py
│
├── modules/
│   ├── literature.py
│   ├── gaps.py
│   ├── question_builder.py
│   ├── study_design.py
│   ├── dataset_analysis.py
│   └── statistical_analysis.py
│
├── services/
│   ├── ncbi.py
│   └── openai_service.py
│
├── prompts.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/clinical-research-copilot.git

cd clinical-research-copilot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Secrets

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY="your_openai_api_key"

NCBI_EMAIL="your_email@example.com"

NCBI_API_KEY="your_ncbi_api_key"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## Example Workflow

1. Enter a clinical research topic
2. Search PubMed
3. Generate AI literature summary
4. Identify research gaps
5. Generate research questions
6. Create a study design
7. Upload a dataset
8. Perform descriptive statistics
9. Run comparative analyses

---

## Future Improvements

* Forest plots
* Kaplan-Meier survival analysis
* Logistic regression
* Cox proportional hazards models
* Meta-analysis support
* Automated manuscript drafting
* RAG-enhanced literature review
* TriNetX integration
* Epic Cosmos integration
* Citation export (BibTeX, RIS)

---

## Disclaimer

This application is intended for research and educational purposes only.

Generated outputs should be reviewed by qualified clinicians, statisticians, and researchers before use in clinical decision-making or publication.

---

## License

MIT License
