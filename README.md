#  Streamlit & Chainlit Chatbot Apps

## Overview
This project contains two chatbot applications built using:

- **Streamlit** → Interactive chatbot UI with response streaming
- **Chainlit** → Conversational AI interface with chat history

Both applications are integrated with OpenAI models and demonstrate building conversational AI interfaces using different frameworks.

---

## Project Structure

day9/
│── streamlit_app.py  
│── chainlit_app.py  
│── requirements.txt  
│── .env  
│── README.md  

---

## Features

### Streamlit App
- Chat-based UI
- Maintains chat history
- Response streaming
- OpenAI LLM integration

### Chainlit App
- Built-in conversational interface
- Session-based chat history
- OpenAI LLM integration
- Event-driven architecture

---

## Technologies Used

- Python
- Streamlit
- Chainlit
- OpenAI SDK
- python-dotenv

---

## Installation

### 1. Create virtual environment
```bash
python3.10 -m venv venv
2. Activate virtual environment
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Environment Setup

Create a .env file:

OPENAI_API_KEY=your_api_key_here
Run the Streamlit App
streamlit run streamlit_app.py

App will open at:

http://localhost:8501

Run the Chainlit App
chainlit run chainlit_app.py

App will open at:

http://localhost:8000

Key Concepts Implemented
Streamlit
st.chat_input()
st.chat_message()
st.session_state
st.write_stream()
Chainlit
@cl.on_chat_start
@cl.on_message
cl.user_session
cl.Message