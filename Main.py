import openai

openai.api_key = "ENTER-THE-API-KEY-HERE"
for i in range(1000):
    prompt = input("Enter the prompt:")
    print("loading...")
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ],
    )
    print("-----CHAT-GPT-3.5-TURBO-----")
    print(res["choices"][0]["message"]["content"])
    print("----------------------------")
