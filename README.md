# 🚀 PDF-based AI Chatbot

A simple AI chatbot that processes PDFs and answers questions using **LangChain, FAISS, and Ollama**.

## 🛠️ Frameworks & Libraries
- **LangChain** - For building LLM-powered applications
- **FAISS** - Vector database for efficient retrieval
- **Ollama** - Embedding and LLM model provider
- **PyPDF** - Extracting text from PDFs

## 🔧 Functions
### 📄 Load PDF
```python
def pdf_loader(path):
    """Loads PDF and extracts text."""
```

### ✂️ Split Text into Chunks
```python
def split_chunks(pages):
    """Splits text into chunks for processing."""
```

### 📌 Create Vector Database
```python
def create_vector_db(chunks):
    """Embeds text and stores it in FAISS."""
```

### 📥 Load Pre-trained Vector Database
```python
def load_vector_db(path):
    """Loads an existing FAISS database."""
```

### 🤖 Create Chatbot
```python
def making_bot(vector_db):
    """Creates a chatbot using the vector database."""
```

### 🎯 Main Function
```python
def main():
    """Runs the chatbot interface. Enter a PDF path or use a pre-built vector DB."""
```

## 📌 How to Use
1. Load a PDF or use a pre-trained vector database.
2. The chatbot processes your input and retrieves relevant answers.
3. Type **'tata'** to exit.

---
🔥 **Get Started & Have Fun!**

