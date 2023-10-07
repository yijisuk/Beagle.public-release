import streamlit as st

from ..base.basepage import BasePage
from ..pages.tradingview.economic_calendar import economic_calendar
from ..pages.tradingview.forex_heatmap import forex_heatmap


class EconomyPage(BasePage):

    def __init__(self):

        super().__init__()
        economyReviewCol, economyCalendarCol = st.columns(2, gap="medium")


        with economyReviewCol:
            st.title("This Week's Economy 🤔")

            data = self.datasetloader.economy_eval_data

            for column in data.columns:

                title = ' '.join(word.capitalize() for word in column.split())
                st.subheader(title)
                st.write(data[column].iloc[0])


        with economyCalendarCol:
            economic_calendar()
            forex_heatmap()