"""
engine/sensitivity.py
======================
Sensitivity Analysis, Scenario Engine & Market-Implied Expectations (Reverse-DCF)
Target: Vista Energy, S.A.B. de C.V. (NYSE: VIST)

Includes:
  1. 2D WACC x Terminal Growth Rate Sensitivity Matrix (EV and Value Per Share)
  2. One-at-a-Time (OAT) Sensitivity for Load-Bearing Drivers
  3. Terminal Value Share Analysis across parameter space
  4. Reverse-DCF Solver: Market-Implied Oil Price and Production CAGR at current price ($65.00)
"""

import copy
from typing import Dict, Any, List, Tuple
from engine.model import get_base_inputs, run_proforma, value_company


def run_wacc_growth_matrix(
    base_inputs: Dict[str, Any],
    wacc_rates: List[float] = None,
    growth_rates: List[float] = None
) -> Dict[str, Any]:
    """
    Computes a 2D matrix of Enterprise Value and Equity Value Per Share
    across ranges of WACC and Terminal Growth Rates.
    """
    if wacc_rates is None:
        wacc_rates = [0.110, 0.115, 0.120, 0.125, 0.129, 0.135, 0.140, 0.145, 0.150]
    if growth_rates is None:
        growth_rates = [0.010, 0.015, 0.020, 0.025, 0.030]

    proforma_res = run_proforma(copy.deepcopy(base_inputs))

    vps_grid: List[List[float]] = []
    ev_grid: List[List[float]] = []
    tv_share_grid: List[List[float]] = []

    for w in wacc_rates:
        vps_row = []
        ev_row = []
        tv_share_row = []
        for g in growth_rates:
            if w <= g:
                vps_row.append(float("nan"))
                ev_row.append(float("nan"))
                tv_share_row.append(float("nan"))
            else:
                val = value_company(proforma_res, custom_wacc=w, custom_g=g)
                vps_row.append(val["value_per_share"])
                ev_row.append(val["enterprise_value"])
                tv_share_row.append(val["terminal_value_share"])
        vps_grid.append(vps_row)
        ev_grid.append(ev_row)
        tv_share_grid.append(tv_share_row)

    return {
        "wacc_rates": wacc_rates,
        "growth_rates": growth_rates,
        "vps_grid": vps_grid,
        "ev_grid": ev_grid,
        "tv_share_grid": tv_share_grid,
    }


def run_oat_sensitivity(base_inputs: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Executes One-at-a-Time (OAT) sensitivity for key operating and financial drivers.
    Each run perturbs exactly one independent driver, holding all others constant at base.
    """
    base_run = run_proforma(copy.deepcopy(base_inputs))
    base_val = value_company(base_run)
    base_vps = base_val["value_per_share"]
    base_ebitda_5 = base_run["statements"][-1]["ebitda"]
    base_fcff_5 = base_run["statements"][-1]["fcff"]

    tests = [
        {
            "driver": "Realized Hydrocarbon Price",
            "unit": "$/boe",
            "base_desc": "$64.50 -> $61.50/boe",
            "low_desc": "-$5.00/boe shift",
            "high_desc": "+$5.00/boe shift",
            "param_key": "realized_price_forecast",
            "low_val": [p - 5.0 for p in base_inputs["realized_price_forecast"]],
            "high_val": [p + 5.0 for p in base_inputs["realized_price_forecast"]],
        },
        {
            "driver": "Net Production Volume",
            "unit": "boe/d",
            "base_desc": "105k -> 190k boe/d",
            "low_desc": "-10% production volume",
            "high_desc": "+10% production volume",
            "param_key": "prod_boed_forecast",
            "low_val": [p * 0.90 for p in base_inputs["prod_boed_forecast"]],
            "high_val": [p * 1.10 for p in base_inputs["prod_boed_forecast"]],
        },
        {
            "driver": "Lifting Cost per BOE",
            "unit": "$/boe",
            "base_desc": "$4.65 -> $4.40/boe",
            "low_desc": "-$0.75/boe (high efficiency)",
            "high_desc": "+$0.75/boe (cost inflation)",
            "param_key": "lifting_cost_per_boe",
            "low_val": [max(2.5, c - 0.75) for c in base_inputs["lifting_cost_per_boe"]],
            "high_val": [c + 0.75 for c in base_inputs["lifting_cost_per_boe"]],
        },
        {
            "driver": "Annual Development CapEx",
            "unit": "$M/year",
            "base_desc": "$950M -> $700M/yr",
            "low_desc": "-$100M/year",
            "high_desc": "+$100M/year",
            "param_key": "capex_forecast",
            "low_val": [c - 100.0 for c in base_inputs["capex_forecast"]],
            "high_val": [c + 100.0 for c in base_inputs["capex_forecast"]],
        },
        {
            "driver": "Country Risk Premium (CRP)",
            "unit": "bps",
            "base_desc": "400 bps (4.0%)",
            "low_desc": "300 bps (3.0%)",
            "high_desc": "550 bps (5.5%)",
            "param_key": "country_risk_premium",
            "low_val": 0.030,
            "high_val": 0.055,
        },
    ]

    results = []

    for t in tests:
        # Lower case
        inp_low = copy.deepcopy(base_inputs)
        inp_low[t["param_key"]] = t["low_val"]
        res_low = run_proforma(inp_low)
        val_low = value_company(res_low)
        vps_low = val_low["value_per_share"]
        ebitda_5_low = res_low["statements"][-1]["ebitda"]
        fcff_5_low = res_low["statements"][-1]["fcff"]

        # Higher case
        inp_high = copy.deepcopy(base_inputs)
        inp_high[t["param_key"]] = t["high_val"]
        res_high = run_proforma(inp_high)
        val_high = value_company(res_high)
        vps_high = val_high["value_per_share"]
        ebitda_5_high = res_high["statements"][-1]["ebitda"]
        fcff_5_high = res_high["statements"][-1]["fcff"]

        span_vps = abs(vps_high - vps_low)
        results.append({
            "driver": t["driver"],
            "unit": t["unit"],
            "base_desc": t["base_desc"],
            "low_desc": t["low_desc"],
            "high_desc": t["high_desc"],
            "vps_low": vps_low,
            "vps_base": base_vps,
            "vps_high": vps_high,
            "delta_vps_low": vps_low - base_vps,
            "delta_vps_high": vps_high - base_vps,
            "span_vps": span_vps,
            "ebitda_5_low": ebitda_5_low,
            "ebitda_5_high": ebitda_5_high,
            "fcff_5_low": fcff_5_low,
            "fcff_5_high": fcff_5_high,
        })

    # Sort results by output span descending to establish driver ranking
    results.sort(key=lambda x: x["span_vps"], reverse=True)
    return results


def solve_reverse_dcf(base_inputs: Dict[str, Any], target_price: float = 65.00) -> Dict[str, Any]:
    """
    Solves for the market-implied expectations embedded in the current trading price ($65.00/share).
    1. Implied Constant Flat Hydrocarbon Price ($/boe across all 5 years).
    2. Implied FY2029E Production Scale (boe/d) assuming base price trajectory.
    3. Implied Cost of Capital (WACC) assuming base operating plan.
    """
    # 1. Solve for Implied Hydrocarbon Price Shift (Delta $/boe applied across all years)
    def price_objective(delta_p: float) -> float:
        inp = copy.deepcopy(base_inputs)
        inp["realized_price_forecast"] = [p + delta_p for p in inp["realized_price_forecast"]]
        res = run_proforma(inp)
        val = value_company(res)
        return val["value_per_share"] - target_price

    # Bisection search for delta_p
    low_p, high_p = -30.0, 30.0
    for _ in range(50):
        mid_p = (low_p + high_p) / 2.0
        diff = price_objective(mid_p)
        if abs(diff) < 1e-3:
            break
        if diff < 0:  # Value too low -> need higher price
            low_p = mid_p
        else:
            high_p = mid_p
    implied_price_delta = mid_p
    implied_avg_realized_price = (sum(base_inputs["realized_price_forecast"]) / 5.0) + implied_price_delta

    # 2. Solve for Implied Production Scaling Factor
    def prod_objective(scale: float) -> float:
        inp = copy.deepcopy(base_inputs)
        inp["prod_boed_forecast"] = [p * scale for p in inp["prod_boed_forecast"]]
        res = run_proforma(inp)
        val = value_company(res)
        return val["value_per_share"] - target_price

    low_s, high_s = 0.40, 2.00
    for _ in range(50):
        mid_s = (low_s + high_s) / 2.0
        diff = prod_objective(mid_s)
        if abs(diff) < 1e-3:
            break
        if diff < 0:
            low_s = mid_s
        else:
            high_s = mid_s
    implied_prod_multiplier = mid_s
    implied_fy29_production = base_inputs["prod_boed_forecast"][-1] * implied_prod_multiplier

    # 3. Solve for Implied WACC
    proforma_base = run_proforma(copy.deepcopy(base_inputs))
    def wacc_objective(w: float) -> float:
        val = value_company(proforma_base, custom_wacc=w)
        return val["value_per_share"] - target_price

    low_w, high_w = 0.05, 0.30
    for _ in range(50):
        mid_w = (low_w + high_w) / 2.0
        diff = wacc_objective(mid_w)
        if abs(diff) < 1e-3:
            break
        if diff > 0:  # Higher price means WACC is too low
            low_w = mid_w
        else:
            high_w = mid_w
    implied_wacc = mid_w

    return {
        "target_price": target_price,
        "base_model_price": value_company(proforma_base)["value_per_share"],
        "implied_price_delta": implied_price_delta,
        "implied_avg_realized_price": implied_avg_realized_price,
        "implied_prod_multiplier": implied_prod_multiplier,
        "implied_fy29_production": implied_fy29_production,
        "implied_wacc": implied_wacc,
    }
