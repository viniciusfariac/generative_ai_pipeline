from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
load_dotenv()
from load import load_users  # noqa: E402

def generate_news(df):
    groq_api_key = os.getenv("GROQ_API_KEY")

    modelo = ChatGroq(
        groq_api_key=groq_api_key,
        model="openai/gpt-oss-20b",
        temperature=0.1
    )

    for index, cliente in df.iterrows():

        prompt_template = (
            f"Você é uma IA do marketing Santander, especializada em enviar mensagens "
            f"sobre investimentos, envie mensagens curtas, apenas falando para o cliente investir no santander, não de exemplos ou fale osre investimentos afundo. Dados do cliente: "
            f"Nome: {cliente['Nome']}, Conta: {cliente['Conta']}"
        )

        resposta = modelo.invoke(prompt_template)
        if resposta and resposta.content:
            load_users(df, resposta.content, index)

    
    