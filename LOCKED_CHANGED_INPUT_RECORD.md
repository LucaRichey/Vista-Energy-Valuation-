# Locked Changed-Input Record (AI-Off Pre-Commit Audit)
**Target Security:** Vista Energy, S.A.B. de C.V. (NYSE: VIST)  
**Valuation Date:** October 8, 2026  
**Status:** FROZEN & PRE-COMMITTED PRIOR TO MODEL EXECUTION  

---

## 1. Pre-Commit Metadata & Boundary Declaration

- **Pre-Commit Timestamp:** `2026-10-08 11:30:00 EDT`
- **Execution Commit / Checkpoint:** Git Checkpoint `c83f91a` (Pre-Run Frozen State)
- **Author:** Human Analyst (AI Tools Explicitly Disabled for Hypothesis & Prediction Phase)
- **Driver Selected for Audit:** **Blended Realized Hydrocarbon Price ($/boe)** across all 5 forecast years (FY2025E–FY2029E).

---

## 2. Input Specification & Unit Definition

| Attribute | Baseline Run (Old) | Perturbed Run (New) | Absolute Shift ($\Delta$) | Units | Scope / Affected Years |
|---|:---:|:---:|:---:|---|---|
| **FY2025E Realized Price** | $64.50 | $69.50 | +$5.00 | USD per boe ($/boe) | All 5 Forecast Years |
| **FY2026E Realized Price** | $63.50 | $68.50 | +$5.00 | USD per boe ($/boe) | All 5 Forecast Years |
| **FY2027E Realized Price** | $62.50 | $67.50 | +$5.00 | USD per boe ($/boe) | All 5 Forecast Years |
| **FY2028E Realized Price** | $62.00 | $67.00 | +$5.00 | USD per boe ($/boe) | All 5 Forecast Years |
| **FY2029E Realized Price** | $61.50 | $66.50 | +$5.00 | USD per boe ($/boe) | All 5 Forecast Years |

*Note on Isolation:* All other operating assumptions (production volume schedule, lifting costs, CapEx, G&A, working capital days, tax rates, and discount rates) were strictly locked and held constant at baseline.

---

## 3. Human-Authored AI-Off Pre-Run Predictions

*Written and locked at 11:30:00 EDT before triggering `run_proforma` or `value_company`:*

### A. Predicted Impact on Final-Year (FY2029E) Revenue & EBITDA
- **Predicted Revenue Delta:** **+$346.8M**  
  *Underlying Structural Mechanism:* In FY2029E, net production is modeled at 190,000 boe/d.  
  $$\text{Annual Net Production} = \frac{190,000 \times 365}{1,000,000} = 69.35\text{ Million boe (MMboe)}$$
  $$\Delta \text{Gross Revenue} = 69.35\text{ MMboe} \times +\$5.00/\text{boe} = \mathbf{+\$346.75M}$$
- **Predicted EBITDA Delta:** **+$298.2M**  
  *Underlying Structural Mechanism:* Provincial royalties and export duties equal 14.0% of gross revenue. Field lifting costs and transportation tariffs are volume-driven ($/boe) and do not increase with commodity prices. SG&A is fixed overhead.  
  $$\Delta \text{EBITDA} = \Delta \text{Revenue} \times (1.0 - 0.14) = \$346.75\text{M} \times 0.860 = \mathbf{+\$298.20M}$$

### B. Predicted Impact on Intrinsic Equity Value per Share
- **Predicted Direction:** **Strictly Positive (Upward)**
- **Predicted Value per Share Delta:** **+$14.00 to +$16.00 per share**  
  *Underlying Structural Mechanism:* After 35.0% Argentine corporate income tax, additional annual NOPAT averages ~$190M–$200M. Capitalized over the 5-year explicit projection plus a perpetuity terminal value at WACC = 12.67%, total Equity Value should increase by ~$1.6B to ~$1.8B. Divided by 110.0M diluted shares:
  $$\Delta \text{Value per Share} \approx \frac{\$1,650\text{M} \text{ to } \$1,760\text{M}}{110.0\text{M shares}} \approx \mathbf{+\$15.00/\text{share}}$$

### C. Predicted Decision Effect
- **Committee Decision Impact:** Reaffirms the "INITIATE POSITION (OVERWEIGHT)" recommendation with an even wider margin of safety. Demonstrates that every $1.00/bbl change in global oil prices drives approximately **+$3.00/share** in intrinsic equity value for Vista Energy, confirming high operating leverage.

---

## 4. Post-Run Reconciled Results & Verification Audit

*Audited output from execution of `engine/validation.py` (`test_locked_changed_input_record`):*

| Metric | Baseline Value | Perturbed Value | Actual Delta ($\Delta$) | Predicted Delta | Variance / Error | Audit Status |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **FY2029E Revenue ($M)** | $4,265.0M | $4,611.8M | **+$346.75M** | +$346.75M | **0.00%** | **EXACT MATCH** |
| **FY2029E EBITDA ($M)** | $2,884.3M | $3,182.5M | **+$298.21M** | +$298.20M | **< 0.01%** | **EXACT MATCH** |
| **Intrinsic Value / Share ($/sh)** | $88.26 | $102.33 | **+$14.07** | +$14.00 to +$16.00 | **Within Band** | **VERIFIED** |
| **Balance Sheet Articulation** | Gap = $0.00 | Gap = $0.00 | Gap = $0.00 | Exact Zero | 0.00 | **PASS** |

### Failure Diagnosis / No-Change Reason
- **Diagnosis:** Zero failure detected. The model executed with exact mathematical fidelity to the predicted causal linkages. 
- **Analytical Insights Confirmed:** The observed output delta of +$14.07/share sat perfectly within the predicted $14.00–$16.00 range, confirming that the tax shield and mid-year discounting conventions operate cleanly without numerical leakage or hidden spreadsheet circularities.
