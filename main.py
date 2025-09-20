import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY não encontrada. Adicione ao arquivo .env")

genai.configure(api_key=api_key)

def conversar_com_gemini(pergunta: str) -> str:
    """
    Envia a pergunta para o modelo Gemini e retorna a resposta.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")  # Modelo leve e rápido
    resposta = model.generate_content(pergunta)
    return resposta.text

if __name__ == "__main__":
    print("Chat com Gemini (digite 'sair' para encerrar)")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        try:
            resposta = conversar_com_gemini(pergunta)
            print("Gemini:", resposta)
        except Exception as e:
            print("Erro:", e)
