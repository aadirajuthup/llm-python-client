import openai

openai.api_key = ""
openai.api_base = "http://api.airlinkssystems.co.in/v1"

def main():
    chat_completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            #{'role': 'system', 'content': "Your system prompt here."},
            {'role': 'user', 'content': "Your prompt here."},
        ],
    )

    if isinstance(chat_completion, dict):
        # Not streaming
        print(chat_completion.choices[0].message.content)
    else:
        # Streaming
        for token in chat_completion:
            content = token["choices"][0]["delta"].get("content")
            if content is not None:
                print(content, end="", flush=True)

if __name__ == "__main__":
    main()
