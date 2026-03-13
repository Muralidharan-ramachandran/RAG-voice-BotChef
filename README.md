# RAG
# 🍳 VoiceBotChef  
### *A Local Voice-Enabled Vectorless RAG Cooking Assistant*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/BM25-Vectorless%20RAG-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Local-orange?style=for-the-badge" />
</p>

<p align="center">
  <b>🎤 Speak your recipe question → 📚 Retrieve from cookbook PDF → 🤖 Generate/Read answer → 🔊 Hear the response</b>
</p>

---

## ✨ Overview

**VoiceBotChef** is a **local AI-powered voice cooking assistant** that answers recipe-related questions from a **South Indian recipe book PDF** using **vectorless retrieval (BM25)** and optional **local LLM generation via Ollama**.

It is designed for a **hands-free cooking experience**, allowing users to ask questions like:

- *"How do I make dosa?"*
- *"Tell me the recipe for rasam"*
- *"What ingredients are needed for sambar?"*

The bot listens through the microphone, retrieves the most relevant recipe from the cookbook, optionally refines the response with a lightweight local LLM, and then **speaks the answer aloud**.

---

## 🌟 Key Highlights

- 🎤 **Voice Input** using microphone
- 📝 **Speech-to-Text** using `SpeechRecognition`
- 📚 **Recipe Retrieval from PDF**
- 🔍 **Vectorless RAG** using **BM25** (No embeddings / No vector DB)
- 🤖 **Optional Local LLM** support via **Ollama**
- 🔊 **Text-to-Speech Output** using `pyttsx3`
- 💻 **Fully local-first** architecture
- 🪶 Lightweight and suitable for **low-resource laptops**
- 🛠️ **Fallback mode** if the LLM is unavailable or memory is low

---

## 🧠 Why This Project?

Most RAG systems depend on:

- Embeddings
- Vector Databases
- Cloud APIs
- Paid LLM services

**VoiceBotChef** explores a **simpler and more efficient alternative**:

✅ **BM25-based lexical retrieval**  
✅ **Domain-specific PDF knowledge base**  
✅ **Voice interaction**  
✅ **Optional local lightweight LLM**  

This makes it ideal for:

- Offline/edge AI demos
- Low-memory laptops
- GenAI learning projects
- Lightweight RAG prototypes
- Recruiter-friendly portfolio projects

---

## 🏗️ System Architecture

```text
┌────────────────────┐
│   User speaks 🎤   │
└─────────┬──────────┘
          │
          ▼
┌──────────────────────────────┐
│ Speech-to-Text (Google STT)  │
│ using SpeechRecognition      │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│  Query Text                  │
│  e.g. "How to make dosa?"    │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ PDF Recipe Retrieval         │
│ using BM25 (rank-bm25)       │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ Optional Local LLM (Ollama)  │
│ e.g. TinyLlama               │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│  Final Answer / Fallback     │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ Text-to-Speech (pyttsx3) 🔊  │
└──────────────────────────────┘
