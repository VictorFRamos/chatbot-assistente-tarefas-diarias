import os
from openai import OpenAI
from dotenv import load_dotenv
from memory import add_task, list_tasks

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat():
    print("🤖 Assistente pessoal iniciado! (digite 'sair')\n")

    mensagens = [
        {
            "role": "system",
            "content": """
Você é um assistente pessoal que ajuda o usuário nas tarefas do dia a dia.

Regras:
- Seja direto e útil
- Sugira melhorias na rotina
- Ajude com produtividade
- Quando o usuário quiser adicionar tarefa, responda apenas com:
ADD_TASK: descrição da tarefa
"""
        }
    ]

    while True:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Até mais 👋")
            break

        # comando manual
        if user_input.lower() == "ver tarefas":
            tarefas = list_tasks()
            print("\n📋 Suas tarefas:")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
            print()
            continue

        mensagens.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=mensagens,
            temperature=0.5
        )

        resposta = response.choices[0].message.content

        # intercepta ação de tarefa
        if resposta.startswith("ADD_TASK:"):
            tarefa = resposta.replace("ADD_TASK:", "").strip()
            add_task(tarefa)
            print(f"\n✅ Tarefa adicionada: {tarefa}\n")
        else:
            print(f"\n🤖 {resposta}\n")

        mensagens.append({"role": "assistant", "content": resposta})


if __name__ == "__main__":
    chat()
