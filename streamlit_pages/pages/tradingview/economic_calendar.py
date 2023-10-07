import streamlit as st
import streamlit.components.v1 as components


def economic_calendar(height=800):

    st.header("Economic Calendar 🗓️")

    components.html(
        html=f"""
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
        {{
        "width": "100%",
        "height": "{height}",
        "colorTheme": "dark",
        "isTransparent": true,
        "locale": "en",
        "importanceFilter": "0,1",
        "currencyFilter": "USD,CNY,EUR,JPY"
        }}
        </script>
        </div>
        """,
        height=height
    )