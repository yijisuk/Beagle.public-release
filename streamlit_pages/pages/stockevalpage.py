import streamlit as st

from ..base.basepage import BasePage
from streamlit_pages.pages.tradingview.company_info import CompanyInfo
from data_evaluation.utils.base_validation import Validator
from data_evaluation.ticker_eval import TickerEvaluator


class StockEvalPage(BasePage):

    def __init__(self):

        super().__init__()

        self.user_input = None
        self.ticker = None
        self.exchange = None

        self.ticker_data = self.datasetloader.ticker_data

        self.display_title()
        self.display_evaluation()


    def display_title(self):

        self.intro()

        self.user_input = st.selectbox(
            label="Select a company to analyze:",
            index=None,
            options=self.datasetloader.company_list
        )

        _, _, endcol = st.columns(3)

        with endcol:
            self.search = st.button("Search", type="primary", use_container_width=True)


    def display_evaluation(self):

        evalcol, infocol = st.columns(2, gap="medium")

        with evalcol:
            if self.search:
                if self.user_input is not None:

                    ticker = self.user_input.split(":")[0].strip()

                    validator = Validator(
                        user_input=ticker,
                        ticker_data=self.ticker_data
                    )

                    validation_result = validator.base_validation()
                    if validation_result["result"]:

                        ticker_val = validation_result["ticker"]
                
                        tickerevaluator = TickerEvaluator(
                            ticker=ticker_val,
                            organized_ticker_data=self.ticker_data,
                        )
                        self.ticker, self.exchange = tickerevaluator.ticker_search()

                        if self.user_input is not None and self.exchange is not None:
                            tickerevaluator.ticker_eval()

                    elif validation_result["result"] is False:
                        st.write("Please select one of the provided companies.")
                        st.write("If a company has been selected, but the error message is displayed, try again after refreshing the page.")

                elif self.user_input is None:
                    st.write("Please select one of the provided companies.")
            

        with infocol:

            if self.ticker is not None and self.exchange is not None:
                _ = CompanyInfo(exchange=self.exchange, ticker=self.ticker, theme=st.theme().lower())


    def intro(self):

        st.title("Beagle 🐶", anchor=False)
        st.header("Evaluate company financials, price technicals, and analysts' forecasts 💡")
        st.write("Select a company to get started.")
        st.write("The search engine is a demo deployment, and the supported tickers are limited.")
        st.write("Processing the evaluation for each criteria may take up to 30 seconds.")
        st.divider()