import os
import textwrap
import langchain
from langchain.memory import ChatMessageHistory,ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate

from langchain import HuggingFaceHub

import os
import requests
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm=HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature":0.5, "max_length":1024})

def print_response(response:str):
    print(textwrap.fill(response,width=1024))

history=ChatMessageHistory()
memory = ConversationBufferMemory(chat_memory=history)


context= """The Idrisid dynasty was a Muslim polity centered in Morocco, which ruled from 788 to 974. Named after the founder Idriss I,
the great-grandchild of Hasan ibn Ali, the Idrisids are believed by some historians to be the founders of the first Moroccan state"""
template = "Context : \n "+ context + """
 
Conversation: {history}

User: {input}

Bot : """


PROMPT = PromptTemplate(input_variables=['history','input'],template=template)
conversation = ConversationChain(prompt=PROMPT,llm=llm,verbose=True,memory=ConversationBufferMemory(ai_prefix='AI'))

def conv(prompt):
    prompt= prompt
    print()
    result=conversation(prompt)
    print_response("result: "+result['response'])
    return f"Bot: {result['response']}"