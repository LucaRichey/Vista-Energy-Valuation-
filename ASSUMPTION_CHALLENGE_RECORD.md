# Assumption Challenge Record & Lab Partner Fresh-Eyes Challenges
**Target Company:** Vista Energy, S.A.B. de C.V. (NYSE: VIST)  
**Valuation Date:** October 8, 2026  
**Format:** Value · Basis · Challenge · Evidence That Would Change It  

---

## 1. Load-Bearing Operating Driver Challenge Records

### Driver 1: Net Daily Hydrocarbon Production (boe/d)
- **Value:** Ramps from 105,000 boe/d in FY2025E to 140,000 boe/d in FY2026E, plateauing at 190,000 boe/d in FY2029E.
- **Basis:** Geological inventory in Bajada del Palo Oeste, Aguada Federal, and newly integrated PEPASA acreage supporting 50–65 new well tie-ins annually; supported by Oldelval pipeline expansion (Proyecto Duplicar) adding 315k bbl/d takeaway capacity by mid-2025.
- **Challenge:** Assumes zero logistical or hydraulic fracturing sand/water bottlenecks, flawless execution by drilling contractors (Nabors, Helmerich & Payne), and timely pipeline commissioning without Argentine regulatory intervention.
- **Evidence That Would Change It:** 
  1. A reported quarterly evacuation curtailment or pipeline commissioning delay exceeding 90 days.
  2. Sub-commercial initial production rates (IP30 < 1,500 boe/d) in step-out delineation wells in Aguada Federal.
  3. Shortages of high-spec drilling rigs or frac fleets in the Neuquén Basin.

### Driver 2: Blended Realized Hydrocarbon Price ($/boe)
- **Value:** $64.50/boe in FY2025E, gently normalizing down to $61.50/boe by FY2029E.
- **Basis:** Grounded in a base Brent crude curve of $75.00–$70.00/bbl, an ~85% crude oil / 15% natural gas production mix, with oil realizing at Brent minus a $4.50–$5.50/bbl quality and transportation netback discount.
- **Challenge:** Global crude oil demand could weaken under accelerated OECD EV adoption and Chinese economic deceleration; alternatively, Argentine domestic refiners could lobby for a return of the "barril criollo" artificial domestic price cap.
- **Evidence That Would Change It:**
  1. Brent crude breaking below $60.00/bbl for more than two consecutive quarters on global macroeconomic weakness.
  2. Reintroduction of federal administrative price freezes on domestic fuel pump prices by the Argentine Energy Secretariat.
  3. Escalation in export retention withholdings above the current 8% statutory ceiling.

### Driver 3: Direct Lifting Cost ($/boe)
- **Value:** $4.65/boe in FY2025E, declining to $4.40/boe by FY2029E.
- **Basis:** Vista is historically the undisputed low-cost operator in Vaca Muerta ($4.80/boe in FY2024); operational scale across multi-well pads (up to 4 wells per pad) and centralized water gathering systems reduces per-barrel variable costs.
- **Challenge:** Argentine domestic oilfield service (OFS) labor unions (Sindicato de Petróleo y Gas Privado) regularly demand inflation-indexed wage increases exceeding 100% in local currency terms, threatening dollar-denominated cost inflation if the Argentine peso exchange rate lags domestic inflation (real FX appreciation).
- **Evidence That Would Change It:**
  1. Persistent local currency overvaluation causing dollar lifting costs to exceed $5.25/boe in consecutive quarterly earnings.
  2. Water handling or disposal capacity limits requiring high-cost trucking rather than piped transport.

### Driver 4: Development Capital Expenditures (CapEx)
- **Value:** $950M in FY2025E, peaking at $1,050M in FY2026E, before tapering to a maintenance level of $700M in FY2029E.
- **Basis:** Reflects drilling and completion (D&C) costs of ~$13.5M per 2,800m lateral horizontal well across 55–65 wells annually, plus $100M–$150M in central processing facilities (CPF) and gathering pipelines.
- **Challenge:** Unconventional shale wells exhibit rapid initial decline rates (~65-70% in Year 1). If EURs deteriorate, sustaining 190k boe/d could require 80+ wells annually, permanently elevating maintenance CapEx above $1.0B/year.
- **Evidence That Would Change It:**
  1. Average D&C cost per well inflating above $15.0M due to steel casing or tubular price surges.
  2. Observed decline curve steepening in mature pads forcing management to elevate annual rig counts.

### Driver 5: Cost of Capital (WACC) & Country Risk Premium (CRP)
- **Value:** Blended WACC of 12.67% (Cost of Equity = 14.50%, After-Tax Debt = 5.36%, Target Debt = 20%).
- **Basis:** $R_f = 4.25\%$, $\beta = 1.25$, $\text{ERP} = 5.0\%$, plus a normalized Country Risk Premium (CRP) of 4.00% (400 bps), recognizing that Vista's offshore dollar escrow accounts mitigate pure Argentine sovereign default risk.
- **Challenge:** Sovereign bond spreads (EMBI+ Argentina) have historically exceeded 1,200 bps during political transitions. Applying only 400 bps could understate transfer and convertibility risk if radical political shifts re-impose capital controls.
- **Evidence That Would Change It:**
  1. Congressional repeal of Decree 929 / RIGI foreign exchange protections.
  2. Central Bank of Argentina (BCRA) blocking cross-border dollar debt servicing for private corporate issuers.
  3. Corporate bond yields on Vista's 2029/2032 Senior Notes spiking above 11.5% in secondary trading.

---

## 2. Lab Partner Fresh-Eyes Challenges (Weeks 5–6 Collaborative Audit)

### Fresh-Eyes Challenge 1 — Working Capital & CapEx Articulation
- **Challenger:** Embedded Lab Partner (Lead Analyst, Industrial & Asset-Intensive Track)
- **Partner's Challenge:** 
  > *"In your cash flow statement, CapEx is modeled at $1.05B in FY26, but how do trade payables handle drilling contractors? In heavy drilling cycles, E&P companies stretch supplier payables, temporarily boosting operating cash flow at the expense of working capital liquidity."*
- **Model Revision & Defense:** 
  * I revised the Days Payable Outstanding (DPO) driver to explicitly link accounts payable to total cash operating outlays **plus** CapEx: `total_purchases = cash_field_costs + sga + capex`. 
  * With DPO set conservatively at 65 days, trade payables naturally expand during peak drilling and contract when CapEx scales down in FY28–29, ensuring full articulation without unbacked liquidity windfalls.
- **Outcome:** Validated and incorporated into `engine/model.py`.

### Fresh-Eyes Challenge 2 — Terminal Growth vs. Geologic Reserve Exhaustion
- **Challenger:** Embedded Lab Partner (Lead Analyst, Energy & Resources Track)
- **Partner's Challenge:** 
  > *"You are using a 2.0% perpetual growth rate in your DCF terminal value. Can an oil and gas company legitimately grow in perpetuity, given physical subsurface depletion and global energy transition decarbonization mandates?"*
- **Model Revision & Defense:**
  * I cross-checked Vista's certified 2P reserves (exceeding 350M boe) against our 5-year cumulative production (~280M boe), plus unbooked contingent resources across its 200,000+ net core acres. Vaca Muerta has over 20–25 years of drilling inventory at 60 wells/year.
  * To address the decarbonization challenge, I added a secondary **Exit Multiple Cross-Check** (5.0x EV/EBITDA), which discounts cash flow to a terminal multiple without requiring infinite growth. The perpetuity DCF ($88.26/sh) and the exit multiple check ($88.85/sh) converged within 1%, demonstrating that a 2.0% perpetuity assumption is economically equivalent to a modest 5x terminal multiple.
- **Outcome:** Retained with explicit exit-multiple triangulation.

### Fresh-Eyes Challenge 3 — Downside Case Plausibility & Recommendation Inversion
- **Challenger:** Senior Sector Reviewer / Fresh-Eyes Auditor
- **Partner's Challenge:** 
  > *"Your initial downside test only lowered Brent by $5/bbl. In commodity markets, real downside shocks involve joint distributions: Brent dropping to $50, pipeline bottlenecks, and government tax hikes all occurring simultaneously. Show me a case that actually breaks the buy thesis."*
- **Model Revision & Defense:**
  * I built the named **"Severe Downside Stress Case"** (`Downside_Stress` in `engine/scenarios.py`), which joint-stresses:
    1. Realized prices down to $45/boe.
    2. Evacuation capped at 125k boe/d (18-month takeaway stall).
    3. Export withholding taxes hiked to 8% (total tax 20%).
    4. Lifting costs rising to $5.50/boe.
    5. WACC spiking to 14.96%.
  * Under this stress case, intrinsic share value collapses to **$1.52/share**, proving that the model captures real solvency and equity wipeout risk under catastrophic conditions.
- **Outcome:** Fully implemented and highlighted in the Investment Committee Memo as the basis for the mandatory Reversal Triggers.
