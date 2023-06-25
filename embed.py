import json
from langchain.embeddings import HuggingFaceEmbeddings
from huggingface_hub import hf_hub_download
import pinecone
from langchain.vectorstores import Pinecone
import cohere


def get_chunk(text):
    index_name = 'pfa'

    # pinecone.init(
    #         api_key="a51028e8-8d2f-436d-b346-0b090cc3de08",
    #         environment="asia-southeast1-gcp-free"
    # )
    pinecone.init(
        api_key="305ffee6-6327-4bd1-9196-f58b0b92574e",  # find api key in console at app.pinecone.io
        environment="northamerica-northeast1-gcp"  # find next to api key in console
    )

    index = pinecone.Index(index_name)

    co = cohere.Client('xwQEiqU1kYFXZxECK7aquQPyXDx9uUTU4j44pHB2')
    response = co.embed(
    model='embed-english-v2.0',
    texts=[text])

    print('___________')


    print(index.describe_index_stats())

    docs = index.query(response.embeddings, top_k=1, include_metadata=True)

    print(docs['matches'][0]['metadata']['content'])
    print("===============")
    # print(docs['matches'][1]['metadata']['content'])
    print("===============")
    # print(docs['matches'][2]['metadata']['content'])
    return docs['matches'][0]['metadata']['content'],docs['matches'][0]['metadata']['source'],int(docs['matches'][0]['metadata']['page_number'])