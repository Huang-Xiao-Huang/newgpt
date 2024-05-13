from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


#聊天机器人模型
memory = ConversationBufferMemory(return_messages=True)
# memory = ConversationSummaryBufferMemory(max_token_limit=1000,return_messages=True)
def get_chat_response(prompt,openai_api_key):
    #模型
    model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key,
                                           openai_api_base="https://api.aigc369.com/v1")
    #记忆
    chain = ConversationChain(llm=model,memory=memory)
    #调用链
    response = chain.invoke({"input":prompt})

    return response



def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key,
                       openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return  response["response"]





if __name__ == "__main__":
    memory = ConversationBufferMemory(return_messages=True)
    ai_answer = get_chat_response("月亮什么时候最圆？",  "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c")
    print(ai_answer)
    print(get_chat_response("我刚才问了什么问题", "sk-8DdVVv5xOLRoSdLN5d1274Dc70514a40Be4684F7C152F04c"))
