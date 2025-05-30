#pip install langchain-openai

from langchain_openai import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings()   # 模型的embeddings，有默认值

embeddings = embeddings_model.embed_documents(
    [
        "嗨！",
        "哦，你好！",
        "你叫什么名字？",
        "我的朋友们叫我World",
        "Hello World！"
    ]
)
#第一个打印是embeddings的文本数量，第二个打印是第一段文本的embedding向量维度
print(len(embeddings), len(embeddings[0])) 
