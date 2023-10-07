import re


class Validator:

    def __init__(self, user_input, ticker_data):

        self.user_input = user_input
        self.ticker_data = ticker_data


    def preprocess(self, text):

        text = text.lower()
        # Remove non-alphabetic characters
        text = re.sub(r'[^a-z\s]', '', text)
        # Convert multiple spaces to a single space
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    
    def base_validation(self):

        query = self.preprocess(self.user_input)

        if query in self.ticker_data["ticker"].str.lower().values:
            return {
                "result": True,
                "ticker": query.upper(),
            }
        
        return {
            "result": False,
            "ticker": None,
        }