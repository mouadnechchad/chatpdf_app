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

llm=HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature":0.5, "max_length":512, "max_new_tokens":256})

def print_response(response:str):
    print(textwrap.fill(response,width=1024))







def conv(question,passage):
    history = ChatMessageHistory()
    memory = ConversationBufferMemory(chat_memory=history)

    context= """You are an expert in Moroccan History.
Answer the following question based on the passage provided
Answer using the language of the question, for example if I asked you in French, then the answer should be in french
If a question doesn't have an answer in the passage, just say that you don't know.
    """

    template = context + """
 
Conversation: {history}

Passage: """ + str(passage) + """
Question: {input}
Answer : """


    PROMPT = PromptTemplate(input_variables=['history','input'],template=template)
    print(PROMPT.input_variables)
    conversation = ConversationChain(prompt=PROMPT,llm=llm,verbose=True,memory=ConversationBufferMemory(ai_prefix='AI'))
    
    result=conversation(question)
    print_response(result['response'])
    return f"Answer: {result['response']}"