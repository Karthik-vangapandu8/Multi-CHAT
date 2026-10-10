# 📚 MultiPDF Local Chat App (Powered by Ollama)

A 100% local, privacy-focused Python application that allows you to chat with multiple PDF documents using **Ollama** and **LangChain**. No cloud API keys or external services required—all text embeddings and language model responses run locally on your machine.

---

## 🌟 Features

- 🔒 **100% Local & Private**: No data leaves your machine. Powered entirely by local Ollama models (`qwen2.5` & `nomic-embed-text`).
- ⚡ **Fast Vector Search**: Uses the FAISS vector store for rapid document chunk indexing and semantic retrieval.
- 🎨 **Modern Cyberpunk UI**: Sleek Orange & Black theme built with Streamlit, custom glassmorphic CSS, and responsive chat inputs.
- 📄 **AES Encrypted PDF Support**: Full support for standard and AES-encrypted PDF documents.

---

## 🛠️ Prerequisites & Ollama Setup

1. **Install Ollama**:
   Download and install Ollama from [ollama.com](https://ollama.com).

2. **Pull the Required Models**:
   Open your terminal and pull the language model and embedding model:
   ```bash
   ollama pull qwen2.5:latest
   ollama pull nomic-embed-text
   ```

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ask-multiple-pdfs.git
   cd ask-multiple-pdfs
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running the App

Start the application using Streamlit:

```bash
streamlit run app.py
```

Once running, navigate to `http://localhost:8501` in your browser.

---

## 📖 How It Works

1. **PDF Text Extraction**: Reads and parses uploaded PDF documents using `PyPDF2` (with `pycryptodome` for AES decryption).
2. **Text Chunking**: Divides long text into manageable overlapping chunks via `CharacterTextSplitter`.
3. **Local Embedding Vectorization**: Converts chunks to embeddings using `OllamaEmbeddings(model="nomic-embed-text")`.
4. **FAISS Vector Indexing**: Indexes embeddings into a local FAISS vector store for fast similarity search.
5. **Contextual QA Chain**: Rewrites follow-up questions using `create_history_aware_retriever` and generates precise answers with `ChatOllama(model="qwen2.5:latest")`.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).