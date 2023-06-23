import json
from langchain.embeddings import HuggingFaceEmbeddings
from huggingface_hub import hf_hub_download
import pinecone
from langchain.vectorstores import Pinecone
import requests
import cohere


path="/Users/medmachrouh/Desktop/PFA/index_2.json"
with open(path) as json_file:
    data1 = json.load(json_file)
json_file.close()

def get_chunk(text):
    index_name = 'pfa'

    pinecone.init(
            api_key="a51028e8-8d2f-436d-b346-0b090cc3de08",  # find api key in console at app.pinecone.io
            environment="asia-southeast1-gcp-free"  # find next to api key in console
    )

    index = pinecone.Index(index_name)

    co = cohere.Client('xwQEiqU1kYFXZxECK7aquQPyXDx9uUTU4j44pHB2') # This is your trial API key
    response = co.embed(
    model='embed-multilingual-v2.0',
    texts=[text])
    # hf_embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/gtr-t5-large')

    # API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/gtr-t5-large"
    # headers = {"Authorization": "Bearer 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"}

    # def query(payload):
    #     response = requests.post(API_URL, headers=headers, json=payload)
    #     return response.json()
        
    # output = query({
    #     "inputs": {
    #         "source_sentence": text,
    #         "sentences":[text]
    #     },
    # })


    print('___________')



    batch_limit = 100
    metadatas = []

    with open(path) as json_file:
        data = json.load(json_file)
        for item in data:
            metadata = {
            'source': item['filename'],
            'page_number': item['page_number'],
            'content':item['content']
                }
            metadatas.append(metadata)

    json_file.close()

    print(index.describe_index_stats())

    # vectorstore = Pinecone(index,hf_embeddings.embed_query, [t['content'] for t in metadatas])

    # docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=output)

    docs = index.query(response.embeddings, top_k=1, include_metadata=True)

    return docs['matches'][0]['metadata']['content'],docs['matches'][0]['metadata']['source'],int(docs['matches'][0]['metadata']['page_number'])