class FinancialsLLMPrompts:

    def __init__(self):
        pass

    
    def company_intro_prompt(self, ticker, data):

        prompt = (
            "You are a professional market analyst at Wall Street. "
            f"Given are the basic information about the company's stock {ticker}."
            f"\n{data}\n"
            "Elaborate this information to form 2-3 sentences that can "
            "help the investors to understand about the company, "
            "Use all the information given, especially the market cap and weight "
            "(express this is percentage format, up to 2 decimal points),"
            "and make sure to provide a logical explanation, "
            "before diving into the details. "
            f"Make sure to start the introduction with the company's ticker: {ticker}. "
            "Good to include the company's name, if you have the information. Otherwise, don't.\n"
        )

        return prompt


    def base_financials_eval_prompt(self):

        data_eval_prompt = (
            "DESCRIPTION: \n"
            "Here are more detailed data on the company's financials: "
            "This section holds the company's {section_title}.\n"


            "INSTRUCTION: \n"
            "Given the data, derive an insight that can help the investors to understand "
            "about the company's financials and make wise investment decisions. "
            "The overall evaluation should consist 3-4 sentences, "
            "- No need for introductions like: "
            "'Based on the given data,...', 'From the evaluation data,...', etc. "
            "Just go straight to the point.\n"
            

            "YOU MUST: \n"
            "- Make sure to provide a logical explanation on your evaluation.\n"
            "- Make sure to go through all individual sections throughout the entire given data.\n"
            "- In the evaluation, do also provide a brief description on the ratio, "
            "specifically on what aspect of the company it indicates.\n"
            "- Make sure the evaluation is delivered on the third person's perspective. "
            
            
            "YOU MUST NOT: \n"
            "- Do not mention the given numbers like '1.0'and '0.0', "
            "but just provide the evaluations verbally.\n"
            "- Do not mention any column names from the given data.\n"


            "NOTE THAT: \n"
            "- The given numbers are not the actual ratio values, "
            "but instead are BOOLEAN VALUES indicating the evaluation on that ratio. "
            "It only tells whether the company is doing well or not in that aspect, "
            "but not whether the ratio is high or low.\n"
            "- Some sections include a NULL value, which means that the data is not available. \n"

            "Here is the data: \n"
            "{data}"
        )

        scoring_prompt = (
            "Given is the evaluation on the company's {section_title}. "
            "Based on the evaluation, give a score "
            "where the minimum score is 0 and the maximum score is 5."
            "How much would you rate the company? "
            "Return the score in the format of an integer. "
            "No need to return any explanation. "
            "Here is the evaluation: \n"
            "{evaluation}"
        )

        return (data_eval_prompt, scoring_prompt)


class LLMSummarizePrompts:

    def __init__(self):

        pass

    
    def financials_prompt(self, option):

        if option == "key_points":

            PROMPT_TEMPLATE = (
                "Given the full evaluation on a company's financial statement, "
                "pull out the key highlights, max three bullet points, "
                "where each bullet point contains a max of 5 words. "
                "Focus the scope on what the company excels at, "
                "and what needs improvement. Make sure to mention profitability. "
                "Strengths and Weaknesses, max three bullet points each. "
                "No need to return any explanation. "
                "Return in the format of: "
                "'Strengths: ...', 'Weaknesses: ...'. \n"
                "{response}"
            )

        elif option == "summary":

            PROMPT_TEMPLATE = (
                "Now, reformat the strengths and weaknesses, "
                "each into a simple 2 sentences evaluation. "
                "Should be easy for the general public to comprehend. "
                "However, use the essential financial terms, but not too complicated. "
                "For example, 'money' may be a too vague concept. "
                "Instead, use 'cash' or 'profit', depending on relevancy. "
                "No need for additional explanation. "
                "Take out the company name, unify it into 'the company' "
                "if mentioning its name is needed. "
                "Take out the filling words or any unnecessary adjectives. "
                "Let's keep it super simple."
                "Return in the format of a dictionary, where the keys are "
                "'strengths' and 'weaknesses', "
                "and the values are the respective sentences."
                "Just return the dictionary. No need to return any explanation.\n"
                "{response}"
            )

        return PROMPT_TEMPLATE