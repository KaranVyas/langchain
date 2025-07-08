from pydantic.v1 import BaseModel
from langchain_community.llms import Ollama

LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="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"
LANGSMITH_PROJECT="pr-blank-hermit-52"

llm=Ollama(model="llama3.2")
llm.invoke("Hello, world!")