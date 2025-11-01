#!/usr/bin/env python3
import json
from pathlib import Path
from transformers import AutoTokenizer
import json
import os

CONFIG_PATH = Path.home() / ".cache" / "tokenize-cli" / "config.json"


def get_model_name() -> str:
    """Retrieve the tokenizer model name from the config file."""
    if not CONFIG_PATH.exists():
        print("❌ Tokenizer not set. Run 'tokenize-cli --model <MODEL>' first.")
        raise SystemExit(1)

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
    return config.get("tokenizer_model")


def count_token_types(tokenizer, token_ids: list[int]) -> tuple[int, int, int]:
    """Count special, non-special, and total tokens."""
    special_token_count = sum(1 for token_id in token_ids if token_id in tokenizer.all_special_ids)
    total_count = len(token_ids)
    non_special_count = total_count - special_token_count
    return special_token_count, non_special_count, total_count


def tokenize(file_path: str):
    """Tokenize a text file and count token types."""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ File not found: {file_path}")
        raise SystemExit(1)

    model_name = get_model_name()
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    print(f"🔤 Using tokenizer: {model_name}")
    print(f"📄 Tokenizing file: {path.name}")

    text = path.read_text(encoding="utf-8", errors="ignore")
    token_ids = tokenizer.encode(text)

    special, non_special, total = count_token_types(tokenizer, token_ids)

    print("✅ Tokenization complete.")
    print(f"🧩 Special tokens    : {special}")
    print(f"🔡 Non-special tokens: {non_special}")
    print(f"🔢 Total tokens      : {total}")

def apply_chat_template(json_file: str, tokenize: bool = False, save: str = None):
    # Check if file exist
    
    model_name = get_model_name()
    tokenizer = AutoTokenizer.from_pretrained(model_name)
	
    print(f"🔤 Using tokenizer: {model_name}")
    print(f"📄 Tokenizing file: {json_file}")
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
        chat = tokenizer.apply_chat_template(data, tokenize=tokenize)
        tokens = len(chat)
        if tokenize == False:
            tokens = len(tokenizer.encode(chat))
        print("=== Conversation: ===")
        print(chat)
        print("=== Details: ===")
        print(f"Tokenized: {tokenize}")
        print(f"Length of Characters:", len(chat))
        print(f"Total tokens:", tokens) # TODO: integrate with tokenize func

        if save is not None and tokenize == False:
            with open(save, "w") as f:
                f.write(chat)
                f.close()
            print(f"Save as file:", save)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON — {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    import fire
    fire.Fire({
        "file": tokenize,
        "chat": apply_chat_template,
    })


if __name__ == "__main__":
    main()

