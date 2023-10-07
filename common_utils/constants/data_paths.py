import os


class DataPaths:

    base_path = "data_storage"

    # Finalized data paths
    organized_ticker_data_fn = os.path.join(base_path, "ticker_data_sample.csv")

    economy_eval_data_fn = os.path.join(base_path, "economy_evaluation.csv")