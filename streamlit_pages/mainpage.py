import streamlit as st

from .pages.stockevalpage import StockEvalPage
from .pages.marketpage import MarketPage
from .pages.economypage import EconomyPage


class MainPage():

    def __init__(self):

        stockEvalTab, marketTab, economyTab = st.tabs(
            [
                "🔍 Stock Evaluation", 
                "📈 Market", 
                "💵 Economy",
            ]
        )

        with stockEvalTab:
            _ = StockEvalPage()

        with marketTab:
            _ = MarketPage()

        with economyTab:
            _ = EconomyPage()