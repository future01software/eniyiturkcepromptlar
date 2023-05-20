name: ChatGPT Interaction

on:
  push:
    branches:
      - main

jobs:
  interaction:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install transformers

      - name: Run ChatGPT interaction
        run: |
          python chat_interaction.py
