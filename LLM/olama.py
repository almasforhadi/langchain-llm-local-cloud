# https://docs.langchain.com/oss/python/integrations/providers/ollama
# ollama pull llama3

from langchain_community.chat_models import ChatOllama

model = ChatOllama(model="llama3")

response = model.invoke("Why do parrots talk?")
print(response.content)
