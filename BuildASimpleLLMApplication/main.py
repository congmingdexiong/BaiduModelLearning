import os

import qianfan
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import QianfanLLMEndpoint
from langchain_core.messages import HumanMessage, SystemMessage
os.environ["QIANFAN_AK"] = os.getenv('baiduERNIE_KEY')
os.environ["QIANFAN_SK"] = os.getenv('baiduERNIE_SECRET')

model = QianfanLLMEndpoint(temperature=0.9)
#
# text = "对于一家生产彩色袜子的公司来说，什么是一个好的公司名称?"
# print(model.invoke(text))



messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

# print(model.invoke("Hello"))
# print(model.invoke([{"role": "user", "content": "Hello"}]))
# print(model.invoke([HumanMessage("Hello")]))

# streaming
for token in model.stream(messages):
    print(token, end="|")


# from langchain_core.prompts import ChatPromptTemplate
#
# system_template = "Translate the following from English into {language}"
#
# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", system_template), ("user", "{text}")]
# )
#
# prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})
#
# response = model.invoke(prompt)
# print(response)



# message = {
#   "messages": [
#     {"role":"user","content":"介绍一下北京"}
#    ]
# }
# resp = qianfan.ChatCompletion().do(endpoint="completions_pro", temperature=0.95, top_p=0.8, penalty_score=1, enable_system_memory=False, disable_search=False, enable_citation=False,messages=message.get("messages"))
# print(resp.body)