# Empório da Música — AI Customer Support Agent

An AI-powered customer support agent developed in Python as part of the **AI Engineer Technical Challenge for Artefact**.

The project aims to assist the customer service team at Empório da Música, a fictional musical instruments store located in Campo Grande, Brazil, by automating recurring customer inquiries and providing accurate information based on the store's operational data and internal policies.

## Overview

The agent interacts with customers through a command-line interface (CLI), answering questions about products, store information, and customer service policies.

It combines a Large Language Model (LLM), Function Calling, and Retrieval-Augmented Generation (RAG) to determine when to retrieve structured data, search internal documentation, or respond directly.

### Key Features

- **Natural Language Interaction:** Understands and responds to customer messages in a conversational and friendly manner.
- **Product Consultation:** Retrieves product information, prices, and availability from CSV datasets.
- **Order Tracking:** Consults order information to provide customers with relevant updates.
- **Customer Data Retrieval:** Accesses customer information when required.
- **Policy Consultation:** Uses RAG to retrieve relevant information from the store's internal PDF documentation.
- **Function Calling:** Dynamically selects and executes tools according to the customer's request.
- **Out-of-Scope Handling:** Identifies requests unrelated to the store and responds appropriately.
- **Local LLM Execution:** Uses Ollama to run the language model locally.

## Architecture

The solution follows a modular architecture, separating agent orchestration, tools, document retrieval, and external services.

### Project Structure

```text
emporio-musica-agent/
│
├── data/
│   ├── products.csv
│   └── politicas_da_loja.pdf
│
├── src/
│   ├── main.py
│   │
│   ├── agent/
│   │   ├── agent.py
│   │   └── prompts.py
│   │
│   ├── tools/
│   │   ├── products.py
│   │   ├── policies.py
│   │   ├── tool_definitions.py
│   │
│   ├── flows/
│   │   ├── fallback_flow.py
│   │   ├── order_flow.py
│   │   ├── policy_flow.py
│   │   ├── product_flow.py
│   │
│   ├── repositories/
│   │   ├── product_repository.py
│   │
│   ├── rag/
│   │   ├── document_loader.py
│   │   ├── indexer.py
│   │   └── retriever.py
│   │
│   └── services/
│       ├── llm_service.py
│
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Highlight Responsibilities

| Component | Responsibility |
|---|---|
| `main.py` | Initializes the application and handles user input through the CLI. |
| `agent.py` | Orchestrates the interaction between the user, LLM, and available tools. |
| `prompts.py` | Defines the agent's persona, instructions, and behavioral rules. |
| `llm_service.py` | Handles communication with the Ollama model. |
| `products.py` | Provides product information, prices, and availability. |
| `politicas_da_loja.py` | Provides general store information. |
| `document_loader.py` | Extracts and prepares text from the PDF documentation. |
| `retriever.py` | Retrieves relevant document sections based on customer queries. |

## Technical Decisions

### 1. Python

Python was selected as the primary programming language because of its ecosystem for AI development, particularly its libraries for LLM integration, data processing, and vector search.

A virtual environment was created to isolate project dependencies and ensure a consistent development environment.

### 2. LLM and Model Provider — Ollama

Ollama was selected as the model provider to run language models locally.

This approach avoids depending on paid external API calls during development and testing, while providing direct control over the model configuration.

The project uses the `qwen3:4b` model for natural language understanding, response generation, and tool selection.

### 3. Agent Architecture — Hybrid RAG + Function Calling

A hybrid architecture was chosen to handle two different types of information retrieval.

**Function Calling**

Used for structured and operational data that requires direct access to the store's datasets.

Examples:
- Checking product prices and availability.
- Retrieving order status.
- Accessing customer information.
- Retrieving general store information.

The LLM determines which tool is relevant to the customer's request, executes it, and uses the returned information to formulate a response.

**Retrieval-Augmented Generation (RAG)**

Used for unstructured information contained in the store's internal PDF documentation.

The document retrieval pipeline follows these steps:

1. Extracts text from the PDF using `pypdf`.
2. Processes the extracted content.
3. Generates embeddings using an Ollama embedding model.
4. Stores the document vectors in ChromaDB.
5. Retrieves relevant document sections based on the customer's question.
6. Provides the retrieved context to the LLM to generate a grounded response.

This approach allows the agent to answer questions about store policies without requiring the entire document to be included in every prompt.

### 4. Vector Database — ChromaDB

ChromaDB was selected to store and retrieve document embeddings.

Its persistent storage functionality allows document vectors to remain available between application executions, avoiding unnecessary reprocessing.

### 5. Interface — Command Line Interface (CLI)

A CLI was chosen because the primary objective of the challenge is to demonstrate the agent's reasoning, retrieval capabilities, and integration with external tools rather than developing a graphical interface.

### 6. Data Processing

The operational datasets are provided in CSV format.

The project centralizes data access through a dedicated service, allowing the tools to retrieve the required information without duplicating data-loading logic.

## Project Requirements

Before running the project, make sure you have:

- Python 3.10 or later.
- [Ollama](https://ollama.com/) installed and running.
- Git installed.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ryannardelli/emporio-musica-agent.git
cd emporio-musica-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
OLLAMA_MODEL=qwen3:4b
OLLAMA_HOST=http://localhost:11434
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

Replace the embedding model placeholder with the Ollama embedding model configured in the project.

### 5. Download the Ollama models

Make sure Ollama is running, then download the language model:

```bash
ollama pull qwen3:4b
```

Also download the embedding model configured in your `.env` file:

```bash
ollama pull nomic-embed-text
```

### 6. Run the application

From the project root:

```bash
python -m src.main
```

The agent will start in the terminal and wait for customer messages.

## Limitations and Future Improvements

Although the prototype implements the main requirements of the challenge, several improvements could be considered with additional development time:

- **Conversation Persistence:** Store conversation history to maintain context across application sessions.
- **Automated Testing:** Add unit and integration tests for tools, retrieval, and agent orchestration.
- **API Integration:** Expose the agent through a REST API to support integration with messaging platforms such as WhatsApp.
- **Observability:** Implement structured logging and monitoring to track tool execution, retrieval quality, and model responses.
- **Retrieval Optimization:** Experiment with document chunking strategies, metadata filtering, and retrieval evaluation to improve RAG accuracy.
- **Production Deployment:** Containerize the application and deploy it in an environment suitable for production workloads.
- **Security and Privacy:** Implement authentication, access control, and appropriate protection of customer information.

## Technologies Used

The project was developed using the following technologies:

- **Python** – Main programming language.
- **Ollama** – Local execution of language models (LLMs) and embedding models.
- **Qwen3:4b** – Language model responsible for generating conversational responses.
- **Nomic Embed Text** – Embedding model used to convert text into vector representations.
- **ChromaDB** – Vector database used to store document embeddings and perform semantic searches.
- **RAG (Retrieval-Augmented Generation)** – Architecture used to retrieve relevant information from internal documents and provide contextual responses.
- **PyPDF** – PDF text extraction for processing the store's policies and procedures.
- **Pandas** – Data manipulation and processing, particularly for handling structured data.
- **python-dotenv** – Environment variable management.

They were used as development assistants for exploring implementation approaches, troubleshooting errors, reviewing code, and improving the integration of AI components.

The architecture, technical decisions, and implementation were evaluated and adapted throughout the development process.

## Author

Developed as part of the **AI Engineer Technical Challenge — Artefact**.

---
