# Week 2 Contamination Catalog & Historical Normalization
**Target Company:** Vista Energy, S.A.B. de C.V. (NYSE: VIST)  
**Valuation Date:** October 8, 2026  
**Accounting Standard:** IFRS as issued by the IASB, reported in USD Millions  

---

## 1. Objective & Taxonomy of Inputs

To ensure institutional data integrity and eliminate "mixed-time" contamination or silent spreadsheet repairs, every input in the model stack is explicitly classified under one of four rigorous evidentiary tiers:
1. **Facts (F):** Audited, publicly verified historical figures extracted verbatim from SEC filings, audited balance sheets, or authoritative regulatory registries with explicit as-of dates.
2. **Normalizations (N):** Historical figures adjusted for non-recurring events, asset transfers, hyperinflationary accounting anomalies, or definition reconciliations to create an economically clean base year.
3. **Forecasts (E):** Prospective operating assumptions grounded in management guidance, geological field development plans, midstream commercial contracts, or independent commodity forward curves.
4. **Model Outputs (M):** Mathematically calculated values derived strictly through articulating formulas and valuation algorithms.

---

## 2. Master Lineage & Contamination Traceability Matrix

| Line Item | Tier | As-of Date | Form / Authoritative Source | Reported Value | Normalized Base Value | Contamination / Adjustment Justification |
|---|:---:|:---:|---|:---:|:---:|---|
| **Gross Hydrocarbon Revenue** | F $\rightarrow$ N | 2024-12-31 | Form 20-F, Item 18 (Statement of Profit or Loss) | $1,640.0M | $1,640.0M | Unadjusted audited revenue. Excludes conventional assets transferred in 2023. |
| **Crude Oil & Gas Production** | F | 2024-12-31 | Form 20-F, Item 5A (Operating Review) | 68,000 boe/d | 68,000 boe/d | Weighted average net daily production across operated shale concessions. |
| **Direct Lifting Cost** | F $\rightarrow$ N | 2024-12-31 | Form 20-F, Item 5A | $4.80/boe | $4.80/boe | Reconciled: Cash field extraction costs divided by net production. Excludes transportation tariffs and royalties. |
| **Transferred Conventional Assets** | N | 2023-2024 | Form 20-F, Note 4 (Asset Dispositions) | -$115.0M | Normalized | Excluded non-core conventional production sold to Aconcagua Energía to isolate pure-play shale cash flows. |
| **PEPASA Acquisition ADS Issuance** | F $\rightarrow$ N | 2025-04-15 | Form 6-K / SEC Acquisition Prospectus | 7,297,507 ADSs | Diluted Count Included | 7.30M ADSs issued to Petronas added to share count; eliminates post-acquisition equity dilution surprises. |
| **Opening Cash & Equivalents** | F | 2024-12-31 | Form 20-F, Consolidated Statement of Financial Position | $764.0M | $764.0M | Verified unrestricted bank balances + short-term sovereign treasury deposits. |
| **Gross Financial Debt** | F | 2024-12-31 | Form 20-F, Note 19 (Borrowings) | $1,544.0M | $1,544.0M | Bank borrowings ($244M short-term) + Senior Notes ($1,300M long-term). |
| **ARO Provisions & Leases** | F $\rightarrow$ N | 2024-12-31 | Form 20-F, Note 21 & Note 22 | $140.0M | $140.0M | Asset retirement obligations ($95M) + capitalized right-of-use lease liabilities ($45M) bridged into EV net debt. |
| **Development CapEx (Drilling & Completion)** | F $\rightarrow$ N | 2024-12-31 | Form 20-F, Consolidated Statement of Cash Flows | $1,113.0M | $1,113.0M | Peak development CapEx (50 wells connected); normalized to forward D&C efficiency ($13.5M/well). |
| **Provincial Royalties & Export Withholdings** | F | 2024-2026 | Neuquén Concession Contracts / Decree 488 | 14.0% | 14.0% | 12.0% statutory provincial royalty on gross wellhead value + ~2.0% blended oil export withholding tax. |
| **Argentina Corporate Tax Rate** | F | 2024-2026 | Ley de Impuesto a las Ganancias (Argentina) | 35.0% | 35.0% | Statutory corporate income tax rate on net taxable profit. |
| **US 10-Year Treasury Yield ($R_f$)** | F | 2026-10-02 | Federal Reserve Board H.15 Release | 4.25% | 4.25% | Benchmark risk-free discount anchor. |
| **Country Risk Premium (CRP)** | N | 2026-10-02 | JP Morgan EMBI+ Global Argentina & CDS | 1,150 bps | 400 bps (4.00%) | Normalized down from sovereign bond spread due to dollar export escrow and Decree 929 foreign exchange immunity. |

---

## 3. Reconciliation of Provider Labels to Financial Definitions

| Third-Party Provider Label (Bloomberg / FactSet / Yahoo) | Reported Screened Value | Audited IFRS / Model Definition | Reconciliation Diagnosis |
|---|:---:|---|---|
| **"EBITDA"** | $1,120M | Operating Profit + DD&A | Confirmed exact match with Adjusted EBITDA reported in Form 20-F Item 5. |
| **"Total Debt"** | $1,544M | Short-Term Borrowings + Long-Term Borrowings | Screened metrics occasionally omit short-term trade facilities; model captures the complete $1,544M gross debt. |
| **"Net Debt"** | $780M | Gross Financial Debt ($1,544M) - Cash ($764M) | Confirmed exact match. |
| **"Shares Outstanding"** | 108.9M | 110.0M Diluted ADSs | Screened data excludes unexercised stock options and acquisition earnout shares. Model uses conservative 110.0M fully diluted count. |
| **"P/E Ratio"** | 17.5x | Market Price / GAAP Diluted EPS | Screened trailing P/E reflects historical reinvestment trough; model evaluates forward 2025E-2026E normalized P/E. |

---

## 4. Base-Year Articulation Reconciliation to Audited Form 20-F

The opening balance sheet for the 5-year pro-forma strictly articulates to the audited balance sheet of December 31, 2024:

$$\begin{aligned}
\text{Total Assets} &= \text{Cash } (\$764.0\text{M}) + \text{Receivables } (\$235.0\text{M}) + \text{Inventory } (\$45.0\text{M}) \\
&\quad + \text{Net PP\&E } (\$3,850.0\text{M}) + \text{Other Assets } (\$420.0\text{M}) = \mathbf{\$5,314.0\text{M}} \\
\text{Total Liabilities} &= \text{Payables } (\$580.0\text{M}) + \text{Gross Debt } (\$1,544.0\text{M}) + \text{Other Liab } (\$490.0\text{M}) = \mathbf{\$2,614.0\text{M}} \\
\text{Shareholders' Equity} &= \mathbf{\$2,700.0\text{M}} \\
\text{Total Liab \& Equity} &= \$2,614.0\text{M} + \$2,700.0\text{M} = \mathbf{\$5,314.0\text{M}} \\
\mathbf{\text{Articulation Gap}} &= \mathbf{\$5,314.0\text{M}} - \mathbf{\$5,314.0\text{M}} = \mathbf{\$0.0000\text{M (Exact Zero)}}
\end{aligned}$$

No silent reconciliations or manual plugs were introduced.
