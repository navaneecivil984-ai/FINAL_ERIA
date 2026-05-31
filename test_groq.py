from groq import Groq

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Say Hello"}
    ]
)

print(response.choices[0].message.content)