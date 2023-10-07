from langchain.callbacks.base import BaseCallbackHandler


class StreamDisplayHandler(BaseCallbackHandler):

    def __init__(self, container, initial_text="", display_method='markdown'):

        self.container = container
        self.text = initial_text
        self.display_method = display_method
        self.new_sentence = ""


    def on_llm_new_token(self, token: str, **kwargs) -> None:

        self.text += token
        self.new_sentence += token

        display_function = getattr(self.container, self.display_method, None)

        if display_function is not None:
            display_function(self.text)
        else:
            raise ValueError(f"Invalid display_method: {self.display_method}")
        

    def on_llm_end(self, response, **kwargs) -> None:
        self.text=""