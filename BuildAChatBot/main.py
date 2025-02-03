import os

import qianfan
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import QianfanLLMEndpoint
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

os.environ["QIANFAN_AK"] = os.getenv('baiduERNIE_KEY')
os.environ["QIANFAN_SK"] = os.getenv('baiduERNIE_SECRET')

model = QianfanLLMEndpoint(temperature=0.9)


data = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

print(data)