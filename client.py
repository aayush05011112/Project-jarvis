from openai import OpenAI
client=OpenAI(
api_key="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",)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful virtual assistant named jarvis skilled in general task like Alexa and google assistant."},
        {
            "role": "user", "content": "What is AI."
        }
    ]
)

print(completion.choices[0].message.content)
