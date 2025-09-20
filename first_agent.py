import os
from openai import OpenAI

# Load your API key from the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat():
    print("🤖 AI Agent ready! Type 'exit' to quit.\n")
    messages = []  # keeps conversation memory

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "q"]:
            print("Agent: Goodbye! 👋")
            break

        # Add user message to conversation
        messages.append({"role": "user", "content": user_input})

        # Get response
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # fast & cost-efficient
            messages=messages
        )

        answer = response.choices[0].message.content
        print(f"Agent: {answer}\n")

        # Add assistant response to conversation memory
        messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    chat()