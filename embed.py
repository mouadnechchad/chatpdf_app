import json
from langchain.embeddings import HuggingFaceEmbeddings
from huggingface_hub import hf_hub_download
import pinecone
from langchain.vectorstores import Pinecone

path="/Users/medmachrouh/Desktop/PFA/index_2.json"
with open(path) as json_file:
    data1 = json.load(json_file)
json_file.close()

def get_chunk(query):
    index_name = 'pfa'

    pinecone.init(
            api_key="a51028e8-8d2f-436d-b346-0b090cc3de08",  # find api key in console at app.pinecone.io
            environment="asia-southeast1-gcp-free"  # find next to api key in console
    )

    hf_embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/gtr-t5-large')

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

    docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)

    docs = docsearch.similarity_search(query,k=1)

    for t in metadatas:
        if docs[0].page_content==t['content']:
            print(docs[0].page_content,t['source'],t['page_number'])

    return docs[0].page_content,t['source'],t['page_number']