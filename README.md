# Streamlit & Chainlit Chatbot Apps

## Overview

This project contains two chatbot applications built using:

* **Streamlit** → Interactive chatbot UI with response streaming
* **Chainlit** → Conversational AI interface with chat history

Both applications are integrated with OpenAI models and demonstrate building conversational AI interfaces using different frameworks.

---

## Project Structure

```text
day9/
│── streamlit_app.py
│── chainlit_app.py
│── requirements.txt
│── .env
│── README.md
```

---

## Features

### Streamlit App

* Chat-based UI
* Maintains chat history
* Response streaming
* OpenAI LLM integration

### Chainlit App

* Built-in conversational interface
* Session-based chat history
* OpenAI LLM integration
* Event-driven architecture

---

## Technologies Used

* Python
* Streamlit
* Chainlit
* OpenAI SDK
* python-dotenv

---

## Installation

### 1. Create Virtual Environment

```bash
python3.10 -m venv venv
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

App will open at:

```text
http://localhost:8501
```

---

## Run the Chainlit App

```bash
chainlit run chainlit_app.py
```

App will open at:

```text
http://localhost:8000
```

---

