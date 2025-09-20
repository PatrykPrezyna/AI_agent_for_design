from openai import OpenAI

# Initialize client with your API key (set it as an environment variable first!)
client = OpenAI()

def simple_agent(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # lightweight, cheap model
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print(simple_agent("Hello! What can you do?"))

assistant = client.beta.assistants.create(
    name="My First Agent",
    instructions="You are a helpful assistant that explains data science concepts.",
    model="gpt-4o-mini"
)