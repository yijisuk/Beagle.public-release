import json
from langchain.chains import LLMChain
from langchain.schema import HumanMessage

from common_utils.agent_loader import AgentLoader
from ..utils.constants import (
    FinancialsKeyValues as fkv,
    FinancialsSectionTitles as fst
)
from ..utils.llm_prompts import (
    FinancialsLLMPrompts, 
    LLMSummarizePrompts
)
from ..processors.financials_data_split import financials_data_split


class FinancialsEvaluationFormatter:

    def __init__(self, ticker, data):

        self.ticker = ticker
        self.data = financials_data_split(data)

        self.llmp = FinancialsLLMPrompts()
        self.base_eval_prompt, self.base_scoring_prompt = self.llmp.base_financials_eval_prompt()

        self.agentloader = AgentLoader()
        self.steaming_gpt_llm = self.agentloader.load_streaming_openai_agent(model="gpt-4")
        self.gpt_llm = self.agentloader.load_openai_agent(model="gpt-4")


    def base_evaluation(self, eval_prompt, scoring_prompt, section_title, section_column_name):

        if self.data[section_column_name] is None:
            return (None, None)
        
        eval = LLMChain.from_string(
            llm=self.gpt_llm, template=eval_prompt
        ).predict(
            section_title=section_title,
            data=self.data[section_column_name]
        )
        
        score = ""
        score_chain = LLMChain.from_string(
            llm=self.gpt_llm, template=scoring_prompt
        )

        while not score.isdigit():
            score = score_chain.predict(
                section_title=section_title,
                evaluation=eval
            )

        score = int(score)

        return (eval, score)


    def company_introduction(self):

        company_intro_prompt = self.llmp.company_intro_prompt(
            ticker=self.ticker,
            data=self.data[fkv.COMPANY_BASIC_DATA.value]
        )

        response = self.steaming_gpt_llm([HumanMessage(content=company_intro_prompt)])

        return response
    
    
    # Liquidity Ratio Evaluation
    def liquidity_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.LIQUIDITY_RATIO_EVAL.value,
            section_column_name=fkv.LIQUIDITY_RATIO_DATA.value
        )

        if None not in results:
            self.liquidity_evaluation_response = results[0]
        else:
            self.liquidity_evaluation_response = ""

        return results
    

    # Turnover Ratio Evaluation
    def turnover_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.TURNOVER_RATIO_EVAL.value,
            section_column_name=fkv.TURNOVER_RATIO_DATA.value
        )

        if None not in results:
            self.turnover_evaluation_response = results[0]
        else:
            self.turnover_evaluation_response = ""

        return results
    

    # Profitability Ratio Evaluation
    def profitability_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.PROFITABILITY_RATIO_EVAL.value,
            section_column_name=fkv.PROFITABILITY_RATIO_DATA.value
        )

        if None not in results:
            self.profitability_evaluation_response = results[0]
        else:
            self.profitability_evaluation_response = ""
    
        return results


    # Business Risk Ratio Evaluation
    def business_risk_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.BUSINESS_RISK_RATIO_EVAL.value,
            section_column_name=fkv.BUSINESS_RISK_RATIO_DATA.value
        )

        if None not in results:
            self.business_risk_evaluation_response = results[0]
        else:
            self.business_risk_evaluation_response = ""
    
        return results
    

    # Financial Risk Ratio Evaluation
    def financial_risk_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.FINANCIAL_RISK_RATIO_EVAL.value,
            section_column_name=fkv.FINANCIAL_RISK_RATIO_DATA.value
        )

        if None not in results:
            self.financial_risk_evaluation_response = results[0]
        else:
            self.financial_risk_evaluation_response = ""
    
        return results
    

    # Stability Ratio Evaluation
    def stability_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.STABILITY_RATIO_EVAL.value,
            section_column_name=fkv.STABILITY_RATIO_DATA.value
        )

        if None not in results:
            self.stability_evaluation_response = results[0]
        else:
            self.stability_evaluation_response = ""

        return results
    

    # Valuation Ratio Evaluation
    def valuation_evaluation(self):

        results = self.base_evaluation(
            eval_prompt=self.base_eval_prompt,
            scoring_prompt=self.base_scoring_prompt,
            section_title=fst.VALUATION_RATIO_EVAL.value,
            section_column_name=fkv.VALUATION_RATIO_DATA.value
        )

        if None not in results:
            self.valuation_evaluation_response = results[0]
        else:
            self.valuation_evaluation_response = ""

        return results


    def evaluate_financials(self):

        eval_agg = self.liquidity_evaluation_response \
            + self.turnover_evaluation_response \
            + self.profitability_evaluation_response \
            + self.business_risk_evaluation_response \
            + self.financial_risk_evaluation_response \
            + self.stability_evaluation_response \
            + self.valuation_evaluation_response
        
        return eval_agg


    def summarize_financials(self, response):

        llmsp = LLMSummarizePrompts()

        financials_key_points_extraction_prompt = llmsp.financials_prompt(option="key_points")
        kp_response = LLMChain.from_string(
            llm=self.gpt_llm,
            template=financials_key_points_extraction_prompt
        ).predict(response=response)


        financials_summary_prompt = llmsp.financials_prompt(option="summary")
        
        summary_response = ""
        summary_chain = LLMChain.from_string(
            llm=self.gpt_llm,
            template=financials_summary_prompt
        )

        while not is_dict_format(summary_response):
            summary_response = summary_chain.predict(response=kp_response)

        summary_response = json.loads(summary_response)
        formatted = (
            f"Strengths: {summary_response['strengths']}\n\n"
            f"Weaknesses: {summary_response['weaknesses']}"
        )

        return formatted
    

def is_dict_format(s):

    try:
        data = json.loads(s)
        return isinstance(data, dict)
    
    except json.JSONDecodeError:
        return False