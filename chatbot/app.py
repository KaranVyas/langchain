from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

## LANGSMITH TRACKING
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You're a helpful assistant. Please provide answer to the user's queries"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo using OLLAMA LLAMA2 API")
input_text=st.text_input("Chat here ")

##OLLAMA LLAMA3.2 LLM
llm=Ollama(model="llama3.2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))