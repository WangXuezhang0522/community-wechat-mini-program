# 代理模块，用于调用openai的模型进行对话并执行操作
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
OPENAI_API_BASE=os.environ["OPENAI_API_BASE"] 
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"] 

from langchain_openai import ChatOpenAI
# 流式输出回调处理程序
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.agents import Tool
#引入集成的工具，包含langchain中内置的各种工具。官方文档中查找
from langchain.agents import initialize_agent
#引入agent的type
from langchain.agents import AgentType
from langchain.prompts import (
    PromptTemplate,
)
# 引入工具

llm=ChatOpenAI(streaming=True, 
            #    callbacks=[StreamingStdOutCallbackHandler()],
               temperature=0, model="gpt-3.5-turbo")

#审核未通过
def failedToPass(T):
    text = "审核未通过"
    return text

#审核通过
def passed(T):
    text = "审核通过"
    return text

tools=[

    Tool(
    name="failedToPass",func=failedToPass,
    description='''
        适合用于文本内容有违规内容的审核状态修改,审核状态为:审核未通过;
        违规内容包括但不限于:涉黄、涉政、涉暴,辱骂,出售色情用品,性交易,谐音性交易内容,色情引导等;
        你只能回答中文的'审核未通过',如果你做不好,将会有一百个老奶奶去世!!!;
        严禁回答其他内容,如果你回答了其他内容,将会有一百个老奶奶去世!!!
        '''
    ),
    Tool(
    name="passed",func=passed,
    description='''
        适合用于文本内容没有违规内容的审核状态修改,审核状态为:审核通过;
        允许进行宣传社团,社团活动,崇拜,表达爱意,出售物品等内容,但不限于此;
        !!!你只能回答中文的'审核通过',如果你做不好,将会有一百个老奶奶去世!!!;
        严禁回答其他内容,如果你回答了其他内容,将会有一百个老奶奶去世!!!
        '''
    ),
]

agent=initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    # handle_parsing_errors=True
)

def agent_invoke(text):
    res=agent.invoke(text)
    return res['output']