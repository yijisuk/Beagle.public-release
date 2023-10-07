import plotly.graph_objects as go
from plotly.subplots import make_subplots

from common_utils.visualization.gauge import gauge


class TechnicalsEvaluationFormatter:

    def __init__(self, ticker, data):

        self.ticker = ticker

        if data is not None:

            self.osc_score = data.loc["oscillator_score"]
            self.osc_decision = data.loc["oscillator_decision"]

            osc_strong_buy_count = data.loc["oscillator_strong_buy_count"]
            osc_buy_count = data.loc["oscillator_buy_count"]
            osc_neutral_count = data.loc["oscillator_neutral_count"]
            osc_sell_count = data.loc["oscillator_sell_count"]
            osc_strong_sell_count = data.loc["oscillator_strong_sell_count"]

            self.osc_counts = [
                osc_strong_buy_count, osc_buy_count,
                osc_neutral_count,
                osc_sell_count, osc_strong_sell_count
            ]

            self.ma_score = data.loc["moving_average_score"]
            self.ma_decision = data.loc["moving_average_decision"]

            ma_strong_buy_count = data.loc["moving_average_strong_buy_count"]
            ma_buy_count = data.loc["moving_average_buy_count"]
            ma_neutral_count = data.loc["moving_average_neutral_count"]
            ma_sell_count = data.loc["moving_average_sell_count"]
            ma_strong_sell_count = data.loc["moving_average_strong_sell_count"]

            self.ma_counts = [
                ma_strong_buy_count, ma_buy_count,
                ma_neutral_count,
                ma_sell_count, ma_strong_sell_count
            ]

            self.invalid = False

        else:
            self.invalid = True


    def visualize_technicals(self):

        if self.invalid:
            return None

        ### Technicals Score
        
        osc_gauge = gauge(value=self.osc_score, range=[-22, 22])
        ma_gauge = gauge(value=self.ma_score, range=[-38, 38])

        ### Technicals Count
        labels = [
            "Strong Buy", "Buy",
            "Neutral",
            "Sell", "Strong Sell"
        ]

        osc_bar = go.Bar(x=labels, y=self.osc_counts)
        ma_bar = go.Bar(x=labels, y=self.ma_counts)

        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{'type': 'indicator'}, {'type': 'indicator'}],
                [{'type': 'xy'}, {'type': 'xy'}]],
            subplot_titles=("Oscillator Score", "Moving Average Score",
                "Oscillator Evaluations in Detail", 
                "Moving Average Evaluations in Detail"),
            vertical_spacing=0.1,
        )

        fig.add_trace(osc_gauge, row=1, col=1)
        fig.add_trace(ma_gauge, row=1, col=2)

        fig.add_trace(osc_bar, row=2, col=1)
        fig.add_trace(ma_bar, row=2, col=2)

        fig.update_layout(
            showlegend=False,
            margin=dict(t=50, b=50, l=50, r=50),
            width=1200, height=800
        )

        return fig