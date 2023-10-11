import streamlit as st
import plotly.graph_objects as go

from .formatters.financials_eval_formatter import FinancialsEvaluationFormatter
from .formatters.technicals_eval_formatter import TechnicalsEvaluationFormatter
from .tradingview.technicals import technicals
from .utils.constants import (
    KeyValues as kv,
    EvaluationCriterionDescriptions as ecd
)
from common_utils.visualization.gauge import gauge


class TickerEvaluator:

    def __init__(self, ticker, organized_ticker_data):

        self.ticker = ticker
        self.exchange = None

        self.organized_ticker_data = organized_ticker_data

        self.data = None
        self.evaluation_score = {
            "liquidity": None,
            "operation_efficiency": None,
            "profitability": None,
            "business_stability": None,
            "financial_stability": None,
            "overall_stability": None,
            "valuation": None,
        }


    def ticker_eval(self):

        self.financials_evaluation()
        self.technicals_evaluation()
        self.additional_resources()


    def financials_evaluation(self):

        ### Financials Evaluation
        st.header("Financials Evaluation")
        st.subheader("The Details:")

        # Base setups
        financials_eval = self.data[kv.FINANCIALS_EVAL.value]
        financials_formatter = FinancialsEvaluationFormatter(
            self.ticker, financials_eval)

        # Company introduction
        company_intro = financials_formatter.company_introduction()

        # Liquidity Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.liquidity_evaluation(),
            subheader_title = "Liquidity",
            subheader_description = ecd.LIQUIDITY.value
        )

        # Turnover Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.turnover_evaluation(),
            subheader_title = "Operation Efficiency",
            subheader_description = ecd.OPERATION_EFFICIENCY.value
        )

        # Profitability Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.profitability_evaluation(),
            subheader_title = "Profitability",
            subheader_description = ecd.PROFITABILITY.value
        )

        # Business Risk Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.business_risk_evaluation(),
            subheader_title = "Business Stability",
            subheader_description = ecd.BUSINESS_STABILITY.value
        )

        # Financial Risk Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.financial_risk_evaluation(),
            subheader_title = "Financial Stability",
            subheader_description = ecd.FINANCIAL_STABILITY.value
        )

        # Stability Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.stability_evaluation(),
            subheader_title = "Overall Stability",
            subheader_description = ecd.OVERALL_STABILITY.value
        )

        # Valuation Ratio Evaluation
        self.base_eval_formatting(
            result = financials_formatter.valuation_evaluation(),
            subheader_title = "Valuation",
            subheader_description = ecd.VALUATION.value
        )
        
        # Detailed evaluation
        eval_agg = financials_formatter.evaluate_financials()

        # Summary
        summary = financials_formatter.summarize_financials(eval_agg)

        short_term_score, long_term_score = self.calculate_overall_score()
        
        st.subheader("To summarize,")
        st.write(summary)

        st.subheader("Overall Evaluation Score:")
        st.write(f"{self.ticker} as an investment...")

        col1, col2 = st.columns(2, gap="medium")

        with col1:
            st.write(f"In the short-term, the score would be: {short_term_score} out of 5")
            st_gauge = go.Figure(gauge(
                value=short_term_score, range=[0, 5],
                title="Short-term Score"))
            st.plotly_chart(st_gauge, use_container_width=True)

        with col2:
            st.write(f"In the long-term, the score would be: {long_term_score} out of 5")
            lt_gauge = go.Figure(gauge(
                value=long_term_score, range=[0, 5],
                title="Long-term Score"))
            st.plotly_chart(lt_gauge, use_container_width=True)


    def technicals_evaluation(self):

        ### TODO: Update Technicals Evaluation
        st.header("Technicals Evaluation")

        # technicals_formatter = TechnicalsEvaluationFormatter(
        #     self.ticker, self.data[kv.TECHNICALS_EVAL.value])
        
        # technicals_vis = technicals_formatter.visualize_technicals()

        # if technicals_vis is None:
        #     st.write("No technicals data available.")
        # else:
        #     st.plotly_chart(technicals_vis, use_container_width=True)

        technicals(self.ticker, self.exchange)


    def additional_resources(self):

        st.header("Additional Resources")
        st.write("Here are some additional resources that you can use to further evaluate the company.")

        col1, col2, col3 = st.columns(3, gap="medium")

        with col1:
            marketwatch_url = f"https://www.marketwatch.com/investing/stock/{self.ticker.lower()}/analystestimates"
            st.subheader(f"[MarketWatch]({marketwatch_url})")
            st.write(f"Detailed analyst estimate statistics on {self.ticker}, including price targets and recommendations.")

        with col2:
            tipranks_url = f"https://www.tipranks.com/stocks/{self.ticker.lower()}/forecast"
            st.subheader(f"[TipRanks]({tipranks_url})")
            st.write(f"Comprehensive analysis on {self.ticker}, including analyst estimates, company financials, and market sentiment.")

        with col3:
            alphaspread_url = f"https://www.alphaspread.com/security/{self.exchange.lower()}/{self.ticker.lower()}/summary"
            st.subheader(f"[AlphaSpread]({alphaspread_url})")
            st.write(f"Intrinsic value, fundamental analysis, and competitor analysis on {self.ticker}.")

        
    def ticker_search(self):

        financials_eval = self.get_evaluation_data(self.organized_ticker_data)

        self.data = {
            kv.FINANCIALS_EVAL.value: financials_eval \
                if financials_eval is not None and not financials_eval.empty else None,
        }

        try:
            ticker_info = financials_eval["ticker"]
            exchange_info = financials_eval["exchange"]

        except:
            ticker_info = None
            exchange_info = None

        if exchange_info == "XNYS":
            exchange_info = "NYSE"

        elif exchange_info == "XNAS":
            exchange_info = "NASDAQ"

        self.exchange = exchange_info

        return (ticker_info, exchange_info)


    def get_evaluation_data(self, data):

        try:
            return data[data["ticker"] == self.ticker].reset_index(drop=True).iloc[0]
        except IndexError:
            return None
        

    def base_eval_formatting(self, result, subheader_title, subheader_description):

        key = subheader_title.lower().replace(" ", "_")

        if None not in result:
            ratio_eval, ratio_score = result

            st.subheader(f"{subheader_title}: {ratio_score} out of 5")
            st.caption(subheader_description)
            st.write(ratio_eval)

            self.evaluation_score[key] = ratio_score

        else:
            self.evaluation_score[key] = 0


    def calculate_overall_score(self):

        short_term_weights = {
            'liquidity': 0.2,
            'operation_efficiency': 0.15,
            'profitability': 0.3,
            'business_stability': 0.1,
            'financial_stability': 0.1,
            'overall_stability': 0.05,
            'valuation': 0.1
        }

        long_term_weights = {
            'liquidity': 0.1,
            'operation_efficiency': 0.1,
            'profitability': 0.2,
            'business_stability': 0.2,
            'financial_stability': 0.2,
            'overall_stability': 0.05,
            'valuation': 0.15
        }

        short_term_score = sum(
            self.evaluation_score[key] * short_term_weights[key] for key in self.evaluation_score)
        long_term_score = sum(
            self.evaluation_score[key] * long_term_weights[key] for key in self.evaluation_score)

        short_term_score = round(max(0, min(short_term_score, 5)), 2)
        long_term_score = round(max(0, min(long_term_score, 5)), 2)

        return (short_term_score, long_term_score)
    

filler_str = "====================================================================================================="