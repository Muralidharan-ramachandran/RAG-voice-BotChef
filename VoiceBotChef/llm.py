import ollama

def ask_llm(context, question):

    prompt = f"""
You are a helpful cooking assistant.

Use this recipe to answer the question.

Recipe:
{context}

Question:
{question}

Answer clearly in steps.
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]