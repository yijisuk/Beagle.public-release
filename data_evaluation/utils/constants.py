from enum import Enum


class KeyValues(Enum):

    FINANCIALS_EVAL = "financials_eval"
    TECHNICALS_EVAL = "technicals_eval"
    ANALYSTS_EVAL = "analysts_eval"


class FinancialsKeyValues(Enum):

    COMPANY_BASIC_DATA = "company_basic_data"
    LIQUIDITY_RATIO_DATA = "liquidity_ratio_data_eval"
    TURNOVER_RATIO_DATA = "turnover_ratio_data_eval"
    PROFITABILITY_RATIO_DATA = "profitability_ratio_data_eval"
    BUSINESS_RISK_RATIO_DATA = "business_risk_ratio_data_eval"
    FINANCIAL_RISK_RATIO_DATA = "financial_risk_ratio_data_eval"
    STABILITY_RATIO_DATA = "stability_ratio_data_eval"
    VALUATION_RATIO_DATA = "valuation_ratio_data_eval"


class FinancialsSectionTitles(Enum):

    LIQUIDITY_RATIO_EVAL = "liquidity ratio evaluation data"
    TURNOVER_RATIO_EVAL = "turnover ratio evaluation data"
    PROFITABILITY_RATIO_EVAL = "profitability ratio evaluation data"
    BUSINESS_RISK_RATIO_EVAL = "business risk ratio evaluation data"
    FINANCIAL_RISK_RATIO_EVAL = "financial risk ratio evaluation data"
    STABILITY_RATIO_EVAL = "stability ratio evaluation data"
    VALUATION_RATIO_EVAL = "valuation ratio evaluation data"