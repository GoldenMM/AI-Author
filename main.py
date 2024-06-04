from openai import OpenAI
import os

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def generate_text(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content



print(generate_text("This is a test"))