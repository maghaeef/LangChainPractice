# setting up the environment -> openai api key
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_restaurant_name_and_items(cuisine):
    llm = OpenAI(temperature=0.6)

    # name prompt template
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fency name for this.")

    # items prompt template
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest some menu items for {restaurant_name}. Return it as comma separated list.'
    )

    # chains
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name') # output_key is added
    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='items')         # output_key is added

    # sequential chain
    chain = SequentialChain(chains=[name_chain, items_chain], 
                            input_variables=['cuisine'], 
                            output_variables=['restaurant_name', 'items'])

    return chain({'cuisine':cuisine})


if __name__=="__main__":
    print(generate_restaurant_name_and_items("Persian"))