#paf 回答
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
#txt回答
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import TextLoader


import  tempfile


def pdf_agent(api_key, memory, uploaded_file, question):
    #读取PDF 文档
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key,
                       openai_api_base="https://api.aigc369.com/v1")
    file_content = uploaded_file.read()
    temp_file_path = "temp.pdf"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(file_content)
    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n", "。", "！", "？", "，", "、", ""]
    )
    texts = text_splitter.split_documents(docs)
    embeddings_model = OpenAIEmbeddings(openai_api_base="https://api.aigc369.com/v1",
                                        openai_api_key=api_key)
    db = FAISS.from_documents(texts, embeddings_model)
    retriever = db.as_retriever()
    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=retriever,
        memory=memory
    )
    response = qa.invoke({"chat_history": memory, "question": question})
    return response


#
def pdf_anwser(subject,question,api_key):
    #处理PDF文档
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", f"请你读完这篇论文:'{subject}',请用论文的原文回答问题'{question}'")
        ]
    )

    model = ChatOpenAI(openai_api_key=api_key, temperature=0,
                                            openai_api_base="https://api.aigc369.com/v1"
                       )

    title_chain = title_template | model
    content = title_chain.invoke({"subject": subject,"question":question}).content
    # script = script_chain.invoke({"title": title, "duration": video_length, "wikipedia_search": search_result}).content
    return content

def txt_answer(api_key, memory1, uploaded_file, question):
    #读取txt文档
    content_bytes = uploaded_file.read().decode('utf-8')
    # 假设我们想要保存上传的内容到服务器的某个文件中
    server_file_path = "uploaded_content.txt"
    # 写入内容到服务器的文件系统中
    with open(server_file_path, "w", encoding="utf-8") as f:
        f.write(content_bytes)
    loader = TextLoader(server_file_path, encoding="utf-8")
    docs = loader.load()
    #长文本分词
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=40,
        separators=["\n", "。", "！", "？", "，", "、", ""]
    )
    print(text_splitter)
    texts = text_splitter.split_documents(docs)
    embeddings_model = OpenAIEmbeddings(openai_api_base="https://api.aigc369.com/v1",
                                        openai_api_key=api_key)
    # 词向量库
    db = FAISS.from_documents(texts, embeddings_model)
    print(db)
    retriever = db.as_retriever()

    # openai模型
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       openai_api_key=api_key,
                       openai_api_base="https://api.aigc369.com/v1"
                       )

    memory = ConversationBufferMemory(return_messages=True, memory_key='chat_history', output_key='answer')

    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=retriever,
        memory=memory1
    )

    # questions = question
    # data = qa.invoke({"chat_history": memory, "question": questions})
    # print(data["answer"])
    # return data["answer"]
    response = qa.invoke({"chat_history": memory, "question": question})
    return response
