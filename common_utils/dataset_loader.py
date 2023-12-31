import pandas as pd

from .constants.data_paths import DataPaths as dp


class DatasetLoader():

    def __init__(self):
        
        self.ticker_data = self.load_organized_ticker_data()
        self.economy_eval_data = self.load_economy_eval_data()

        self.tickers = self.ticker_data["ticker"].tolist()
        self.company_names = self.ticker_data["company_name"].tolist()

        self.company_list = [f"{ticker}: {company_name}" for ticker, company_name in zip(self.tickers, self.company_names)]


    def load_organized_ticker_data(self):

        return pd.read_csv(dp.organized_ticker_data_fn)
        

    def load_economy_eval_data(self):

        return pd.read_csv(dp.economy_eval_data_fn)