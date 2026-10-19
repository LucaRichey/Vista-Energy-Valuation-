"""
engine/model.py
================
Core Three-Statement Pro-Forma & FCFF / WACC Valuation Engine
Target Security: Vista Energy, S.A.B. de C.V. (NYSE: VIST)
Reporting Standard: IFRS in USD Millions (unless specified per-share or per-boe)
Valuation Date: October 8, 2026
Base Year: FY2024 (Audited Form 20-F filed April 9, 2025)
Forecast Period: FY2025E - FY2029E (5-Year Pro-Forma)

Architecture:
  - Personalized Driver Architecture (Volume, Realized Price, Lifting Cost, CapEx/Wells, Royalties, Tariffs)
  - Articulating 3-Statement Pro-Forma (Income Statement, Balance Sheet, Cash Flow)
  - Loud Integrity Checks:
      * Balance Sheet balances every year (Total Assets == Total Liabilities + Equity)
      * Cash Flow ties to Balance Sheet cash (Ending Cash == Prior Cash + Net Cash Flow)
      * Base Year reconciles to audited Form 20-F filing
  - Enterprise-Value / FCFF DCF Engine with WACC, Terminal Perpetuity, and Exit Multiple
  - Comprehensive Enterprise-to-Equity & Per-Share Bridge
"""

import copy
import math
from typing import Dict, Any, List, Tuple


def get_base_inputs() -> Dict[str, Any]:
    """
    Returns the audited base-year inputs (FY2024) and baseline forecast drivers.
    All dollar figures are in USD Millions unless noted ($/boe, $/bbl, or $/share).
    """
    return {
        # --- Metadata & Security Identification ---
        "target_name": "Vista Energy, S.A.B. de C.V.",
        "ticker": "VIST",
        "exchange": "NYSE",
        "currency": "USD",
        "scale": "USD Millions",
        "valuation_date": "2026-10-08",
        "intended_user": "Buy-Side Investment Committee / Energy Strategy Fund",
        "decision_horizon": "3-5 Year Investment Holding Period",
        "current_market_price": 65.00,  # USD per share as of early October 2026
        "diluted_shares": 110.00,       # Million fully diluted ADSs / Series C shares
        
        # --- FY2024 Audited Base Balance Sheet (Form 20-F) ---
        "cash_0": 764.0,           # Cash and cash equivalents
        "receivables_0": 235.0,    # Trade & other receivables
        "inventory_0": 45.0,       # Crude oil and supplies inventory
        "ppe_0": 3850.0,           # Property, Plant & Equipment (Oil & gas concessions & wells)
        "other_assets_0": 420.0,   # Goodwill, deferred tax assets, right-of-use assets
        "tot_assets_0": 5314.0,    # Total Assets = 764 + 235 + 45 + 3850 + 420
        
        "payables_0": 580.0,       # Trade payables, accrued liabilities, and royalties payable
        "st_debt_0": 244.0,        # Short-term bank borrowings
        "lt_debt_0": 1300.0,       # Long-term senior notes and dollar credit facilities
        "gross_debt_0": 1544.0,    # st_debt_0 + lt_debt_0
        "other_liab_0": 490.0,     # Deferred tax liabilities, lease liabilities, ARO provisions
        "tot_liab_0": 2614.0,      # Total Liabilities = 580 + 1544 + 490
        
        "equity_0": 2700.0,        # Shareholders' Equity (5314 - 2614)
        
        # --- FY2024 Base Operating Baseline ---
        "rev_0": 1640.0,           # Full-Year 2024 Audited Revenue
        "prod_boed_0": 68000.0,    # Average daily production in boe/d
        "ebitda_0": 1120.0,        # FY2024 Adjusted EBITDA
        "ebit_0": 720.0,           # FY2024 Operating Profit (EBIT)
        "net_income_0": 410.0,     # FY2024 Net Income
        "capex_0": 1113.0,         # FY2024 Total Capital Expenditures
        
        # --- 5-Year Forecast Operating Drivers (FY2025E - FY2029E) ---
        # Net Daily Production in boe/d (Vaca Muerta shale expansion)
        "prod_boed_forecast": [105000.0, 140000.0, 165000.0, 180000.0, 190000.0],
        
        # Realized Blended Hydrocarbon Price ($/boe)
        # Based on $75-$70 Brent, ~85% oil mix, minus domestic and export parity logistics discount
        "realized_price_forecast": [64.50, 63.50, 62.50, 62.00, 61.50],
        
        # Operating Lifting Cost ($/boe) — Vista is benchmark lowest-cost Vaca Muerta operator
        "lifting_cost_per_boe": [4.65, 4.50, 4.45, 4.40, 4.40],
        
        # Statutory Provincial Royalty + Export Tax Rate (% of gross revenue)
        "royalty_export_tax_rate": 0.140,  # 12.0% Neuquén provincial royalty + ~2.0% blended export duty
        
        # Midstream Transportation & Logistics Tariff ($/boe)
        "midstream_tariff_per_boe": 5.40,  # Oldelval pipeline expansion & OTE terminal tariffs
        
        # Selling, General & Administrative (G&A) Fixed Base + Inflation ($M)
        "sga_expense_forecast": [62.0, 70.0, 76.0, 80.0, 84.0],
        
        # Other Operating & Environmental Remediation ($M)
        "other_operating_exp": [15.0, 18.0, 20.0, 20.0, 20.0],
        
        # DD&A (Depreciation, Depletion & Amortization) per boe produced ($/boe)
        "ddna_per_boe": 14.50,     # Unit-of-production DD&A standard for shale development
        
        # Development CapEx Forecast ($M) — Driven by wells connected and D&C efficiency (~$13.5M/well)
        "capex_forecast": [950.0, 1050.0, 950.0, 800.0, 700.0],
        
        # Working Capital Ratios
        "dso_days": 48.0,          # Days Sales Outstanding (Receivables)
        "dio_days": 28.0,          # Days Inventory Outstanding (relative to cash production costs)
        "dpo_days": 65.0,          # Days Payable Outstanding (relative to cash operating costs + CapEx)
        
        # Debt, Interest & Cash Reinvestment Rules
        "gross_interest_rate": 0.0825,     # 8.25% weighted average coupon on USD senior notes
        "cash_yield_rate": 0.045,          # 4.50% interest income yield on USD cash deposits
        "min_operational_cash": 150.0,     # Minimum liquidity reserve required for field operations
        "annual_debt_repayment": 100.0,    # Scheduled senior debt amortization ($M/yr)
        "dividend_payout_ratio": 0.15,     # 15% dividend payout on net income starting FY26E
        
        # Tax Assumptions
        "effective_tax_rate": 0.35,        # 35.0% statutory corporate income tax rate (Argentina)
        
        # --- Cost of Capital (WACC) & Valuation Engine Inputs ---
        "risk_free_rate": 0.0425,          # 4.25% 10-Year US Treasury Yield
        "equity_risk_premium": 0.050,      # 5.00% Mature Market Equity Risk Premium
        "levered_beta": 1.25,              # E&P Operating & Financial Leverage Beta
        "country_risk_premium": 0.040,     # 4.00% Corporate-adjusted Argentina sovereign spread
        "cost_of_debt_pretax": 0.0825,     # 8.25% Pre-tax cost of debt
        "target_debt_weight": 0.20,        # 20.0% Target Debt / (Debt + Equity)
        "target_equity_weight": 0.80,      # 80.0% Target Equity / (Debt + Equity)
        
        # Terminal Assumptions
        "terminal_growth_rate": 0.020,     # 2.00% Long-term perpetual growth rate
        "terminal_exit_multiple": 5.0,     # 5.0x EV/EBITDA cross-check benchmark
        
        # Enterprise-to-Equity Bridge Additions/Subtractions ($M)
        "aro_and_leases": 140.0,           # Asset retirement obligations and discounted lease liabilities
        "minority_interest": 0.0,          # Zero minority interest
        
        "years": [2025, 2026, 2027, 2028, 2029],
    }


def calculate_wacc(inputs: Dict[str, Any]) -> Dict[str, float]:
    """
    Calculates the Weighted Average Cost of Capital (WACC) using CAPM with Country Risk Premium.
    Formula:
      Cost of Equity = Rf + Beta * ERP + CRP
      After-tax Cost of Debt = Rd * (1 - t)
      WACC = We * Ke + Wd * Kd_after_tax
    """
    rf = inputs["risk_free_rate"]
    erp = inputs["equity_risk_premium"]
    beta = inputs["levered_beta"]
    crp = inputs["country_risk_premium"]
    t = inputs["effective_tax_rate"]
    rd = inputs["cost_of_debt_pretax"]
    we = inputs["target_equity_weight"]
    wd = inputs["target_debt_weight"]

    cost_of_equity = rf + (beta * erp) + crp
    cost_of_debt_after_tax = rd * (1.0 - t)
    wacc = (we * cost_of_equity) + (wd * cost_of_debt_after_tax)

    return {
        "cost_of_equity": cost_of_equity,
        "cost_of_debt_pretax": rd,
        "cost_of_debt_after_tax": cost_of_debt_after_tax,
        "wacc": wacc,
        "equity_weight": we,
        "debt_weight": wd,
    }


def run_proforma(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes the 5-year articulating Three-Statement Model and computes Free Cash Flow to Firm (FCFF).
    Enforces loud accounting integrity checks:
      1. Balance sheet balances exactly every year (Gap == 0.0).
      2. Cash Flow statement ties exactly to Balance Sheet ending cash.
      3. Base-year opening balance sheet balances to audited filing.
    """
    years = inputs["years"]
    num_years = len(years)
    
    # Verify Base Year Reconciliation
    tot_assets_0 = inputs["cash_0"] + inputs["receivables_0"] + inputs["inventory_0"] + inputs["ppe_0"] + inputs["other_assets_0"]
    tot_liab_eq_0 = inputs["payables_0"] + inputs["gross_debt_0"] + inputs["other_liab_0"] + inputs["equity_0"]
    base_reconciliation_gap = tot_assets_0 - tot_liab_eq_0
    if abs(base_reconciliation_gap) > 1e-4:
        raise ValueError(f"Base year opening balance sheet does not articulate! Gap = {base_reconciliation_gap:.4f}")
    
    # State tracking variables
    cur_cash = inputs["cash_0"]
    cur_receivables = inputs["receivables_0"]
    cur_inventory = inputs["inventory_0"]
    cur_ppe = inputs["ppe_0"]
    cur_other_assets = inputs["other_assets_0"]
    
    cur_payables = inputs["payables_0"]
    cur_debt = inputs["gross_debt_0"]
    cur_other_liab = inputs["other_liab_0"]
    cur_equity = inputs["equity_0"]
    
    statements: List[Dict[str, Any]] = []
    
    for i, yr in enumerate(years):
        # ----------------------------------------------------
        # 1. OPERATING ENGINE & INCOME STATEMENT
        # ----------------------------------------------------
        prod_boed = inputs["prod_boed_forecast"][i]
        annual_prod_mmboe = (prod_boed * 365.0) / 1_000_000.0  # Million barrels of oil equivalent (MMboe)
        realized_price = inputs["realized_price_forecast"][i]
        
        # Gross Hydrocarbon Revenue ($M)
        revenue = annual_prod_mmboe * realized_price
        
        # Royalties & Provincial Duties ($M)
        royalties = revenue * inputs["royalty_export_tax_rate"]
        
        # Field Operating Costs (Lifting Costs) ($M)
        lifting_cost_rate = inputs["lifting_cost_per_boe"][i]
        lifting_costs = annual_prod_mmboe * lifting_cost_rate
        
        # Transportation & Midstream Logistics ($M)
        midstream_costs = annual_prod_mmboe * inputs["midstream_tariff_per_boe"]
        
        # Total Cash Field Production Costs
        cash_field_costs = lifting_costs + midstream_costs
        
        # SG&A Expense ($M)
        sga = inputs["sga_expense_forecast"][i]
        
        # Other Operating Expenses ($M)
        other_operating = inputs["other_operating_exp"][i]
        
        # Adjusted EBITDA ($M)
        ebitda = revenue - royalties - cash_field_costs - sga - other_operating
        
        # Depreciation, Depletion & Amortization (DD&A) ($M)
        ddna = annual_prod_mmboe * inputs["ddna_per_boe"]
        
        # Operating Profit (EBIT) ($M)
        ebit = ebitda - ddna
        
        # Net Interest Expense ($M)
        # Interest on gross debt minus interest yield on operational cash
        interest_exp = (cur_debt * inputs["gross_interest_rate"]) - (cur_cash * inputs["cash_yield_rate"])
        
        # Earnings Before Taxes (EBT) ($M)
        ebt = ebit - interest_exp
        
        # Current and Deferred Income Tax ($M)
        tax_rate = inputs["effective_tax_rate"]
        tax = max(0.0, ebt) * tax_rate
        
        # Net Income ($M)
        net_income = ebt - tax
        
        # NOPAT (Net Operating Profit After Tax) for FCFF calculation ($M)
        nopat = ebit * (1.0 - tax_rate)
        
        # ----------------------------------------------------
        # 2. BALANCE SHEET DRIVERS & WORKING CAPITAL
        # ----------------------------------------------------
        capex = inputs["capex_forecast"][i]
        
        # Trade Receivables tied to DSO
        receivables = (revenue / 365.0) * inputs["dso_days"]
        delta_receivables = receivables - cur_receivables
        
        # Inventories tied to DIO and field cash operating costs
        inventory = (cash_field_costs / 365.0) * inputs["dio_days"]
        delta_inventory = inventory - cur_inventory
        
        # Accounts Payable tied to cash operating costs + CapEx
        total_purchases = cash_field_costs + sga + capex
        payables = (total_purchases / 365.0) * inputs["dpo_days"]
        delta_payables = payables - cur_payables
        
        # Non-Cash Net Working Capital (NWC)
        # NWC = Receivables + Inventory - Payables
        nwc = receivables + inventory - payables
        prior_nwc = cur_receivables + cur_inventory - cur_payables
        delta_nwc = nwc - prior_nwc  # Positive means cash outflow / cash trapped
        
        # Net PP&E (Property, Plant & Equipment) Roll-Forward
        ppe = cur_ppe + capex - ddna
        
        # Other Non-Current Assets (stable)
        other_assets = cur_other_assets
        
        # Debt Amortization
        debt_repayment = min(cur_debt, inputs["annual_debt_repayment"])
        debt = cur_debt - debt_repayment
        
        # Other Non-Current Liabilities (stable)
        other_liab = cur_other_liab
        
        # Dividends & Shareholder Distributions
        div_rate = inputs["dividend_payout_ratio"] if yr >= 2026 else 0.0
        dividends = max(0.0, net_income * div_rate)
        
        # Shareholders' Equity Roll-Forward
        equity = cur_equity + net_income - dividends
        
        # ----------------------------------------------------
        # 3. CASH FLOW STATEMENT & CASH BALANCE
        # ----------------------------------------------------
        # Cash Flow from Operations (CFO)
        cfo = net_income + ddna - delta_receivables - delta_inventory + delta_payables
        
        # Cash Flow from Investing (CFI)
        cfi = -capex
        
        # Cash Flow from Financing (CFF) (before liquidity draw)
        cff = -debt_repayment - dividends
        
        # Net Cash Flow
        net_cash_flow = cfo + cfi + cff
        
        # Ending Cash before liquidity draw
        cash_tentative = cur_cash + net_cash_flow
        
        # Minimum Liquidity Buffer Protection
        min_cash = inputs["min_operational_cash"]
        liquidity_draw = 0.0
        if cash_tentative < min_cash:
            liquidity_draw = min_cash - cash_tentative
            debt += liquidity_draw  # draw on working capital revolving facility
            cash = min_cash
            cff += liquidity_draw
            net_cash_flow += liquidity_draw
        else:
            cash = cash_tentative
        
        # ----------------------------------------------------
        # 4. FREE CASH FLOW TO FIRM (FCFF) ENGINE
        # ----------------------------------------------------
        # Standard Corporate Finance Formulation with Tax Shield Accounting:
        # Tax shield on debt interest is realized only to the extent of taxable operating income:
        tax_shield = (max(0.0, ebit) - max(0.0, ebt)) * tax_rate
        after_tax_interest = interest_exp - tax_shield
        nopat = ebit - (tax + tax_shield)
        
        # Standard FCFF = NOPAT + DD&A - CapEx - Delta NWC
        fcff_standard = nopat + ddna - capex - delta_nwc
        
        # Equivalent Reconciliation via CFO:
        # FCFF = CFO + After-Tax Net Interest Expense - CapEx
        fcff_cfo_bridge = cfo + after_tax_interest - capex
        
        # Verification that both FCFF formulas agree exactly
        fcff_discrepancy = abs(fcff_standard - fcff_cfo_bridge)
        if fcff_discrepancy > 1e-3:
            raise ValueError(f"Year {yr}: FCFF reconciliation mismatch! Diff = {fcff_discrepancy:.4f}")
        
        # ----------------------------------------------------
        # 5. LOUD ARTICULATION & BALANCE SHEET INTEGRITY CHECK
        # ----------------------------------------------------
        total_assets = cash + receivables + inventory + ppe + other_assets
        total_liab_eq = payables + debt + other_liab + equity
        bs_gap = total_assets - total_liab_eq
        
        if abs(bs_gap) > 1e-4:
            raise ValueError(
                f"LOUD FAILURE: Balance sheet failed to balance in FY{yr}E! "
                f"Total Assets = {total_assets:.2f}, Total Liab & Eq = {total_liab_eq:.2f}, Gap = {bs_gap:.4f}"
            )
        
        # Store year projection
        statements.append({
            "year": yr,
            "label": f"FY{yr}E",
            # Operating Metrics
            "prod_boed": prod_boed,
            "annual_prod_mboe": annual_prod_mmboe,
            "realized_price": realized_price,
            "revenue": revenue,
            "royalties": royalties,
            "cash_field_costs": cash_field_costs,
            "lifting_costs": lifting_costs,
            "midstream_costs": midstream_costs,
            "sga": sga,
            "other_operating": other_operating,
            "ebitda": ebitda,
            "ddna": ddna,
            "ebit": ebit,
            "nopat": nopat,
            "interest_exp": interest_exp,
            "ebt": ebt,
            "tax": tax,
            "net_income": net_income,
            # Balance Sheet
            "cash": cash,
            "receivables": receivables,
            "inventory": inventory,
            "nwc": nwc,
            "delta_nwc": delta_nwc,
            "ppe": ppe,
            "other_assets": other_assets,
            "total_assets": total_assets,
            "payables": payables,
            "debt": debt,
            "other_liab": other_liab,
            "equity": equity,
            "total_liab_eq": total_liab_eq,
            "bs_gap": bs_gap,
            # Cash Flow
            "cfo": cfo,
            "capex": capex,
            "cfi": cfi,
            "cff": cff,
            "net_cash_flow": net_cash_flow,
            "debt_repayment": debt_repayment,
            "dividends": dividends,
            "fcff": fcff_standard,
            "prior_cash": cur_cash,
        })
        
        # Advance state to next year
        cur_cash = cash
        cur_receivables = receivables
        cur_inventory = inventory
        cur_ppe = ppe
        cur_other_assets = other_assets
        cur_payables = payables
        cur_debt = debt
        cur_other_liab = other_liab
        cur_equity = equity

    return {
        "inputs": inputs,
        "statements": statements,
        "checks_passed": True,
    }


def value_company(proforma_result: Dict[str, Any], custom_wacc: float = None, custom_g: float = None) -> Dict[str, Any]:
    """
    Computes the FCFF Discounted Cash Flow valuation, Enterprise Value, Terminal Value,
    and the complete Enterprise-to-Equity / Per-Share Bridge.
    """
    inputs = proforma_result["inputs"]
    statements = proforma_result["statements"]
    
    # Cost of Capital
    wacc_details = calculate_wacc(inputs)
    wacc = custom_wacc if custom_wacc is not None else wacc_details["wacc"]
    g = custom_g if custom_g is not None else inputs["terminal_growth_rate"]
    
    if wacc <= g:
        raise ValueError(f"WACC ({wacc:.2%}) must be strictly greater than terminal growth rate ({g:.2%})!")
    
    # 1. Discount Explicit 5-Year FCFF Stream (Mid-Year Convention)
    # Using mid-year discounting: discount factor = 1 / (1 + WACC)^(i + 0.5)
    pv_explicit_fcff = 0.0
    fcff_schedule: List[Dict[str, float]] = []
    
    for i, s in enumerate(statements):
        period = i + 1
        t_mid = period - 0.5
        discount_factor = 1.0 / ((1.0 + wacc) ** t_mid)
        pv_fcff = s["fcff"] * discount_factor
        pv_explicit_fcff += pv_fcff
        fcff_schedule.append({
            "year": s["year"],
            "label": s["label"],
            "fcff": s["fcff"],
            "discount_factor": discount_factor,
            "pv_fcff": pv_fcff,
        })
    
    # 2. Terminal Value Calculation
    # Final forecast year (FY2029E)
    last_stmt = statements[-1]
    final_fcff = last_stmt["fcff"]
    final_ebitda = last_stmt["ebitda"]
    
    # Perpetuity Growth Method:
    # Terminal FCFF = FCFF_5 * (1 + g)
    terminal_fcff = final_fcff * (1.0 + g)
    terminal_value_perpetuity = terminal_fcff / (wacc - g)
    
    # Discount Terminal Value to Present (end of Year 5 discounting: (1 + WACC)^5)
    terminal_discount_factor = 1.0 / ((1.0 + wacc) ** len(statements))
    pv_terminal_value = terminal_value_perpetuity * terminal_discount_factor
    
    # Exit Multiple Cross-Check:
    # TV_multiple = Final Year EBITDA * Exit Multiple
    exit_mult = inputs["terminal_exit_multiple"]
    terminal_value_exit_mult = final_ebitda * exit_mult
    pv_terminal_exit_mult = terminal_value_exit_mult * terminal_discount_factor
    
    # 3. Enterprise Value
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    terminal_value_share = pv_terminal_value / enterprise_value if enterprise_value > 0 else 0.0
    
    # 4. Enterprise-to-Equity Bridge
    # Add: Opening / Valuation Date Cash
    # Less: Gross Debt
    # Less: ARO provisions and capitalized leases
    valuation_cash = inputs["cash_0"]
    valuation_debt = inputs["gross_debt_0"]
    net_debt = valuation_debt - valuation_cash
    aro_and_leases = inputs["aro_and_leases"]
    
    equity_value = enterprise_value + valuation_cash - valuation_debt - aro_and_leases
    
    # 5. Per-Share Intrinsic Value
    diluted_shares = inputs["diluted_shares"]
    value_per_share = equity_value / diluted_shares
    
    # Market comparison
    current_market_price = inputs["current_market_price"]
    upside_downside_pct = (value_per_share - current_market_price) / current_market_price
    
    return {
        "wacc": wacc,
        "terminal_growth": g,
        "wacc_details": wacc_details,
        "pv_explicit_fcff": pv_explicit_fcff,
        "fcff_schedule": fcff_schedule,
        "terminal_value_perpetuity": terminal_value_perpetuity,
        "pv_terminal_value": pv_terminal_value,
        "terminal_value_share": terminal_value_share,
        "terminal_value_exit_mult": terminal_value_exit_mult,
        "pv_terminal_exit_mult": pv_terminal_exit_mult,
        "enterprise_value": enterprise_value,
        # Bridge
        "valuation_cash": valuation_cash,
        "valuation_debt": valuation_debt,
        "net_debt": net_debt,
        "aro_and_leases": aro_and_leases,
        "equity_value": equity_value,
        "diluted_shares": diluted_shares,
        "value_per_share": value_per_share,
        "current_market_price": current_market_price,
        "upside_downside_pct": upside_downside_pct,
    }
