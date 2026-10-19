# Project 1 — Corporate Finance Application: Vista Energy (NYSE: VIST)

> **Embedded AI Task Force Buy-Side Valuation Stack & Decision Engine**  
> **Target Security:** Vista Energy, S.A.B. de C.V. (NYSE: VIST / BMV: VISTA)  
> **Valuation Date:** October 8, 2026 | **Current Price:** $65.00/share  
> **Recommendation:** **INITIATE ACTIVE LONG POSITION (OVERWEIGHT / ACCUMULATE)**  
> **Defensible Valuation Range:** **$43.15 – $139.96 per share** (Base Target: **$88.26**, +35.8% Upside)  
> **Primary Methodology:** 5-Year Articulating Three-Statement Pro-Forma & FCFF / WACC DCF Bridge  

---

## Workspace Setup Recommendation

The user currently does not have an active workspace set in their environment. It is strongly recommended to set this directory as your active workspace in Antigravity / your IDE:
```bash
/Users/lucarichey/.gemini/antigravity/scratch/vista_energy_project1
```

---

## Quickstart: How to Run

The entire modeling and validation engine requires **zero external third-party dependencies** (built strictly using Python's standard library):

```bash
# Navigate to the project root
cd /Users/lucarichey/.gemini/antigravity/scratch/vista_energy_project1

# Execute the complete end-to-end analysis and validation suite
python3 run_analysis.py
```

To run individual validation checks:
```bash
python3 -c "from engine.validation import run_all_validations; [print(v['name'], ':', '[PASS]' if v.get('passed', True) else '[FAIL]') for v in run_all_validations()]"
```

---

## System Architecture & Modular Structure

```
vista_energy_project1/
├── README.md                           # Master Project Guide & Reproduction Instructions
├── run_analysis.py                     # Master Executable CLI Runner (Visible Grader Output)
├── engine/                             # Core Financial Modeling & Valuation Modules
│   ├── model.py                        # 3-Statement Articulating Pro-Forma & FCFF/WACC DCF Engine
│   ├── sensitivity.py                  # 2D WACC x Growth Matrix, OAT Spans & Reverse-DCF Solver
│   ├── multiples.py                    # Peer Policy, Comparable Multiples & Method Disagreement
│   ├── scenarios.py                    # Causal Cases (High/Base/Low) & Severe Downside Stress Case
│   └── validation.py                   # Automated Test Suite (Closed-Form Benchmark, Locked Record, Covenants)
└── docs/                               # Formal Submission Documents & Evidentiary Records
    ├── EDITION_A_BASELINE.md           # Week 2 Supervised Baseline Window Checkpoint (Pre-AI Judgment)
    ├── EDITION_B_FINAL_MEMO.md         # Final Buy-Side Investment Committee Memo & Defense Deck
    ├── CONTAMINATION_CATALOG.md        # Form 20-F Historical Traceability & One-Time Normalizations
    ├── ASSUMPTION_CHALLENGE_RECORD.md  # Every Load-Bearing Driver: Value · Basis · Challenge · Evidence
    ├── LOCKED_CHANGED_INPUT_RECORD.md  # Frozen AI-Off Human Prediction & Verification Audit
    ├── PEER_POLICY_AND_MULTIPLES.md    # Pre-Screened Peer Policy, Multiple Matrices & Transaction Qualification
    ├── AI_GOVERNANCE_AND_AUDIT.md      # Accepted, Corrected, Qualified & Rejected AI Output Record
    ├── COLD_RUN_EVIDENCE.md            # Fresh Environment Execution Log & Zero-Leakage Output
    ├── VIDEO_TRANSCRIPTS_AND_SCRIPTS.md# Storyboards, Slide Cues & Word-for-Word Transcripts for Videos 1, 2, 3
    └── SUBMISSION_MANIFEST.md          # Complete 7-Part Submission Bundle Checklist (300-Pt Rubric Mapping)
```

---

## Executive Investment Summary

### 1. Valuation & Decision Summary
- **Current Trading Price:** **$65.00 per share** (Market Cap: ~$7.15B | EV: ~$7.93B).
- **Base Case DCF Target:** **$88.26 per share** (+35.8% upside at WACC = 12.67%, $g = 2.0\%$).
- **Defensible Valuation Range:** **$43.15 to $139.96 per share** across causal macroeconomic scenarios.
- **Severe Downside Stress Floor:** **$1.52 per share** under joint global recession + Argentine sovereign shock.
- **Execution Strategy:** Deploy an initial **60% capital tranche at $\le \$66.00$**; reserve 40% dry powder for macro dips.

### 2. Why Valuation Methods Disagree (Do Not Mechanically Average)
- **DCF Intrinsic Value ($88.26):** Captures multi-year cash flow inflection as peak development CapEx ($1.05B in 2026E) transitions into a cash-harvesting plateau ($1.49B FCFF in 2029E, a 20.8% free cash flow yield).
- **Peer Multiples ($47.54 – $50.82):** Dragged down by state-controlled, politically subsidized peers (YPF at 3.5x EBITDA) and mature, depleting conventional operators (GeoPark, Gran Tierra). Vista deserves a premium for pure-play Vaca Muerta shale quality and lowest-quartile $4.50/boe lifting costs.

### 3. Market-Implied Reverse-DCF
At $65.00/share, the market prices:
- A perpetual realized oil price of **$54.54/boe** (equivalent to sub-$60 Brent).
- OR an implied cost of capital of **15.47%** (pricing an exorbitant ~800 bps sovereign penalty).

---

## Formal Validation Suite (100% Passed)

| Validation Test | Target Assertion | Result |
|---|---|:---:|
| **Synthetic Known-Answer DCF** | Closed-form analytical formula reconciliation ($103.9255/sh) | **PASS (Diff: 0.000000)** |
| **Independent Source Definition** | Form 20-F Item 5 lifting cost ($4.80/boe) reconciliation | **PASS (Audited)** |
| **Directional Monotonicity Suite** | Expected monotonic movement across WACC, growth, volume, and costs | **PASS (All Passed)** |
| **Locked Changed-Input Record** | Pre-commit AI-off prediction (+14 to +16 VPS on +$5/boe price shift) | **PASS (Actual: +$14.07)** |
| **Pro-Forma Loud Articulation** | Balance sheet gap = $0.0000 every year; cash ties to cash flow | **PASS (Gap: $0.0000)** |
| **Highest-Risk Failure Test** | Graceful handling of $35/bbl oil collapse and covenant strain | **PASS (Zero Crash)** |

---

