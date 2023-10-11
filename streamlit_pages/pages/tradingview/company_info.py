import streamlit as st
import streamlit.components.v1 as components


class CompanyInfo:

    def __init__(self, exchange, ticker, theme):

        self.exchange = exchange
        self.ticker = ticker

        self.stock_price_widget()
        self.company_financials_widget()

    
    def stock_price_widget(self, height=500, ma_length=20):

        components.html(
            html=f"""
            <!-- TradingView Widget BEGIN -->
            <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
            {{
            "symbols": [
                [
                "{self.exchange}:{self.ticker}|1D"
                ]
            ],
            "chartOnly": false,
            "width": "100%",
            "height": "{height}",
            "locale": "en",
            "colorTheme": "{st.get_option("theme.base").lower()}",
            "autosize": true,
            "showVolume": true,
            "showMA": true,
            "hideDateRanges": false,
            "hideMarketStatus": false,
            "hideSymbolLogo": false,
            "scalePosition": "right",
            "scaleMode": "Normal",
            "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
            "fontSize": "10",
            "noTimeScale": false,
            "valuesTracking": "1",
            "changeMode": "price-and-percent",
            "chartType": "area",
            "maLineColor": "#2962FF",
            "maLineWidth": 1,
            "maLength": {ma_length},
            "lineWidth": 2,
            "lineType": 0,
            "dateRanges": [
                "1d|1",
                "1m|30",
                "3m|60",
                "12m|1D",
                "60m|1W",
                "all|1M"
            ]
            }}
            </script>
            </div>
            <!-- TradingView Widget END -->
            """,
            height=height
        )


    def company_financials_widget(self, height=1000):

        components.html(
            html=f"""
            <!-- TradingView Widget BEGIN -->
            <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
            {{
            "colorTheme": "dark",
            "isTransparent": true,
            "largeChartUrl": "",
            "displayMode": "regular",
            "width": "100%",
            "height": "{height}",
            "symbol": "{self.exchange}:{self.ticker}",
            "locale": "en"
            }}
            </script>
            </div>
            <!-- TradingView Widget END -->
            """,
            height=height
        )