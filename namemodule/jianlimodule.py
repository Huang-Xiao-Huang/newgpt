from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

#书写简历的重功能


#简历模板
system_template_text = """
你是一个求职者，请你遵循以下步骤进行创作：
已知姓名叫{name},年龄{age},学历{education},工作年限{years},面试职位{job},想要去的城市是{city}
请按照以下要求生成简历:
task1: 列出这个人的基本资料，如姓名、出生年月、学历、面试职位、工作年限、意向城市，头像等。一行列一个资料，头像用emoji头像即可。
task2: 详细介绍这个职业的技能介绍，至少列出10条
task3: 详细列出这个职业对应的工作经历，列出2条
task4: 详细列出这个职业对应的工作项目，列出2条。项目按照项目背景、项目细节、项目难点、优化和改进、我的价值几个方面来描述，多展示职业关键字。也可以体现我在项目管理、工作推进方面的一些能力。
task5: 详细列出个人评价，100字左右
你把以上任务结果按照以下Markdown格式输出：
"""



#输入进来的模板
def Jianli(dict_info, openai_api_key):
    # dic_info = {"姓名": name, "年龄": age, "学历": education, "工作年限": years
    #             "面试职位": job, "意向城市": city}
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,openai_api_base="https://api.aigc369.com/v1")
    chain = prompt | model
    result = chain.invoke({
        "name": dict_info["姓名"],
        "age":dict_info["年龄"],
        "education":dict_info["学历"],
        "years":dict_info["工作年限"],
        "job":dict_info["面试职位"],
        "city":dict_info["意向城市"]
    })

    return result.content

