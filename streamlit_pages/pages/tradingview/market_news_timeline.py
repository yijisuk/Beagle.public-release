import streamlit as st
import streamlit.components.v1 as components


def market_news_timeline(height=750):

    components.html(
        html=f"""
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
        {{
        "feedMode": "market",
        "market": "stock",
        "colorTheme": "dark",
        "isTransparent": true,
        "displayMode": "regular",
        "width": "100%",
        "height": "{height}",
        "locale": "en"
        }}
        </script>
        </div>
        """,
        height=height,
    )