import streamlit as st
import streamlit.components.v1 as components


def forex_heatmap(height=500):

    st.header("Forex Heatmap 🌡️")

    components.html(
        html=f"""
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-forex-heat-map.js" async>
        {{
        "width": "100%",
        "height": "{height}",
        "currencies": [
            "EUR",
            "USD",
            "JPY",
            "GBP",
            "CNY",
            "HKD",
            "SGD",
            "KRW"
        ],
        "isTransparent": true,
        "colorTheme": "dark",
        "locale": "en"
        }}
        </script>
        </div>
        """,
        height=height
    )