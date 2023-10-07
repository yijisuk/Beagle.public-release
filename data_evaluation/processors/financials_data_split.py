from common_utils.constants.data_columns import FinancialsDataColumns as dc


def financials_data_split(data):

    base_cols = ["ticker"]

    # Company basic data
    # company_basic_cols = [
    #     "ticker", "company_name", "company_description",
    #     "sic_code", "sic_description",
    #     "marketcap", "weight", "exchange"
    # ]

    company_basic_cols = [
        "ticker",
        "sic_code", "sic_description",
        "marketcap", "weight", "exchange"
    ]

    company_basic_data = data[company_basic_cols]


    # Liquidity ratio data
    liquidity_ratio_cols = [
        dc.EVAL_CURRENT_RATIO.value,
        dc.EVAL_QUICK_RATIO.value,
        dc.EVAL_CASH_RATIO.value,
        dc.EVAL_CASH_CONVERSION_CYCLE.value,
    ]

    if ~data[liquidity_ratio_cols].isnull().all():

        liquidity_ratio_cols = base_cols + liquidity_ratio_cols
        liquidity_ratio_data = data[liquidity_ratio_cols]

        liquidity_ratio_data_eval = (
            "Liquidity ratio determines a business's ability to meet its financial obligations "
            "during the short term and maintain its short-term debt-paying ability. "
            "Liquidity ratios: Current ratio, Quick ratio, Cash ratio, and Cash conversion cycle "
            "were evaluated."
            "A value of 1 means the company's liquidity ratio meets the criteria for the company to be considered as liquid. "
            "A value of 0 means the company's liquidity ratio does not meet the criteria for the company to be considered as liquid. "

            "Here are the results of the evaluation:\n"
            f"Current ratio: {liquidity_ratio_data[dc.EVAL_CURRENT_RATIO.value]}\n"
            f"Quick ratio: {liquidity_ratio_data[dc.EVAL_QUICK_RATIO.value]}\n"
            f"Cash ratio: {liquidity_ratio_data[dc.EVAL_CASH_RATIO.value]}\n"
            f"Cash conversion cycle: {liquidity_ratio_data[dc.EVAL_CASH_CONVERSION_CYCLE.value]}\n"
        )

    else:
        liquidity_ratio_data_eval = None


    # Turnover ratio data
    turnover_ratio_cols = [
        dc.EVAL_INVENTORY_TURNOVER_RATIO.value,
        dc.EVAL_RECEIVABLES_TURNOVER_RATIO.value,
        dc.EVAL_CAPITAL_TURNOVER_RATIO.value,
        dc.EVAL_ASSET_TURNOVER_RATIO.value,
        dc.EVAL_NET_WORKING_CAPITAL_TURNOVER_RATIO.value,
        dc.EVAL_CASH_CONVERSION_CYCLE.value,
    ]

    if ~data[turnover_ratio_cols].isnull().all():

        turnover_ratio_cols = base_cols + turnover_ratio_cols
        turnover_ratio_data = data[turnover_ratio_cols]

        turnover_ratio_data_eval = (
            "Turnover ratio determines how efficiently a company is using its assets to generate revenue. "
            "Turnover ratios: Inventory turnover ratio, Receivables turnover ratio, Capital turnover ratio, "
            "Asset turnover ratio, Net working capital turnover ratio, and Cash conversion cycle were evaluated. "
            "A value of 1 means the company's turnover ratio meets the criteria for the company to be considered as having a good management. "
            "A value of 0 means the company's turnover ratio does not meet the criteria for the company to be considered as having a good management. "

            "Here are the results of the evaluation:\n"
            f"Inventory turnover ratio: {turnover_ratio_data[dc.EVAL_INVENTORY_TURNOVER_RATIO.value]}\n"
            f"Receivables turnover ratio: {turnover_ratio_data[dc.EVAL_RECEIVABLES_TURNOVER_RATIO.value]}\n"
            f"Capital turnover ratio: {turnover_ratio_data[dc.EVAL_CAPITAL_TURNOVER_RATIO.value]}\n"
            f"Asset turnover ratio: {turnover_ratio_data[dc.EVAL_ASSET_TURNOVER_RATIO.value]}\n"
            f"Net working capital turnover ratio: {turnover_ratio_data[dc.EVAL_NET_WORKING_CAPITAL_TURNOVER_RATIO.value]}\n"
            f"Cash conversion cycle: {turnover_ratio_data[dc.EVAL_CASH_CONVERSION_CYCLE.value]}\n"
        )

    else:
        turnover_ratio_data_eval = None


    # Profitability ratio data
    profitability_ratio_cols = [
        dc.EVAL_GROSS_PROFIT_MARGIN.value,
        dc.EVAL_NET_PROFIT_MARGIN.value,
        dc.EVAL_OPERATING_PROFIT_MARGIN.value,
        dc.EVAL_PRETAX_PROFIT_MARGIN.value,
        dc.EVAL_RETURN_ON_ASSETS.value,
        dc.EVAL_RETURN_ON_EQUITY.value,
        dc.EVAL_RETURN_ON_CAPITAL_EMPLOYED.value,
        dc.EVAL_EARNINGS_PER_SHARE.value,
    ]

    if ~data[profitability_ratio_cols].isnull().all():

        profitability_ratio_cols = base_cols + profitability_ratio_cols
        profitability_ratio_data = data[profitability_ratio_cols]

        profitability_ratio_data_eval = (
            "Profitability ratio determines how well a company is able to generate profit from its operations. "
            "Profitability ratios: Gross profit margin, Net profit margin, Operating profit margin, Pretax profit margin, "
            "Return on assets, Return on equity, Return on capital employed, and Earnings per share were evaluated. "
            "A value of 1 means the company's profitability ratio meets the criteria for the company to be considered as profitable. "
            "A value of 0 means the company's profitability ratio does not meet the criteria for the company to be considered as profitable. "

            "Here are the results of the evaluation:\n"
            f"Gross profit margin: {profitability_ratio_data[dc.EVAL_GROSS_PROFIT_MARGIN.value]}\n"
            f"Net profit margin: {profitability_ratio_data[dc.EVAL_NET_PROFIT_MARGIN.value]}\n"
            f"Operating profit margin: {profitability_ratio_data[dc.EVAL_OPERATING_PROFIT_MARGIN.value]}\n"
            f"Pretax profit margin: {profitability_ratio_data[dc.EVAL_PRETAX_PROFIT_MARGIN.value]}\n"
            f"Return on assets: {profitability_ratio_data[dc.EVAL_RETURN_ON_ASSETS.value]}\n"
            f"Return on equity: {profitability_ratio_data[dc.EVAL_RETURN_ON_EQUITY.value]}\n"
            f"Return on capital employed: {profitability_ratio_data[dc.EVAL_RETURN_ON_CAPITAL_EMPLOYED.value]}\n"
            f"Earnings per share: {profitability_ratio_data[dc.EVAL_EARNINGS_PER_SHARE.value]}\n"
        )

    else:
        profitability_ratio_data_eval = None


    # Business risk ratio data
    business_risk_ratio_cols = [
        dc.EVAL_OPERATING_LEVERAGE.value,
        dc.EVAL_FINANCIAL_LEVERAGE.value,
        dc.EVAL_TOTAL_LEVERAGE.value,
    ]

    if ~data[business_risk_ratio_cols].isnull().all():

        business_risk_ratio_cols = base_cols + business_risk_ratio_cols
        business_risk_ratio_data = data[business_risk_ratio_cols]

        business_risk_ratio_data_eval = (
            "Business risk ratio determines how much risk a company is exposed to in terms of its operations. "
            "Business risk ratios: Operating leverage, Financial leverage, and Total leverage were evaluated. "
            "A value of 1 means the company's business risk ratio meets the criteria for the company to be considered as having a low risk. "
            "A value of 0 means the company's business risk ratio does not meet the criteria for the company to be considered as having a low risk. "

            "Here are the results of the evaluation:\n"
            f"Operating leverage: {business_risk_ratio_data[dc.EVAL_OPERATING_LEVERAGE.value]}\n"
            f"Financial leverage: {business_risk_ratio_data[dc.EVAL_FINANCIAL_LEVERAGE.value]}\n"
            f"Total leverage: {business_risk_ratio_data[dc.EVAL_TOTAL_LEVERAGE.value]}\n"
        )

    else:
        business_risk_ratio_data_eval = None


    # Financial risk ratio data
    financial_risk_ratio_cols = [
        dc.EVAL_DEBT_TO_EQUITY_RATIO.value,
        dc.EVAL_DIVIDEND_YIELD.value,
    ]

    if ~data[financial_risk_ratio_cols].isnull().all():

        financial_risk_ratio_cols = base_cols + financial_risk_ratio_cols
        financial_risk_ratio_data = data[financial_risk_ratio_cols]

        financial_risk_ratio_data_eval = (
            "Financial risk ratio determines how much risk a company is exposed to in terms of its finances. "
            "Financial risk ratios: Debt to equity ratio and Dividend yield were evaluated. "
            "A value of 1 means the company's financial risk ratio meets the criteria for the company to be considered as having a low risk. "
            "A value of 0 means the company's financial risk ratio does not meet the criteria for the company to be considered as having a low risk. "

            "Here are the results of the evaluation:\n"
            f"Debt to equity ratio: {financial_risk_ratio_data[dc.EVAL_DEBT_TO_EQUITY_RATIO.value]}\n"
            f"Dividend yield: {financial_risk_ratio_data[dc.EVAL_DIVIDEND_YIELD.value]}\n"
        )

    else:
        financial_risk_ratio_data_eval = None


    # Stability ratio data
    stability_ratio_cols = [
        dc.EVAL_FIXED_ASSET_RATIO.value,
        dc.EVAL_RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS.value,
        dc.EVAL_PROPRIETARY_RATIO.value,
        dc.EVAL_INTEREST_COVERAGE_RATIO.value,
    ]

    if ~data[stability_ratio_cols].isnull().all():

        stability_ratio_cols = base_cols + stability_ratio_cols
        stability_ratio_data = data[stability_ratio_cols]

        stability_ratio_data_eval = (
            "Stability ratio determines how stable a company is in terms of its operations. "
            "Stability ratios: Fixed asset ratio, Ratio of current assets to fixed assets, Proprietary ratio, and Interest coverage ratio were evaluated. "
            "A value of 1 means the company's stability ratio meets the criteria for the company to be considered as stable. "
            "A value of 0 means the company's stability ratio does not meet the criteria for the company to be considered as stable. "

            "Here are the results of the evaluation:\n"
            f"Fixed asset ratio: {stability_ratio_data[dc.EVAL_FIXED_ASSET_RATIO.value]}\n"
            f"Ratio of current assets to fixed assets: {stability_ratio_data[dc.EVAL_RATIO_TO_CURRENT_ASSETS_TO_FIXED_ASSETS.value]}\n"
            f"Proprietary ratio: {stability_ratio_data[dc.EVAL_PROPRIETARY_RATIO.value]}\n"
            f"Interest coverage ratio: {stability_ratio_data[dc.EVAL_INTEREST_COVERAGE_RATIO.value]}\n"
        )

    else:
        stability_ratio_data_eval = None


    # Valuation ratio data
    valuation_ratio_cols = [
        dc.EVAL_PRICE_EARNINGS_RATIO.value,
        dc.EVAL_BOOK_VALUE_PER_SHARE.value,
        dc.EVAL_FREE_CASH_FLOW.value,
        dc.EVAL_PRICE_BOOK_RATIO.value,
        dc.EVAL_PRICE_EARNINGS_TO_GROWTH_RATIO.value,
        # dc.EVAL_GRAHAMS_VALUATION.value,
    ]

    if ~data[valuation_ratio_cols].isnull().all():

        valuation_ratio_cols = base_cols + valuation_ratio_cols
        valuation_ratio_data = data[valuation_ratio_cols]

        valuation_ratio_data_eval = (
            "Valuation ratio determines how much a company is worth. "
            "Valuation ratios: Price earnings ratio, Book value per share, Free cash flow, Price book ratio, "
            "Price earnings to growth ratio, and Graham's valuation were evaluated. "
            "A value of 1 means the company's valuation ratio meets the criteria for the company to be considered as undervalued. "
            "A value of 0 means the company's valuation ratio does not meet the criteria for the company to be considered as undervalued. "

            "Here are the results of the evaluation:\n"
            f"Price earnings ratio: {valuation_ratio_data[dc.EVAL_PRICE_EARNINGS_RATIO.value]}\n"
            f"Book value per share: {valuation_ratio_data[dc.EVAL_BOOK_VALUE_PER_SHARE.value]}\n"
            f"Free cash flow: {valuation_ratio_data[dc.EVAL_FREE_CASH_FLOW.value]}\n"
            f"Price book ratio: {valuation_ratio_data[dc.EVAL_PRICE_BOOK_RATIO.value]}\n"
            f"Price earnings to growth ratio: {valuation_ratio_data[dc.EVAL_PRICE_EARNINGS_TO_GROWTH_RATIO.value]}\n"
            # f"Graham's valuation: {valuation_ratio_data[dc.EVAL_GRAHAMS_VALUATION.value]}\n"
        )

    else:
        valuation_ratio_data_eval = None

    return_data = {
        "company_basic_data": company_basic_data,
        "liquidity_ratio_data_eval": liquidity_ratio_data_eval,
        "turnover_ratio_data_eval": turnover_ratio_data_eval,
        "profitability_ratio_data_eval": profitability_ratio_data_eval,
        "business_risk_ratio_data_eval": business_risk_ratio_data_eval,
        "financial_risk_ratio_data_eval": financial_risk_ratio_data_eval,
        "stability_ratio_data_eval": stability_ratio_data_eval,
        "valuation_ratio_data_eval": valuation_ratio_data_eval,
    }

    return return_data