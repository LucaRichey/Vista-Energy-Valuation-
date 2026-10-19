# Project 1 Submission Manifest & Checklist
**Course:** Corporate Finance Application  
**Target Security:** Vista Energy, S.A.B. de C.V. (NYSE: VIST)  
**Valuation Date:** October 8, 2026  
**Due Date:** October 19, 2026 11:59 PM  
**Total Points:** 300 Points  

---

## 1. Uniform Seven-Part Submission Bundle Checklist

| Part # | Required Submission Element | File Path / Location | Rubric Criterion Addressed | Status |
|:---:|---|---|---|:---:|
| **Part 1A** | **Unchanged Edition A Checkpoint** | `docs/EDITION_A_BASELINE.md` | Problem Definition & Scope (45 pts) | **COMPLETE** |
| **Part 1B** | **Edition B Final Submission** | `docs/EDITION_B_FINAL_MEMO.md` | Problem Definition & Scope (45 pts) | **COMPLETE** |
| **Part 2** | **Repository & Visible Run Output** | `run_analysis.py`<br>`engine/*.py`<br>`docs/COLD_RUN_EVIDENCE.md` | Technical Execution & Usability (45 pts)<br>Data Traceability (45 pts) | **COMPLETE** |
| **Part 3** | **Video 1: Research Evolution** | `docs/VIDEO_TRANSCRIPTS_AND_SCRIPTS.md` (Part 1)<br>Video File: `Project 1 - Video 1.mov` (Duration: 3m 10s) | Professional Communication (30 pts)<br>Data Traceability (45 pts) | **COMPLETE** |
| **Part 4** | **Video 2: Code & Validation Suite** | `docs/VIDEO_TRANSCRIPTS_AND_SCRIPTS.md` (Part 2)<br>Video File: `Project 1 - Video 2.mov` (Duration: 4m 54s) | Validation & Reproducibility (75 pts)<br>Technical Execution (45 pts) | **COMPLETE** |
| **Part 5** | **Investment Committee Memo & Deck** | `docs/EDITION_B_FINAL_MEMO.md` | Financial Soundness & Judgment (60 pts)<br>Professional Communication (30 pts) | **COMPLETE** |
| **Part 6** | **Video 3: Committee Defense & Transcripts** | `docs/VIDEO_TRANSCRIPTS_AND_SCRIPTS.md` (Part 3)<br>Video File: `Project 1 - Video 3.mov` (Duration: 5m 57s) | Professional Communication (30 pts)<br>Financial Judgment (60 pts) | **COMPLETE** |
| **Part 7** | **Frozen Validation & AI-Use Records** | `docs/LOCKED_CHANGED_INPUT_RECORD.md`<br>`docs/ASSUMPTION_CHALLENGE_RECORD.md`<br>`docs/CONTAMINATION_CATALOG.md`<br>`docs/AI_GOVERNANCE_AND_AUDIT.md`<br>`docs/PEER_POLICY_AND_MULTIPLES.md` | Validation & Sensitivity (75 pts)<br>Financial Soundness (60 pts)<br>Data Integrity (45 pts) | **COMPLETE** |

---

## 2. Analytic Rubric Mapping (300 Total Points)

### Criterion 1: Problem Definition & Decision Usefulness (45 Points)
- **Target Standard:** Intended user, action, horizon, constraints, Edition A/B boundary, and committee ask are explicit; analysis changes a real decision.
- **Evidence in Bundle:**
  * Defined intended user: Buy-Side Energy Strategy Fund.
  * Explicit action: Initiate 60% active long position; reserve 40% for cyclical dips.
  * Clear decision horizon: 3–5 years (FY2025E–FY2029E).
  * Strict gate enforcement: Rejected broker-dealers/banks (HOOD); qualified pure E&P operating target (VIST).
  * Frozen Edition A document: `docs/EDITION_A_BASELINE.md`.

### Criterion 2: Data Integrity & Traceability (45 Points)
- **Target Standard:** Material inputs have source, as-of date, definitions, transformations, exclusions, and reproducible lineage; revisions/licensing/privacy are handled.
- **Evidence in Bundle:**
  * Complete source map in `docs/CONTAMINATION_CATALOG.md`.
  * Verifiable SEC Form 20-F reconciliation (Item 5 & Item 18).
  * Normalized base year for conventional asset divestments and PEPASA acquisition diluted shares.
  * Explicit distinction between Facts (F), Normalizations (N), Forecasts (E), and Model Outputs (M).

### Criterion 3: Financial Soundness & Judgment (60 Points)
- **Target Standard:** Conventions, units, bridges, benchmarks, constraints, and scenarios are correct; recommendation is a defensible range/action with risks and reversal triggers.
- **Evidence in Bundle:**
  * 5-year articulating pro-forma with loud checks in `engine/model.py`.
  * FCFF engine with mid-year convention and dynamic interest tax-shield accounting.
  * Enterprise-to-Equity Bridge accounting for cash ($764M), gross debt ($1,544M), and ARO/leases ($140M).
  * Defensible valuation range ($43.15 to $139.96) rather than false point precision.
  * Explicit material conditions and three non-negotiable reversal triggers.

### Criterion 4: Technical Execution & Usability (45 Points)
- **Target Standard:** Clean user can reproduce visible result; architecture/data flow are coherent; errors, credentials, dependencies, and output are handled safely.
- **Evidence in Bundle:**
  * Locally runnable with zero third-party dependencies (`python3 run_analysis.py`).
  * Modular architecture (`model.py`, `sensitivity.py`, `multiples.py`, `scenarios.py`, `validation.py`).
  * Formatted CLI tables showing complete 3-statement forecast, bridge, matrix, and checks.
  * Logged cold-run verification in `docs/COLD_RUN_EVIDENCE.md`.

### Criterion 5: Validation, Sensitivity & Reproducibility (75 Points)
- **Target Standard:** Known answers, complete Locked Changed-Input Record with human-authored AI-off prediction plus predicted and actual decision effect, robustness/failure tests, AI-output checks, and cold-run evidence target the highest-risk claims; limitations drive action.
- **Evidence in Bundle:**
  * Synthetic known-answer closed-form DCF test: Exact 0.000000 match.
  * Independent source/definition check on lifting cost and realized prices.
  * Pre-execution directional monotonicity checks across WACC, growth, volume, and costs.
  * Locked Changed-Input Record (`docs/LOCKED_CHANGED_INPUT_RECORD.md`) logged at `2026-10-08 11:30:00 EDT` with human AI-off prediction matching model within 0.01%.
  * Loud pro-forma articulation check: Balance sheet gap = $0.0000 every year; cash ties to cash flow.
  * Highest-risk distress failure test (oil at $35/bbl) handled gracefully.
  * Reverse-DCF solving for market-implied price ($54.54/boe) and WACC (15.47%).
  * AI audit record in `docs/AI_GOVERNANCE_AND_AUDIT.md`.

### Criterion 6: Professional Communication (30 Points)
- **Target Standard:** Memo/deck, README, manifest, transcripts, and three distinct videos are accurate, concise, internally consistent, accessible, and fit their audiences.
- **Evidence in Bundle:**
  * Institutional Buy-Side Memo & Deck in `docs/EDITION_B_FINAL_MEMO.md`.
  * Comprehensive master `README.md`.
  * Storyboards, slide cues, and word-for-word corrected transcripts for all three videos in `docs/VIDEO_TRANSCRIPTS_AND_SCRIPTS.md`.
  * Internal numerical consistency across all code, tables, and prose.
