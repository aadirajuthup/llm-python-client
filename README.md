Overview
--------

This project is a simple chat completion client using a private api proxy that has a lot of language models including gpt-3.5-turbo, gpt-4, and other opensource models as well. It allows users to input a prompt and receives possible completions from the models.

Features
--------

* Uses a private api proxy for chat completion
* Supports both non-streaming and streaming mode
* Allows users to select one of the provided choices or input their own response

Getting Started
---------------

1. Clone the repository and install dependencies using `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
2. Set the `API KEY` in `openai.api_key = ""` to the API given to you.
3. Run the script using `python main.py`