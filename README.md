# Model Context Protocol (MCP) - From Scratch 🚀

A comprehensive repository for learning, building, and experimenting with the **Model Context Protocol (MCP)** using Python, FastMCP, and LangChain.

---

## 📌 Overview

The **Model Context Protocol (MCP)** is an open standard designed to seamlessly connect AI models (LLMs) and agents with local tools, data sources, databases, and APIs.

This repository serves as a step-by-step guide and template for:
- Creating custom **MCP Servers** & **Tools** using Python (`mcp` SDK).
- Connecting LLMs and Agent frameworks (like **LangChain**) to MCP servers.
- Exposing local functions, file systems, and APIs to AI tools securely.

---

## 🛠️ Tech Stack & Dependencies

- **Language**: Python 3.10+
- **Environment Manager**: [`uv`](https://github.com/astral-sh/uv) (recommended) or standard `venv`
- **Core Libraries**:
  - `mcp[cli]`: Official Anthropic Model Context Protocol SDK & Inspector CLI
  - `langchain`: Agent orchestration and LLM tool integration
  - `pydantic`: Schema validation and type safety
  - `httpx`: Async HTTP client for external integrations & SSE
  - `python-dotenv`: Environment variable & secret key management
  - `uvicorn` & `starlette`: ASGI web server support for SSE/HTTP transports

---

## 📁 Repository Structure

```text
├── main.py            # Entry point for testing & running MCP implementations
├── requirements.txt   # Required Python packages
├── pyproject.toml     # Project metadata and dependency definitions
├── .gitignore         # Configured to prevent uploading keys, .venv, or caches
└── README.md          # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mohd-ahtasham-ansari/MCP-model-context-protocol-from-scratch.git
cd MCP-model-context-protocol-from-scratch
```

### 2. Create Virtual Environment
Using **`uv`**:
```bash
uv venv
```

Activate the environment:
- **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\activate
  ```
- **Linux / macOS**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Using **`uv`**:
```bash
uv pip install -r requirements.txt
```
*Or using standard `pip`:*
```bash
pip install -r requirements.txt
```

---

## 💡 Quick Start: Running an MCP Server

Run your MCP script:
```bash
python main.py
```

### Debugging with MCP Inspector
You can test and inspect your local MCP server with the interactive MCP Inspector:
```bash
npx @modelcontextprotocol/inspector python main.py
```

---

## 🛡️ Security

This project includes a strict `.gitignore` to ensure `.env` files, API keys, credentials, and virtual environment directories are **never** committed to version control.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
