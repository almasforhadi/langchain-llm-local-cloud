# LangChain LLM Usage – README

## Overview

This README explains **what LangChain is**, **how the setup works**, and **how execution happens** for two common cases:

1. **Local LLM using Ollama (No API Key)**
2. **Cloud LLM using OpenAI GPT‑4.1 (API Key required)**

---

## What is LangChain?

**LangChain is a framework, not a model.**

It helps developers:

* Call Large Language Models (LLMs)
* Send prompts and receive responses
* Build agents, memory, tools, and workflows

LangChain itself **does not generate answers**.
It only connects your code to an actual LLM.

---

## Two Ways to Use LangChain

LangChain can work with:

* **Cloud LLMs** (OpenAI GPT‑4.1)
* **Local LLMs** (Ollama, LLaMA, Mistral, etc.)

---

# Option 1: LangChain + Ollama (Local LLM)

### Purpose

Run an LLM **locally on your machine** without internet or API key.

---

## Presetup (One‑time)

### 1. Install Ollama

Download and install from:
[https://ollama.com](https://ollama.com)

Restart the PC after installation.

### 2. Download a Model

```bash
ollama pull llama3
```

### 3. Install Python Packages

```bash
pip install langchain langchain-community
```

---

## Code Example (Local Model)

```python
from langchain_community.chat_models import ChatOllama

model = ChatOllama(model="llama3")

response = model.invoke("Why do parrots talk?")
print(response.content)
```

---

## Execution Process (What Happens Internally)

1. Python code calls LangChain
2. LangChain sends prompt to Ollama
3. Ollama runs **llama3 locally**
4. Model generates response
5. Response is returned to Python

**No API key. No cloud call.**

---

# Option 2: LangChain + OpenAI GPT‑4.1 (Cloud LLM)

### Purpose

Use **OpenAI’s GPT‑4.1**, a powerful cloud‑based model.

---

## Presetup (One‑time)

### 1. Install Packages

```bash
pip install langchain langchain-openai
```

### 2. Set OpenAI API Key

**Windows (PowerShell):**

```powershell
setx OPENAI_API_KEY "sk-your-api-key"
```

Restart the terminal after setting.

---

## Code Example (Cloud Model)

```python
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4.1")

response = model.invoke("Why do parrots talk?")
print(response)
```

---

## Execution Process (What Happens Internally)

1. Python code calls LangChain
2. LangChain sends request to OpenAI servers
3. OpenAI authenticates using API key
4. GPT‑4.1 generates response
5. Response is returned to Python

---

## Why API Key is Required?

* GPT‑4.1 runs on OpenAI servers
* Every request costs compute resources
* API key is required for authentication and billing

---

## Interview Explanation (One Line)

> "GPT‑4.1 is a cloud‑hosted model, so LangChain requires an OpenAI API key to access it."

---

## Key Differences Summary

| Feature     | Ollama (Local) | GPT‑4.1 (Cloud) |
| ----------- | -------------- | --------------- |
| Internet    |  Not required |  Required      |
| API Key     |  No           |  Yes           |
| Cost        | Free           | Paid            |
| Performance | Medium         | Very High       |
| Privacy     | Local          | Cloud           |

---


## Author 
**Name:** Almas Forhadi </br>
**Role:** Junior AI / ML Engineer  
**Focus:** LangChain, LLMs, AI Agents  

---
