# 🧩 Tokenize CLI

An easy-to-use command-line tool for **tokenizing text files or folders** using [🤗 Hugging Face Transformers](https://huggingface.co/docs/transformers).
Ideal for quick inspection of token counts, model comparisons, or debugging chat templates.

---

## 📝 TODO

* Tokenize a folder to parse all the file inside that folder using dataset library
* Visualize the number with scientific notation
* List the special tokens in the context

---

## 🚀 Features

* 🔤 Tokenize any text file with your favorite Hugging Face tokenizer
* 🧮 Count **special**, **non-special**, and **total tokens**
* 💬 Apply chat templates to structured JSON conversation files
* ⚙️ Persist your tokenizer configuration in a simple local JSON file
* ⚡ Uses `fire` for a fast CLI and Hugging Face `transformers` under the hood
* 🪶 Minimal setup — zero boilerplate

---

## 📦 Installation

You can install Tokenize CLI using [**uv**](https://github.com/astral-sh/uv), a modern, lightning-fast Python package manager.

### 🔧 Quick Install

```bash
uv pip install tokenize-cli
```

### 🧩 Install from Local Directory

If you have cloned the repository locally:

```bash
uv pip install .
```

### 🌀 Install Directly from GitHub

```bash
uv pip install git+https://github.com/ZoneTwelve/tokenize-cli.git
```

### 🧑‍💻 Development Install

If you’re working on the project locally (editable mode):

```bash
uv pip install -e .
```

---

## 🧠 Usage

### 1️⃣ Configure Your Tokenizer

Before tokenizing any files, set your preferred model:

```bash
tokenize-cli --model google/gemma-3-270m-it
```

Inspect your current configuration:

```bash
tokenize-cli
```

Example output:

```
📄 Current config: {'tokenizer_model': 'google/gemma-3-270m-it'}
```

---

### 2️⃣ Tokenize a Text File

Use the `tokenize` command to analyze a file:

```bash
tokenize file path/to/file.txt
```

Example output:

```
🔤 Using tokenizer: google/gemma-3-270m-it
📄 Tokenizing file: example.txt
✅ Tokenization complete.
🧩 Special tokens    : 3
🔡 Non-special tokens: 197
🔢 Total tokens      : 200
```

---

### 3️⃣ Apply Chat Templates

For chat-style data (like `messages.json`):

```bash
tokenize chat examples/messages.json
```

To tokenize the resulting text and count total tokens:

```bash
tokenize chat examples/messages.json --tokenize True
```

Optionally, save the chat-rendered text to a file:

```bash
tokenize chat examples/messages.json --save chat_output.txt
```

---

## 🧰 Command Reference

| Command        | Description                             |
| -------------- | --------------------------------------- |
| `tokenize`     | Tokenize text files and count tokens    |
| `tokenize-cli` | Configure or inspect tokenizer settings |

Example commands:

```bash
# Configure model
tokenize-cli --model google/gemma-3-270m-it

# Tokenize plain text file
tokenize file my_text.txt

# Apply chat template
tokenize chat examples/messages.json

# Tokenize chat template output
tokenize chat examples/messages.json --tokenize True
```

---

## 🧩 Example Data

Example chat file: `examples/messages.json`

```json
[
  {"role": "system", "content": "You are an tokenizer."},
  {"role": "user", "content": "This is an easy to use tokenize CLI"},
  {"role": "assistant", "content": "You are 100% correct, this is an easy to use tokenize CLI and I hope you like it."}
]
```

---

## 🧑‍💻 Development

Clone and install with `uv`:

```bash
git clone https://github.com/ZoneTwelve/tokenize-cli.git
cd tokenize-cli
uv pip install -e .
```

Run locally:

```bash
python src/main.py file examples/messages.json
```

Or configure the tokenizer:

```bash
python src/cli.py --model Qwen/Qwen3-0.6B
```

---

## ⚖️ License

This project is licensed under the **GNU Affero General Public License v3.0**.
See the [LICENSE](LICENSE) file for details.
