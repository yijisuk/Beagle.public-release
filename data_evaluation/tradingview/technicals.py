import streamlit.components.v1 as components


def technicals(ticker, exchange, height=500):

    components.html(
        html=f"""
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {{
        "interval": "1D",
        "width": "100%",
        "isTransparent": true,
        "height": "{height}",
        "symbol": "{exchange}:{ticker}",
        "showIntervalTabs": true,
        "locale": "en",
        "colorTheme": "dark"
        }}
        </script>
        </div>
        """,
        height=height,
    )