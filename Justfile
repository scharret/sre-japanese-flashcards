set dotenv-load := true

PYTHON := "python3.14"
VENV := ".venv"

create-env:
    uv venv {{VENV}} --python={{PYTHON}}
    uv run pdm install
    just add genanki

add pkg:
    uv run pdm add {{pkg}}

build:
    uv run python sre_japanese_flashcards.py

clean:
    rm -rf {{VENV}}

