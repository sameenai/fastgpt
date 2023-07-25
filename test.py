from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
import sys


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=api_key)
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
question = input("Please enter a question: ")

print(llm_chain.run(question))
