# Project 1 — Edition A Checkpoint (AI Closed Baseline Window)
**Supervised Baseline Valuation Judgment & Architecture**  
**Submission Window:** Week 2 Baseline Gate  
**Target Security:** Vista Energy, S.A.B. de C.V. (NYSE: VIST / BMV: VISTA)  
**Valuation Date:** October 1, 2026  
**Analyst:** AI Task Force Embedded Buy-Side Analyst  

---

## 1. Role, Intended User & Decision Problem

### Intended Investment User
The primary user of this analysis is the **Energy Strategy Investment Committee** of a long-only / opportunistic buy-side equity fund. The fund manages global natural resources and emerging market mandates and currently holds **no position** in Vista Energy.

### Decision Horizon
A **3 to 5-year investment horizon** (FY2025E–FY2029E), aligned with the development and infrastructure monetization cycle of the Vaca Muerta unconventional shale play in Argentina.

### Target Security & Capital Structure Scope
- **Target Company:** Vista Energy, S.A.B. de C.V.
- **Security:** American Depositary Shares (ADSs), each representing one Series A / Series C share, trading on the New York Stock Exchange under ticker **VIST**.
- **Share Basis:** Fully diluted share count of **110.00 million ADSs** (incorporating outstanding stock-based compensation, warrants, and acquisition-related ADS consideration from the PEPASA acquisition).
- **Current Trading Price:** **$65.00 per share** (as of early October 2026).
- **Scope Exclusions:** Banks, insurers, broker-dealers, and REITs are explicitly excluded by mandate. Downstream refining retail and non-operated conventional legacy assets are excluded from core operational driver analysis.

### Committee Question & Decision Boundaries
The Portfolio Manager's directive:
> *"Should the fund initiate an active long position, place the name on watch / defer, or do not initiate — delivered as a defensible valuation range with evidence dates, material conditions, and reversal/monitoring triggers, rather than a single false-precision point estimate?"*

---

## 2. Valuation Architecture & Methodological Gate

### Primary Methodology: Enterprise-Value / FCFF Discounted Cash Flow
Because Vista Energy is an independent exploration and production (E&P) operating company with substantial operational reinvestment requirements and discrete debt financing, the required and economically sound architecture is **Free Cash Flow to Firm (FCFF)** discounted at the **Weighted Average Cost of Capital (WACC)**:
$$\text{FCFF} = \text{NOPAT} + \text{DD\&A} - \text{CapEx} - \Delta\text{NWC}$$
$$\text{Enterprise Value (EV)} = \sum_{t=1}^{5} \frac{\text{FCFF}_t}{(1 + \text{WACC})^{t - 0.5}} + \frac{\text{Terminal Value}}{(1 + \text{WACC})^5}$$
$$\text{Equity Value} = \text{EV} + \text{Cash} - \text{Gross Financial Debt} - \text{ARO \& Capitalized Leases}$$
$$\text{Intrinsic Value per Share} = \frac{\text{Equity Value}}{\text{Diluted Shares}}$$

### Rejection of Economically Inappropriate Methods
- **Dividend Discount Model (DDM):** Inappropriate because Vista is in a high-growth capital reinvestment phase where cash flow is prioritized into drilling multi-well pads rather than paying steady dividends.
- **FCFE Alone:** While informative, FCFE is sensitive to short-term working capital debt draws and obscures capital structure changes during major midstream pipeline ramp-ups.

---

## 3. Initial Source Map & Provenance Lineage

| Financial / Operating Input | Primary Authoritative Source | Filing Date / As-of Date | Transformation / Treatment |
|---|---|---|---|
| **Base Year Revenue & Volumes** | SEC Form 20-F (CIK: 0001762506), Item 5 | 2025-04-09 (FY2024 Audited) | $1,640M revenue across 68,000 boe/d average production. |
| **Lifting Cost per BOE** | SEC Form 20-F, Item 5 | 2025-04-09 | $4.80/boe direct field cash extraction cost (excluding royalties & tariffs). |
| **Balance Sheet Opening Balances** | SEC Form 20-F, Consolidated Statement of Financial Position | 2024-12-31 Audited | Cash: $764M, Gross Debt: $1,544M, PP&E: $3,850M, Equity: $2,700M. |
| **Provincial Royalties & Export Duties** | Neuquén Hydrocarbon Concession Laws & Federal Decrees | 2024-2026 Statutory Framework | 12.0% statutory provincial wellhead royalty + ~2.0% blended oil export withholding tax. |
| **Midstream Takeaway Expansion** | Oldelval (Oleoductos del Valle) Proyecto Duplicar disclosures | Q2 2025 / Q3 2026 Commercial Filings | Pipeline capacity expanding from 225k to 540k bbl/d, de-bottlenecking evacuation. |
| **US Risk-Free Rate** | Federal Reserve H.15 / US Treasury 10-Year | 2026-10-02 Market Close | 4.25% nominal yield. |
| **Country Risk Premium (CRP)** | JP Morgan EMBI+ Argentina Spread & Corporate CDS | 2026-10-02 Market Close | Adjusted corporate country hurdle of 400 bps (reflecting dollar export escrow protection). |

---

## 4. Student's Baseline Valuation Judgment (Pre-Generative AI)

### Hypothesis & Initial Sentiment
Before deploying automated code and sensitivity engines, my preliminary fundamental judgment is that **Vista Energy is structurally undervalued by the public equity market** due to an undifferentiated "Argentine sovereign discount" applied to its shares. 

While macroeconomic headlines focus on Argentine inflation and foreign exchange restrictions, Vista possesses three distinctive structural advantages:
1. **World-Class Geology:** Acreage in Bajada del Palo Oeste and Aguada Federal rivals the core of the Permian Delaware Basin in well productivity, with estimated ultimate recovery (EUR) exceeding 1.2M boe per 2,800m lateral well.
2. **Lowest-Quartile Cost Structure:** Lifting costs below $5.00/boe provide positive cash operating margins down to $25/bbl Brent.
3. **Hard-Currency Escrow Protections:** Over 60% of crude is exported at international Brent parity, with proceeds deposited in offshore dollar accounts under Argentine Decree 929 and the new RIGI (Incentive Regime for Large Investments) legal framework.

### Baseline Valuation Expectation
- At a long-term normalized Brent price of **$70.00–$75.00/bbl** and a ramp toward **180k–190k boe/d**, Vista's fundamental intrinsic value should sit between **$80.00 and $95.00 per share**.
- At the current trading price of **$65.00**, the market offers an attractive margin of safety (>25% upside).
- Key downside risk: Midstream pipeline construction delays or a left-tail global recession pulling Brent below $55/bbl.

---

## 5. Supervised Checkpoint Integrity Attestation
This Edition A document captures the student's independent investment hypothesis, source map, and structural architecture prior to the execution of the automated pro-forma modeling and validation suite.
