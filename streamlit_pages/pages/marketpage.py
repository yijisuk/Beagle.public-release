import streamlit as st

from ..base.basepage import BasePage
from .tradingview.market_news_timeline import market_news_timeline
from ..pages.tradingview.heatmap import heatmap



class MarketPage(BasePage):

    def __init__(self):

        super().__init__()

        st.title("Market Overview 📰")
        heatmapCol, newsCol = st.columns(2, gap="medium")

        with heatmapCol:
            heatmap()

        with newsCol:
            market_news_timeline()