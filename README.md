# AI-Powered-Customer-Support-Automation-System
AI-Powered Customer Support Automation System built with LangGraph, LangChain, RAG, and SQLite. It classifies customer queries, routes them to specialized support agents, retrieves knowledge from documents, stores conversation history, and supports human approval for sensitive requests.
# 🤖 AI-Powered Customer Support Automation System using LangGraph

An intelligent customer support automation system built using **LangGraph**, **LangChain**, **Python**, **RAG (Retrieval-Augmented Generation)**, and **SQLite Memory**. The system automates customer query handling by classifying user intents, routing requests to specialized support agents, retrieving relevant information from company documents, maintaining conversation history, and incorporating a Human-in-the-Loop approval process for sensitive requests.

---

## 📌 Project Overview

ABC Technologies is a SaaS company that receives thousands of customer support requests related to product information, technical issues, billing, account management, and refunds.

This project automates the customer support workflow using AI agents and LangGraph by:

- Accepting customer queries
- Classifying customer intent
- Routing requests to the appropriate department
- Retrieving relevant information using RAG
- Remembering previous customer conversations using SQLite
- Handling sensitive requests through Human-in-the-Loop approval
- Validating responses through a Supervisor Agent
- Generating the final response

---

# ✨ Features

- ✅ Intent Classification
- ✅ LangGraph Workflow
- ✅ Multi-Agent Architecture
- ✅ Sales Support Agent
- ✅ Technical Support Agent
- ✅ Billing Support Agent
- ✅ Account Support Agent
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ SQLite Conversation Memory
- ✅ Human-in-the-Loop Approval
- ✅ Supervisor Agent
- ✅ Modular Project Structure
- ✅ Easy to Extend

---

# 🏗️ System Workflow

```text
Customer Query
      │
      ▼
Intent Classification
      │
      ▼
Department Routing
      │
      ▼
Specialized Support Agent
      │
      ▼
RAG Knowledge Retrieval
      │
      ▼
SQLite Memory
      │
      ▼
Human Approval (if required)
      │
      ▼
Supervisor Agent
      │
      ▼
Final Customer Response
```

---

# 🗂️ Project Structure

```
Customer-Support-LangGraph/
│
├── agents/
│   ├── sales_agent.py
│   ├── technical_agent.py
│   ├── billing_agent.py
│   └── account_agent.py
│
├── docs/
│   ├── pricing.txt
│   ├── faq.txt
│   ├── policy.txt
│   └── technical_manual.txt
│
├── database/
│   └── memory.db
│
├── screenshots/
│
├── diagrams/
│   └── workflow.png
│
├── app.py
├── graph.py
├── router.py
├── rag.py
├── memory.py
├── supervisor.py
├── human.py
├── state.py
├── config.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | Workflow Orchestration |
| LangChain | LLM Framework |
| SQLite | Conversation Memory |
| RAG | Knowledge Retrieval |
| FAISS / ChromaDB | Vector Database |
| Sentence Transformers | Text Embeddings |
| VS Code | Development Environment |

---

# 📚 Knowledge Base Documents

The RAG pipeline retrieves information from:

- 📄 Company Policy
- 📄 Pricing Guide
- 📄 Technical Manual
- 📄 FAQ Document

---

# 👨‍💻 Support Departments

| Department | Handles |
|------------|---------|
| Sales | Product Information, Pricing, Subscription Plans |
| Technical Support | Installation, Login Issues, Application Errors |
| Billing | Payments, Refunds, Invoices |
| Account | Password Reset, Profile Update, Account Activation |

---

# 🧠 Memory Feature

The system stores customer interactions using SQLite.

### Example

Customer:

```
My name is David.
I have a billing issue.
```

Later...

Customer:

```
What was my previous issue?
```

Response:

```
Your previous issue was related to billing.
```

---

# 🔒 Human-in-the-Loop Approval

The following requests require manual supervisor approval:

- Refund Request
- Subscription Cancellation
- Account Closure
- Compensation Request
- Escalation to Management

---

# 🤖 Supervisor Agent

The Supervisor Agent performs a final validation of responses before they are delivered to the customer.

Responsibilities:

- Validate responses
- Improve response quality
- Ensure company policy compliance
- Generate final response

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Customer-Support-LangGraph.git
```

Go to project directory

```bash
cd AI-Customer-Support-LangGraph
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python app.py
```

---

# 🧪 Sample Queries

### Query 1

```
What are the pricing plans available?
```

Expected Route

```
Sales Agent
```

---

### Query 2

```
I forgot my account password.
```

Expected Route

```
Account Agent
```

---

### Query 3

```
My application crashes while uploading a file.
```

Expected Route

```
Technical Support Agent
```

---

### Query 4

```
I need a refund for my annual subscription.
```

Expected Route

```
Billing Agent
↓

Human Approval
↓

Supervisor
```

---

### Query 5

```
What was my previous support issue?
```

Expected Route

```
SQLite Memory Recall
```

---

# 📸 Project Deliverables

- ✅ LangGraph Workflow Diagram
- ✅ Source Code
- ✅ RAG Integration
- ✅ SQLite Memory
- ✅ Human-in-the-Loop Workflow
- ✅ Documentation
- ✅ Screenshots
- ✅ Demonstration

---

# 📈 Future Enhancements

- OpenAI GPT Integration
- Hugging Face Models
- Web Interface using Streamlit
- Docker Deployment
- Cloud Deployment
- REST API Support
- Voice-based Customer Support
- Multi-language Support
- Authentication System
- Admin Dashboard

Author
Nidhi Singh
---

## ⭐ If you found this project useful, consider giving it a Star!
