import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
OPENAI_API_BASE=os.environ["OPENAI_API_BASE"] 
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"] 

from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from .extraction import extract_community_name
from ..models import search_community_info_by_name
import base64



PDF_NAME = 'application\static\社团信息库.pdf'
docs = PyMuPDFLoader(PDF_NAME).load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(docs)


embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(split_docs, embeddings, collection_name="serverless_guide")


llm = ChatOpenAI(temperature=0)
chain = load_qa_chain(llm, chain_type="stuff",verbose=True)

def search_recommend(human_input):
    query = human_input
    similar_docs = vectorstore.similarity_search(query, 3)
    res=chain.run(input_documents=similar_docs, question=query)
    community_name = extract_community_name(res)
    # print(community_name)
    try:
        if community_name is not None:
            community_info = search_community_info_by_name({'name':community_name[0]['communityName']})
            if community_info is not None:
                if community_info['image'] is not None:
                    community_info['image'] = base64.b64encode(community_info['image']).decode('utf-8')
                return {"res":res,'communityInfo':community_info}
    except Exception as e:
            print(e)
            return {"res":res,'communityInfo':None}
