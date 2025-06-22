# ⚡ fastapi-kit

**The ultimate CLI scaffolding toolkit for [FastAPI](https://fastapi.tiangolo.com/)**  
Generate projects, apps, and full CRUD modules with one command.

---

## ✨ Overview

`fastapi-kit` is a modern, developer-focused CLI that brings Django-style scaffolding to the FastAPI ecosystem.

With just a few commands, you can generate production-ready boilerplate for:

- FastAPI projects
- Modular app folders
- CRUD logic including models, schemas, routes

No more copy-pasting code — just scaffold and build.

---

## 🚀 Features

- 🔨 `fastapikit startproject <name>` – Create a FastAPI project
- 🧱 `fastapikit startapp <name>` – Add a modular app folder
- ⚙️ `fastapikit generate-crud <ModelName>` – Auto-generate full CRUD
- 🪄 Clean flat CLI syntax
- ✅ Typer-powered CLI (from the creator of FastAPI)
- 🧰 Ready to plug into Uvicorn + SQLAlchemy stack

---

## 📦 Installation (via GitHub)

Until it's published on PyPI, install it manually:

```bash
git clone https://github.com/yourusername/fastapi-kit.git
cd fastapi-kit
pip install -e .
```
Recommended: use a virtual environment


## 🧪 Usage
```bash
# Start a new FastAPI project
fastapikit startproject myproject

# Add a new app module
cd myproject
fastapikit startapp blog

# Generate full CRUD for a model
fastapikit generate-crud Post
```

## 🏗️ Generated Folder Structure
```bash
myproject/
├── main.py
├── core/
│   └── __init__.py
├── apps/
│   └── blog/
│       ├── __init__.py
│       ├── models.py
│       ├── schemas.py
│       ├── crud.py
│       └── routes.py
```

## 📁 Project Layout (Dev Structure)
```bash
fastapi-kit/
├── pyproject.toml / setup.cfg
├── README.md
├── src/
│   └── fastapi_kit/
│       ├── cli.py
│       └── commands/
│           ├── startproject.py
│           ├── startapp.py
│           └── generate_crud.py
```

## 🧠 Requirements
- Python 3.8+
- FastAPI
- Typer
- Jinja2

All dependencies are installed automatically when using ```bash pip install -e .```.

## 👨‍💻 Contributing

We welcome all contributions! Whether it’s fixing a bug, adding a feature, improving documentation, or optimizing templates — your help is highly appreciated 🙌

### 🛠️ Steps to Contribute

1. **Fork this repository**  
   Click the `Fork` button in the top right of the repo.

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/fastapi-kit.git
   cd fastapi-kit

