# FINAL_ERIA
Education Regulation Impact Analyzer (ERIA) Simplifying Education Policies and Circulars for Every Institution
# 🎓 ERIA: Education Regulation Impact Analyzer
### *Simplifying Education Policies and Circulars for Every Institution*

ERIA is an AI-powered EdTech and Policy Analytics platform built to decode complex academic, legal, and administrative language found in education policies, university regulations, and circulars. 

By ingesting official documents (from bodies like **UGC, AICTE, NAAC, NIRF, and the Ministry of Education**), ERIA extracts real meaning, traces policy timelines, and maps multi-tier stakeholder impacts, allowing academic planners, students, and institutions to ensure seamless compliance without requiring deep policy expertise.

---

## 🛠️ Core Skills & Architecture Demonstrated
- **Document Ingestion:** High-fidelity PDF layer text extraction and layout parsing.
- **NLP Preprocessing & Structuring:** High-context rule-based regex wrappers combined with advanced text structuring.
- **Topic Classification:** Automated sorting into core domains (Accreditation, Scholarship, Curriculum, Faculty Policy, Examination, Admissions).
- **Chronology & Dependency Graphing:** Conceptual flow mapping tracking predecessor circulars, historic amendments, and framework roots.
- **Stakeholder & Sentiment Audit:** Extracting quantitative risk indices across 6 distinct academic groups.
- **LLM-Powered Summarization:** 10-20 line targeted programmatic digest via **Groq Engine (Llama 3.3)**.
- **Interactive UI Dashboard:** Built natively on Streamlit with structured state caching to prevent runtime glitches.

---

## 💼 Business Use Cases Addressed

1. **Simplified Regulation Summaries:** Condenses verbose compliance text into a student/faculty-friendly 10-20 line direct impact statement.
2. **Chronology & Policy Evolution Tracking:** Explicitly calls out prior related circulars, historic frameworks, and structural changes.
3. **Granular Stakeholder Impact Mapping:** Analyzes positive, neutral, or restrictive impacts specifically isolated for:
   - Students & Scholarship Applicants
   - Faculty Members & Researchers
   - Colleges, Universities, and Academic Administrators
   - Accreditation and Quality Assurance Teams
4. **Structured Impact Forecasting:** Splits operational burdens down into actionable time horizons (Short-term <1 yr, Medium-term 1-5 yrs, Long-term >5 yrs).
5. **Governance & Compliance Optimization:** Alerts institutions ahead of time regarding shifts in documentation workload, academic readiness checks, or procedural barriers.

---

## 📦 Project Directory Structure

```text
├── app.py                  # Main Streamlit Multi-Page Interface Pipeline
├── requirements.txt        # Verified external Python dependencies
├── pdf_reader.py           # Custom layout ingestion utility for PDF source files
├── groq_analyzer.py        # Groq Client Wrapper (Inference handling)
├── report_generator.py     # Structural programmatic layout PDF output engine
└── README.md               # Complete platform documentation
