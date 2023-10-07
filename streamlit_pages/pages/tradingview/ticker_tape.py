import streamlit.components.v1 as components


def ticker_tape():

    components.html(
        """
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
        {
        "symbols": [
            {
            "proName": "FOREXCOM:SPXUSD",
            "title": "S&P 500"
            },
            {
            "proName": "FOREXCOM:NSXUSD",
            "title": "US 100"
            },
            {
            "description": "Crude Oil",
            "proName": "NYMEX:CL1!"
            },
            {
            "description": "Gold",
            "proName": "COMEX:GC1!"
            },
            {
            "description": "Bitcoin",
            "proName": "BINANCE:BTCUSDT"
            },
            {
            "description": "",
            "proName": "NASDAQ:AAPL"
            },
            {
            "description": "",
            "proName": "NASDAQ:MSFT"
            },
            {
            "description": "",
            "proName": "NASDAQ:GOOGL"
            }
        ],
        "showSymbolLogo": true,
        "colorTheme": "dark",
        "isTransparent": true,
        "displayMode": "adaptive",
        "locale": "en"
        }
        </script>
        </div>
        """
    )