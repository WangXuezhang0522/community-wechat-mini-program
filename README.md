## 介绍
一个基于小程序端和PC后台管理的社团管理系统，包含智能化的智能推荐功能、大模型智能审核社团帖子、数据展示功能、校-校联谊、社团企业联通、用户管理、搜索功能、社团活跃度数据统计分析等多项功能，以及为管理员提供社团信息审核、帖子审核、活动审核、用户管理等功能。
## 技术栈
- Flask
- LangChain
- MySQL
- 微信原生小程序
- React
## 效果图
<img height="200" src="https://github.com/WangXuezhang0522/image/blob/main/%E5%9B%BE%E5%BA%8A/%E5%9B%BE%E7%89%871.png?raw=true"><img height="200" src="https://github.com/WangXuezhang0522/image/blob/main/%E5%9B%BE%E5%BA%8A/%E5%9B%BE%E7%89%872.png?raw=true"><img height="200" src="https://github.com/WangXuezhang0522/image/blob/main/%E5%9B%BE%E5%BA%8A/%E5%9B%BE%E7%89%873.png?raw=true"><img height="200" src="https://github.com/WangXuezhang0522/image/blob/main/%E5%9B%BE%E5%BA%8A/%E5%9B%BE%E7%89%874.png?raw=true"><img height="200" src="https://github.com/WangXuezhang0522/image/blob/main/%E5%9B%BE%E5%BA%8A/%E5%9B%BE%E7%89%875.png?raw=true"><img height="200" src="https://github.com/WangXuezhang0522/image/blob/main/%E5%9B%BE%E5%BA%8A/%E5%9B%BE%E7%89%876.png?raw=true">

## 主要功能实现
- 智能推荐

为大语言模型建立一个社团信息外挂知识库，将外挂知识库进行向量化存储到Chroma向量数据库中，将大语言模型作为驱动对外挂知识库进行相似性检索形成一个基于本地知识库的问答功能。结合大语言模型出色的语言处理能力以及答案来自本地知识库的准确性，将回答内容锁定为用户希望的结果。再对回答内容进行数据抽取，将自然语言进行结构化处理，让它能够作为参数进行MySQL数据库检索，得到关于这个社员的自然语言描述以及数据库中的相关全部信息。

- 智能审核

ReActAgent是一个能感知并自主地采取行动的实体，这里的自主性极其关键，Agent要能够实现设定的目标，其中包括具备学习和获取知识的能力以提高自身性能。大语言模型的出现同样将Agent推向了一个新的高度。
Agent= LLM（思考决策）+ prompt(思维链) + memory（记忆）+ tools(执行)
通过ReActAgent使用大语言模型作为驱动，进行推理和思考。对于社团信息的审核，定义好Agent的角色，使其成为一个审核发言内容的审核Agent。ToolCalling可做为一个可调用的工具配备给Agent，定义好两个审核的工具（审核通过与审核未通过），将发言内容限制为包括但不限于:涉黄、涉政、涉暴,辱骂,色情引导等内容进行封禁。Agent的返回结果是一个结构化的数据，可直接作为参数使用进行MySQL数据库操作。

## 操作步骤
### 创建一个.env文件
内容为:
### 代理地址
OPENAI_API_BASE = ""
### 代理密钥
OPENAI_API_KEY = ""
### 创建知识库
1. 在application下创建一个static
2. 在static中创建一个base.pdf文件
    文件内容为社团信息
