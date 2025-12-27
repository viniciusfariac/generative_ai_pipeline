from dotenv import load_dotenv
import os
import groq
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
load_dotenv()

def generate_news(df):
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    for index, cliente in df.iterrows():

        prompt_template = f"Voce é uma ia do marketing Santander, especializada em enviar mensagens para clientes do banco dizendo como investimento é bom. Essa é as informações do usuario: {cliente["Nome"]}, {cliente["Conta"]}"

        modelo = ChatGroq(
        groq_api_key=groq_api_key,
        model="openai/gpt-oss-20b",
        temperature=0.1
        )

        resposta = modelo.invoke(prompt_template)
        print(resposta.content)

    
    