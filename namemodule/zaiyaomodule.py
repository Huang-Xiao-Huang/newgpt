
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


system_template_text = """
你是评论家，请你遵循以下步骤进行创作：
总结文档，要求输出的格式为三个部分：主题 + 中心思想 + 反思，每个部分都要加上适当的emoji表情
{parser_instructions}
"""



def Sumary(file_contents, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,openai_api_base="https://api.aigc369.com/v1")
    chain = prompt | model
    result = chain.invoke({
        "parser_instructions": file_contents,

    })

    return result.content

