# PARAFLOW – AI-Powered Text Rephraser

Paraflow is a modern, fast, and sleek AI-powered rephrasing tool built with **FastAPI** and **Transformers**, integrated into a clean browser extension UI. Whether you're a student, writer, or professional – Paraflow helps you rewrite sentences with clarity and precision using cutting-edge language models.

![Paraflow Screenshot](assests/logo[1].png)

---

## Features

- **Real-time Paraphrasing** using Pegasus Transformer model
- **1000-character limit** for concise input
- **FastAPI backend** with CUDA acceleration support
- **Responsive, dark-themed UI** styled with CSS
- **Chrome Extension support** with local API communication
- **Word/letter counter & validation**

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI, HuggingFace Transformers
- **Model**: [`tuner007/pegasus_paraphrase`](https://huggingface.co/tuner007/pegasus_paraphrase)
- **Environment**: PyTorch, CUDA (if available)

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/paraflow-rephraser.git
cd paraflow-rephraser
