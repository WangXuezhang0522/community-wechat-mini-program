import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
OPENAI_API_BASE=os.environ["OPENAI_API_BASE"] 
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"] 

from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import (
    PromptTemplate,
)

# Run chain
llm = ChatOpenAI(
                temperature=0, model="gpt-3.5-turbo"
)


def extract_community_name(res:str):
    prompt = PromptTemplate(
    template="分析出\n{res}\n中的第一个社团名称,例如'communityName:'羽毛球俱乐部','\n",
    input_variables=["res"],
    )
    # Schema
    schema = {
        "properties": {
            "communityName": {"type": "string"},
        },
        "required": ["communityName"],
    }
    chain = create_extraction_chain(schema, llm, prompt,verbose=True)
    return chain.run(res)


