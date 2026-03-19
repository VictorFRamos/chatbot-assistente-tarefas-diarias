# 🤖 Assistente Pessoal com OpenAI (Python)

Um chatbot simples, porém poderoso, criado para ajudar nas tarefas do dia a dia, como organização, produtividade e gerenciamento de tarefas.

Esse projeto é uma base prática para construir um assistente estilo “Jarvis”, podendo evoluir facilmente para aplicações mais completas (web, API, integrações, etc).

---

## 🚀 Funcionalidades

- 💬 Chat inteligente com contexto  
- 📋 Criação automática de tarefas  
- 🧠 Assistente de produtividade  
- 💾 Memória local (JSON)  
- ⚡ Respostas rápidas usando OpenAI  

---

## 🧠 Como funciona

O assistente interpreta as mensagens do usuário e:

- Responde normalmente (como um chatbot)  
- Identifica quando você quer adicionar uma tarefa  
- Salva automaticamente essa tarefa no arquivo `memory.json`  
- Permite visualizar tarefas com comando simples  

---

## 📁 Estrutura do Projeto
```
src/
│── app.py          # Lógica principal do chatbot
│── memory.py       # Gerenciamento de memória (tarefas)
│── memory.json     # Armazenamento das tarefas (gerado automaticamente)
│── requirements.txt
│── .env
```
---

## ⚙️ Instalação

### 1. Clone o projeto

git clone https://github.com/VictorFRamos/chatbot-assistente-tarefas-diarias
.git  
cd chatbot-assistente  

### 2. Crie um ambiente virtual (opcional)

python -m venv venv  

# Linux/Mac  
source venv/bin/activate  

# Windows  
venv\Scripts\activate  

### 3. Instale as dependências

pip install -r requirements.txt  

---

## 🔐 Configuração

Crie um arquivo `.env` na raiz do projeto:

OPENAI_API_KEY=sua_chave_aqui  

---

## ▶️ Como usar

python app.py  

---

## 💬 Exemplos de uso

Você: preciso estudar inglês amanhã  
→ Tarefa será adicionada automaticamente  

Você: me ajuda a organizar meu dia  
→ O bot sugere uma rotina  

Você: ver tarefas  
→ Lista todas as tarefas salvas  

---

## 🧩 Comandos disponíveis

ver tarefas  → Lista todas as tarefas salvas  
sair         → Encerra o chatbot  

---

## 💾 Como funciona a memória

As tarefas são armazenadas localmente no arquivo:

memory.json  

Exemplo:

{
  "tasks": [
    "Estudar inglês",
    "Treinar na academia"
  ]
}

---

## 🔧 Tecnologias utilizadas

- Python  
- OpenAI API  
- python-dotenv  
- JSON (armazenamento local)  

---

## 🚀 Possíveis melhorias

- API com FastAPI  
- Memória inteligente com embeddings (RAG)  
- Integração com WhatsApp ou Telegram  
- Sistema de lembretes automáticos  
- Dashboard de produtividade  
- Persistência em banco de dados  

---

## 💡 Ideias de uso

- Assistente pessoal  
- Organização de estudos  
- Gestão de tarefas diárias  
- Base para SaaS de produtividade  
- Bot para automação pessoal  

---

## 📄 Licença

Este projeto é livre para uso e modificação.

---

## ⭐ Se esse projeto te ajudou

Considere dar uma estrela no repositório ⭐  
Isso ajuda muito e incentiva novas melhorias!
