# Beagle 🐶
Beagle provides tailored market data analysis to simplify market entry for individual investors.

<img src="https://github.com/yijisuk/Beagle.public-release/assets/63234184/1c2a49be-12a1-4290-9fb8-26636820390c" alt="Demo" width="100%">

Watch our presentation [here.](https://youtu.be/O3Ava2ebgaU)

## Our Solutions
### 1️⃣ Company financials analysis & evaluation

Complex market analysis tasks are automated to present essential insights about any company.

The process begins with a comprehensive assessment of a company's financial statements. Our internal algorithm extracts essential data from income, balance, and cashflow statements, then calculates ratio metrics. These metrics are used to provide an objective score on the company's financial state, based on predefined classifications: Liquidity, Operation Efficiency, Profitability, Business Stability, Financial Stability, Overall Stability, and Valuation.

The organized evaluation scores are integrated with the GPT-4 Large Language Model (LLM), providing a comprehensive evaluation.

### 2️⃣ Market screener

Investment success depends on both identifying companies with solid financials and gauging the optimal market entry time. 

The TradingView widget is incorporated to display a live daily market heatmap, showcasing the most recent market changes.
  
### 3️⃣ Economy overview

Understanding the broader economic landscape is vital, as economic conditions significantly dictate the flow of money. Insights are primarily derived from [JPMorgan Asset Management](https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/economic-update/)'s weekly reports, providing a succinct weekly summary of economic evaluations. 

Additionally, TradingView widgets for the economic calendar and forex heatmap are integrated for a more rounded perspective.

## Accessing the Demo
### 🌐 Public Web App

Easy access can be done through accessing the [public web app](https://beagle.streamlit.app/), powered by [Streamlit](https://streamlit.io/). 

You can also access it by scanning the QR code below 👇

<img src="https://github.com/yijisuk/Beagle.public-release/assets/63234184/afcc771c-06d4-4c8a-8ec8-9e4afb4f4b6f" alt="QR" width="250" height="250"/>

### 🖥️ Run the repo locally
1. Clone the repository: ```git clone https://github.com/yijisuk/Beagle.public-release.git```
2. Create an Anaconda virtual environment and activate it: <br>```conda create --name beagle python=3.10``` <br>```conda activate beagle```
3. Install the dependencies: ```pip install -r requirements.txt```
4. Create a file ```secrets.toml``` inside the folder ```.streamlit```. The path should be: ```./streamlit/secrets.toml```
5. Visit the [OpenAI API Platform](https://platform.openai.com/) and create an API key.
6. Save the created API key in ```secrets.toml```. Should follow the given format: ```openai_api_key = "OPENAI-API-KEY"```
7. Open a new terminal window in the project directory ```./Beagle.public-release```, then run the Streamlit command to run the web app: ```streamlit run main.py```

## File Descriptions
The dataset used for this application can be accessed on ```./data_storage```.
- ```ticker_data_sample.csv```: Holds the quantitative evaluation data of companies, processed by our internal algorithm.
- ```economy_evaluation.csv```: Holds the literary data on economic climate evaluation.
