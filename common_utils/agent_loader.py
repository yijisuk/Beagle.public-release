import streamlit as st
from langchain.chat_models import ChatOpenAI
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from polygon import RESTClient
import streamlit as st

from streamlit_pages.stream_display_handler import StreamDisplayHandler


class AgentLoader:

    def __init__(self):

        self.openai_api_key = st.secrets["openai_api_key"]


    def load_openai_agent(self, model="gpt-4"):

        if model == "gpt-3.5":
            gpt_model = ChatOpenAI(
                temperature=0, 
                model_name="gpt-3.5-turbo-16k", 
                openai_api_key=self.openai_api_key
            )
        
        elif model == "gpt-4":
            gpt_model = ChatOpenAI(
                temperature=0, 
                model_name="gpt-4", 
                openai_api_key=self.openai_api_key
            )
            
        return gpt_model


    def load_streaming_openai_agent(self, model="gpt-4"):

        chat_box = st.empty()
        display_handler = StreamDisplayHandler(chat_box, display_method='write')

        if model == "gpt-3.5":
            gpt_model = ChatOpenAI(
                temperature=0, 
                model_name="gpt-3.5-turbo-16k", 
                openai_api_key=self.openai_api_key,
                streaming=True, 
                callbacks=[display_handler])
            
        elif model == "gpt-4":
            gpt_model = ChatOpenAI(
                temperature=0, 
                model_name="gpt-4", 
                openai_api_key=self.openai_api_key,
                streaming=True, 
                callbacks=[display_handler])
            
        return gpt_model