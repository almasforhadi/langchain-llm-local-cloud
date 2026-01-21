# https://docs.langchain.com/oss/python/langchain/models
# pip install langchain langchain-openai


import os
from langchain.chat_models import init_chat_model

os.environ["OPENAI_API_KEY"] = "sk-..."

model = init_chat_model("gpt-4.1")

response = model.invoke("Why do parrots talk?")
print(response)