#!/usr/bin/env python3
import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".cache" / "tokenize-cli" / "config.json"


def config(model: str = None):
    """
    Configure or inspect the tokenizer model.

    Usage:
      tokenize-cli --model <MODEL>
      tokenize-cli
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    if model:
        with open(CONFIG_PATH, "w") as f:
            json.dump({"tokenizer_model": model}, f)
        print(f"✅ Saved tokenizer config: {model}")
    else:
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH) as f:
                data = json.load(f)
            print(f"📄 Current config: {data}")
        else:
            print("⚠️  No tokenizer set. Run 'tokenize-cli --model <MODEL>'.")

def main():
    import fire
    fire.Fire(config)

if __name__ == "__main__":
    main()
