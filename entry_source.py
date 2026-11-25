import os
from pathlib import Path

ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
CANDIDATE_WORD = "queue"
MAX_LENGTH = 77
MIN_LENGTH = 1

def choose_word():
    word = CANDIDATE_WORD.strip()
    normalized = word.lower()
    assert MIN_LENGTH <= len(normalized) <= MAX_LENGTH
    assert normalized.isalpha()
    assert " " not in normalized
    return normalized

def resolve_output_dir():
    raw = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR)
    directory = Path(raw).expanduser()
    directory.mkdir(parents=True, exist_ok=True)
    return directory

def write_entry():
    text = choose_word()
    output_dir = resolve_output_dir()
    target = output_dir / ENTRY_FILENAME
    target.write_text(text, encoding="utf-8")
    return target

def main():
    target = write_entry()
    written = target.read_text(encoding="utf-8")
    assert written == choose_word()

if __name__ == "__main__":
    main()
