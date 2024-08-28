## 介绍
一个基于小程序端和PC后台管理的社团管理系统，包含智能化的智能推荐功能、大模型智能审核社团帖子、数据展示功能、校-校联谊、社团企业联通、用户管理、搜索功能、社团活跃度数据统计分析等多项功能，以及为管理员提供社团信息审核、帖子审核、活动审核、用户管理等功能。
## 技术栈
- Flask
- LangChain
- MySQL
- 微信原生小程序
- React
## 效果图
<img height="200" src="https://raw.githubusercontent.com/WangXuezhang0522/picture-Repository/ec87a2fbee5009be1698d918d05fe598a2b512c5/image/%E5%9B%BE%E7%89%871.png?token=AYG6CNEUTK6LFB7LMY2REJTGZ3ALQ"><img height="200" src="https://raw.githubusercontent.com/WangXuezhang0522/picture-Repository/ec87a2fbee5009be1698d918d05fe598a2b512c5/image/%E5%9B%BE%E7%89%872.png?token=AYG6CNBV73Q6UXAVQPMJFELGZ3ALQ"><img height="200" src="https://raw.githubusercontent.com/WangXuezhang0522/picture-Repository/ec87a2fbee5009be1698d918d05fe598a2b512c5/image/%E5%9B%BE%E7%89%873.png?token=AYG6CNHUMTKEIGBDT7M3DSLGZ3ALQ"><img height="200" src="https://raw.githubusercontent.com/WangXuezhang0522/picture-Repository/ec87a2fbee5009be1698d918d05fe598a2b512c5/image/%E5%9B%BE%E7%89%874.png?token=AYG6CNALGPPBW5LS63IB7FTGZ3ALQ"><img height="200" src="https://raw.githubusercontent.com/WangXuezhang0522/picture-Repository/ec87a2fbee5009be1698d918d05fe598a2b512c5/image/%E5%9B%BE%E7%89%875.png?token=AYG6CNC4U5JRSGE3LAIQDRTGZ3ALQ"><img height="200" src="https://raw.githubusercontent.com/WangXuezhang0522/picture-Repository/ec87a2fbee5009be1698d918d05fe598a2b512c5/image/%E5%9B%BE%E7%89%876.png?token=AYG6CNABAHNGVDDVOZZZW2DGZ3ALQ">
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
