from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

#输入相关的文件
def translate_text(text_to_translate,source_lang,target_lang,model):

    text_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             f"""你是一位出色的翻译官。请翻译下列句子
             {text_to_translate}，
             要求：由{source_lang}翻译成{target_lang}，翻译的句子要准确
            """)
        ]
    )

    # model = ChatOpenAI(openai_api_key=api_key, openai_api_base="https://api.aigc369.com/v1")



    text_chain = text_template | model


    script = text_chain.invoke({"text_to_translate": text_to_translate, "source_lang": source_lang, "target_lang": target_lang}).content
    return script

