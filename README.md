# 💬 ChatBot (Fine-Tuned GPT-2)

A conversational chatbot built by fine-tuning **GPT-2 Medium** on a custom instruction-based dataset.
The project focuses on understanding LLM internals and building an end-to-end system — from training to deployment.

---

## 🚀 Project Overview

This chatbot is trained on a dataset (`instruction-data.json`) containing ~1100 samples in the format:

```
{
  "instruction": "...",
  "input": "...",
  "output": "..."
}
```

### 🔹 Training Details

* Model: **GPT-2 Medium**
* Dataset size: ~1100 instruction groups
* Train split: 80%
* Validation: 5%
* Test: 15%

The goal was to build a **mini instruction-following model** similar to early LLMs.

---

## 💬 Features

* 🧠 Instruction-based responses (Instruction + optional Input)
* 💻 Custom Streamlit UI (WhatsApp-inspired chat interface)
* ⚡ End-to-end pipeline:

  * Training (`train.py`)
  * Inference (`model.py`)
  * Deployment (`app.py`)

---

## 🖥️ Demo UI

The chatbot UI is inspired by WhatsApp:

* Chat bubbles (user vs bot)
* Instruction + Input interaction
* Real-time response generation

> ⚠️ UI is functional but still under improvement for better UX.

---

## ⚙️ Run Locally

### 1. Clone the repository

```
git clone <your-repo-link>
cd chatbot-project
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model

```
python train.py
```

### 4. Run the app

```
streamlit run app.py
```

### 5. Start chatting 🎉

---

## 🙏 Acknowledgements

This project is a result of learning from amazing mentors:

* **Krish Naik Sir**
  Helped build strong fundamentals in:

  * Machine Learning (Supervised & Unsupervised)
  * NLP
  * Deep Learning

* **Dr. Raj Dandekar**
  His YouTube playlist *"LLM from Scratch"* was crucial in understanding:

  * GPT architecture
  * Byte Pair Encoding (BPE)
  * Causal Attention
  * Core transformer concepts with intuitive explanations

---

## ⚠️ Limitations

* 🚫 Training larger models (e.g., GPT-2 Large) failed due to GPU limitations (Colab crashes)
* 🚫 Large datasets (e.g., Alpaca 52k) could not be used due to memory constraints
* 🤖 Model responses are inconsistent:

  * Sometimes accurate and creative
  * Sometimes irrelevant or weak

---

## 🔮 Future Improvements

* ⚡ Train on larger datasets with better compute resources
* 🧠 Use more powerful models (GPT-2 Large / LLaMA variants)
* 💾 Improve storage handling for larger models
* 🎨 Enhance UI to fully replicate modern chat applications
* 📈 Improve response quality and consistency

---

## 🧠 Key Learning Outcomes

* Understanding of GPT architecture and transformer internals
* Hands-on experience with fine-tuning LLMs
* Building and deploying ML applications using Streamlit
* Managing real-world constraints like GPU limits and memory

---

## 🧪 Additional Experiment

I also trained a small text generation model on a custom dataset (`the-verdict.txt`) to understand how models learn patterns from raw text.

While the output is simple, it helped me understand:
- Tokenization behavior
- Sequence prediction
- Limitations of small datasets

## ⭐ Final Note

This project represents a step toward building intelligent systems from scratch.
It’s not perfect — but it reflects learning, experimentation, and growth.

---
