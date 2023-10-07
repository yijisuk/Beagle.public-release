from enum import Enum


class FinancialsDataColumns(Enum):

    ### Liquidity Ratios ==============================
    # Current Ratio
    CURRENT_RATIO = "currentRatio"
    EVAL_CURRENT_RATIO = f"{CURRENT_RATIO}_liquid"

    # Quick Ratio
    QUICK_RATIO = "quickRatio"
    EVAL_QUICK_RATIO = f"{QUICK_RATIO}_liquid"

    # Absolute Liquid Ratio
    ABSOLUTE_LIQUID_RATIO = "absoluteLiquidRatio"
    W_ABSOLUTE_LIQUID_RATIO = f"weighted_{ABSOLUTE_LIQUID_RATIO}"
    WAVG_ABSOLUTE_LIQUID_RATIO = f"weighted_avg_{ABSOLUTE_LIQUID_RATIO}"
    EVAL_ABSOLUTE_LIQUID_RATIO = f"{ABSOLUTE_LIQUID_RATIO}_liquid"

    # Cash Ratio
    CASH_RATIO = "cashRatio"
    W_CASH_RATIO = f"weighted_{CASH_RATIO}"
    WAVG_CASH_RATIO = f"weighted_avg_{CASH_RATIO}"
    EVAL_CASH_RATIO = f"{CASH_RATIO}_liquid"

    ### Turnover Ratios ==============================
    # Inventory Turnover Ratio
    INVENTORY_TURNOVER_RATIO = "inventoryTurnoverRatio"
    W_INVENTORY_TURNOVER_RATIO = f"weighted_{INVENTORY_TURNOVER_RATIO}"
    WAVG_INVENTORY_TURNOVER_RATIO = f"weighted_avg_{INVENTORY_TURNOVER_RATIO}"
    EVAL_INVENTORY_TURNOVER_RATIO = f"{INVENTORY_TURNOVER_RATIO}_good_management"

    # Receivables Turnover Ratio
    RECEIVABLES_TURNOVER_RATIO = "receivablesTurnoverRatio"
    W_RECEIVABLES_TURNOVER_RATIO = f"weighted_{RECEIVABLES_TURNOVER_RATIO}"
    WAVG_RECEIVABLES_TURNOVER_RATIO = f"weighted_avg_{RECEIVABLES_TURNOVER_RATIO}"
    EVAL_RECEIVABLES_TURNOVER_RATIO = f"{RECEIVABLES_TURNOVER_RATIO}_good_management"

    # Capital Turnover Ratio
    CAPITAL_TURNOVER_RATIO = "capitalTurnoverRatio"
    W_CAPITAL_TURNOVER_RATIO = f"weighted_{CAPITAL_TURNOVER_RATIO}"
    WAVG_CAPITAL_TURNOVER_RATIO = f"weighted_avg_{CAPITAL_TURNOVER_RATIO}"
    EVAL_CAPITAL_TURNOVER_RATIO = f"{CAPITAL_TURNOVER_RATIO}_good_management"

    # Asset Turnover Ratio
    ASSET_TURNOVER_RATIO = "assetTurnoverRatio"
    W_ASSET_TURNOVER_RATIO = f"weighted_{ASSET_TURNOVER_RATIO}"
    WAVG_ASSET_TURNOVER_RATIO = f"weighted_avg_{ASSET_TURNOVER_RATIO}"
    EVAL_ASSET_TURNOVER_RATIO = f"{ASSET_TURNOVER_RATIO}_good_management"

    # Net Working Capital Turnover Ratio
    NET_WORKING_CAPITAL_TURNOVER_RATIO = "netWorkingCapitalTurnoverRatio"
    W_NET_WORKING_CAPITAL_TURNOVER_RATIO = f"weighted_{NET_WORKING_CAPITAL_TURNOVER_RATIO}"
    WAVG_NET_WORKING_CAPITAL_TURNOVER_RATIO = f"weighted_avg_{NET_WORKING_CAPITAL_TURNOVER_RATIO}"
    EVAL_NET_WORKING_CAPITAL_TURNOVER_RATIO = f"{NET_WORKING_CAPITAL_TURNOVER_RATIO}_good_management"

    # Cash Conversion Cycle
    CASH_CONVERSION_CYCLE = "cashConversionCycle"
    W_CASH_CONVERSION_CYCLE = f"weighted_{CASH_CONVERSION_CYCLE}"
    WAVG_CASH_CONVERSION_CYCLE = f"weighted_avg_{CASH_CONVERSION_CYCLE}"
    EVAL_CASH_CONVERSION_CYCLE = f"{CASH_CONVERSION_CYCLE}_efficient"

    ### Operating Profitability Ratios ==============================
    # Gross Profit Margin
    GROSS_PROFIT_MARGIN = "grossProfitMargin"
    W_GROSS_PROFIT_MARGIN = f"weighted_{GROSS_PROFIT_MARGIN}"
    WAVG_GROSS_PROFIT_MARGIN = f"weighted_avg_{GROSS_PROFIT_MARGIN}"
    EVAL_GROSS_PROFIT_MARGIN = f"{GROSS_PROFIT_MARGIN}_profitable"

    # Net Profit Margin
    NET_PROFIT_MARGIN = "netProfitMargin"
    W_NET_PROFIT_MARGIN = f"weighted_{NET_PROFIT_MARGIN}"
    WAVG_NET_PROFIT_MARGIN = f"weighted_avg_{NET_PROFIT_MARGIN}"
    EVAL_NET_PROFIT_MARGIN = f"{NET_PROFIT_MARGIN}_profitable"

    # Operating Profit Margin
    OPERATING_PROFIT_MARGIN = "operatingProfitMargin"
    W_OPERATING_PROFIT_MARGIN = f"weighted_{OPERATING_PROFIT_MARGIN}"
    WAVG_OPERATING_PROFIT_MARGIN = f"weighted_avg_{OPERATING_PROFIT_MARGIN}"
    EVAL_OPERATING_PROFIT_MARGIN = f"{OPERATING_PROFIT_MARGIN}_profitable"

    # Pretax Profit Margin
    PRETAX_PROFIT_MARGIN = "pretaxProfitMargin"
    W_PRETAX_PROFIT_MARGIN = f"weighted_{PRETAX_PROFIT_MARGIN}"
    WAVG_PRETAX_PROFIT_MARGIN = f"weighted_avg_{PRETAX_PROFIT_MARGIN}"
    EVAL_PRETAX_PROFIT_MARGIN = f"{PRETAX_PROFIT_MARGIN}_profitable"

    # Return On Assets
    RETURN_ON_ASSETS = "returnOnAssets"
    W_RETURN_ON_ASSETS = f"weighted_{RETURN_ON_ASSETS}"
    WAVG_RETURN_ON_ASSETS = f"weighted_avg_{RETURN_ON_ASSETS}"
    EVAL_RETURN_ON_ASSETS = f"{RETURN_ON_ASSETS}_profitable"

    # Return on Equity
    RETURN_ON_EQUITY = "returnOnEquity"
    W_RETURN_ON_EQUITY = f"weighted_{RETURN_ON_EQUITY}"
    WAVG_RETURN_ON_EQUITY = f"weighted_avg_{RETURN_ON_EQUITY}"
    EVAL_RETURN_ON_EQUITY = f"{RETURN_ON_EQUITY}_profitable"

    # Return on Capital Employed
    RETURN_ON_CAPITAL_EMPLOYED = "returnOnCapitalEmployed"
    W_RETURN_ON_CAPITAL_EMPLOYED = f"weighted_{RETURN_ON_CAPITAL_EMPLOYED}"
    WAVG_RETURN_ON_CAPITAL_EMPLOYED = f"weighted_avg_{RETURN_ON_CAPITAL_EMPLOYED}"
    EVAL_RETURN_ON_CAPITAL_EMPLOYED = f"{RETURN_ON_CAPITAL_EMPLOYED}_profitable"

    # Earnings Per Share
    EARNINGS_PER_SHARE = "earningsPerShare"
    W_EARNINGS_PER_SHARE = f"weighted_{EARNINGS_PER_SHARE}"
    WAVG_EARNINGS_PER_SHARE = f"weighted_avg_{EARNINGS_PER_SHARE}"
    EVAL_EARNINGS_PER_SHARE = f"{EARNINGS_PER_SHARE}_profitable"

    ### Business Risk Ratios ==============================
    # Operating Leverage
    OPERATING_LEVERAGE = "operatingLeverage"
    W_OPERATING_LEVERAGE = f"weighted_{OPERATING_LEVERAGE}"
    WAVG_OPERATING_LEVERAGE = f"weighted_avg_{OPERATING_LEVERAGE}"
    EVAL_OPERATING_LEVERAGE = f"{OPERATING_LEVERAGE}_low_risk"

    # Financial Leverage
    FINANCIAL_LEVERAGE = "financialLeverage"
    W_FINANCIAL_LEVERAGE = f"weighted_{FINANCIAL_LEVERAGE}"
    WAVG_FINANCIAL_LEVERAGE = f"weighted_avg_{FINANCIAL_LEVERAGE}"
    EVAL_FINANCIAL_LEVERAGE = f"{FINANCIAL_LEVERAGE}_low_risk"

    # Total Leverage
    TOTAL_LEVERAGE = "totalLeverage"
    W_TOTAL_LEVERAGE = f"weighted_{TOTAL_LEVERAGE}"
    WAVG_TOTAL_LEVERAGE = f"weighted_avg_{TOTAL_LEVERAGE}"
    EVAL_TOTAL_LEVERAGE = f"{TOTAL_LEVERAGE}_low_risk"

    ### Financial Risk Ratios ==============================
    # Debt to Equity Ratio
    DEBT_TO_EQUITY_RATIO = "debtToEquityRatio"
    W_DEBT_TO_EQUITY_RATIO = f"weighted_{DEBT_TO_EQUITY_RATIO}"
    WAVG_DEBT_TO_EQUITY_RATIO = f"weighted_avg_{DEBT_TO_EQUITY_RATIO}"
    EVAL_DEBT_TO_EQUITY_RATIO = f"{DEBT_TO_EQUITY_RATIO}_low_risk"

    # Dividend Yield
    DIVIDEND_YIELD = "dividendYield"
    W_DIVIDEND_YIELD = f"weighted_{DIVIDEND_YIELD}"
    WAVG_DIVIDEND_YIELD = f"weighted_avg_{DIVIDEND_YIELD}"
    EVAL_DIVIDEND_YIELD = f"{DIVIDEND_YIELD}_high_yield"

    ### Stability Ratios ==============================
    # Fixed Asset Ratio
    FIXED_ASSET_RATIO = "fixedAssetRatio"
    W_FIXED_ASSET_RATIO = f"weighted_{FIXED_ASSET_RATIO}"
    WAVG_FIXED_ASSET_RATIO = f"weighted_avg_{FIXED_ASSET_RATIO}"
    EVAL_FIXED_ASSET_RATIO = f"{FIXED_ASSET_RATIO}_liquid"

    # Ratio to Current Assets to Fixed Assets
    RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS = "ratioToCurrentAssetsToFixedAssets"
    W_RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS = f"weighted_{RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS}"
    WAVG_RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS = f"weighted_avg_{RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS}"
    EVAL_RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS = f"{RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS}_liquid"

    # Proprietary Ratio
    PROPRIETARY_RATIO = "proprietaryRatio"
    W_PROPRIETARY_RATIO = f"weighted_{PROPRIETARY_RATIO}"
    WAVG_PROPRIETARY_RATIO = f"weighted_avg_{PROPRIETARY_RATIO}"
    EVAL_PROPRIETARY_RATIO = f"{PROPRIETARY_RATIO}_liquid"

    # Interest Coverage Ratio
    INTEREST_COVERAGE_RATIO = "interestCoverageRatio"
    W_INTEREST_COVERAGE_RATIO = f"weighted_{INTEREST_COVERAGE_RATIO}"
    WAVG_INTEREST_COVERAGE_RATIO = f"weighted_avg_{INTEREST_COVERAGE_RATIO}"
    EVAL_INTEREST_COVERAGE_RATIO = f"{INTEREST_COVERAGE_RATIO}_low_risk"

    ### Valuation Ratios ==============================
    # Price Earnings Ratio
    PRICE_EARNINGS_RATIO = "priceEarningsRatio"
    W_PRICE_EARNINGS_RATIO = f"weighted_{PRICE_EARNINGS_RATIO}"
    WAVG_PRICE_EARNINGS_RATIO = f"weighted_avg_{PRICE_EARNINGS_RATIO}"
    EVAL_PRICE_EARNINGS_RATIO = f"{PRICE_EARNINGS_RATIO}_undervalued"

    # Book Value Per Share
    BOOK_VALUE_PER_SHARE = "bookValuePerShare"
    EVAL_BOOK_VALUE_PER_SHARE = f"{BOOK_VALUE_PER_SHARE}_undervalued"

    # Free Cash Flow
    FREE_CASH_FLOW = "freeCashFlow"
    EVAL_FREE_CASH_FLOW = f"{FREE_CASH_FLOW}_positive"

    # Price Book Ratio
    PRICE_BOOK_RATIO = "priceBookRatio"
    EVAL_PRICE_BOOK_RATIO = f"{PRICE_BOOK_RATIO}_undervalued"

    # Price Earnings To Growth Ratio
    PRICE_EARNINGS_TO_GROWTH_RATIO = "priceEarningsToGrowthRatio"
    EVAL_PRICE_EARNINGS_TO_GROWTH_RATIO = f"{PRICE_EARNINGS_TO_GROWTH_RATIO}_undervalued"

    # Graham's Valuation
    GRAHAMS_VALUATION = "grahamsValuation"
    EVAL_GRAHAMS_VALUATION = f"{GRAHAMS_VALUATION}_undervalued"


class TechnicalColumns(Enum):

    SIC_CODE = "sic_code"
    SIC_DESCRIPTION = "sic_description"
    TICKER = "ticker"

    OSC_SCORE = "oscillator_score"
    OSC_DECISION = "oscillator_decision"

    OSC_STRONG_BUY_COUNT = "oscillator_strong_buy_count"
    OSC_BUY_COUNT = "oscillator_buy_count"
    OSC_NEUTRAL_COUNT = "oscillator_neutral_count"
    OSC_SELL_COUNT = "oscillator_sell_count"
    OSC_STRONG_SELL_COUNT = "oscillator_strong_sell_count"

    MOVING_AVG_SCORE = "moving_average_score"
    MOVING_AVG_DECISION = "moving_average_decision"

    MOVING_AVG_STRONG_BUY_COUNT = "moving_average_strong_buy_count"
    MOVING_AVG_BUY_COUNT = "moving_average_buy_count"
    MOVING_AVG_NEUTRAL_COUNT = "moving_average_neutral_count"
    MOVING_AVG_SELL_COUNT = "moving_average_sell_count"
    MOVING_AVG_STRONG_SELL_COUNT = "moving_average_strong_sell_count"

    DECISION = "decision"


class AnalystInsightColumns(Enum):

    HIGH_PCT = "high_percentage"
    MEDIAN_PCT = "median_percentage"
    LOW_PCT = "low_percentage"
    AVG_PCT = "avg_percentage"

    HL_GAP = "high_low_gap"
    HM_GAP = "high_median_gap"

    NUM_RATINGS = "num_ratings"
    AVG_REC = "avg_recommendation"

    TM_BUY_PCT_CHANGE = "tm_buy_percentage_change"
    TM_OVERWEIGHT_PCT_CHANGE = "tm_overweight_percentage_change"
    TM_HOLD_PCT_CHANGE = "tm_hold_percentage_change"
    TM_UNDERWEIGHT_PCT_CHANGE = "tm_underweight_percentage_change"
    TM_SELL_PCT_CHANGE = "tm_sell_percentage_change"

    OM_BUY_PCT_CHANGE = "om_buy_percentage_change"
    OM_OVERWEIGHT_PCT_CHANGE = "om_overweight_percentage_change"
    OM_HOLD_PCT_CHANGE = "om_hold_percentage_change"
    OM_UNDERWEIGHT_PCT_CHANGE = "om_underweight_percentage_change"
    OM_SELL_PCT_CHANGE = "om_sell_percentage_change"

    CURR_BUY_PCT = "curr_buy_percentage"
    CURR_OVERWEIGHT_PCT = "curr_overweight_percentage"
    CURR_HOLD_PCT = "curr_hold_percentage"
    CURR_UNDERWEIGHT_PCT = "curr_underweight_percentage"
    CURR_SELL_PCT = "curr_sell_percentage"