from config.settings import MODEL

def generate_response(character_name, traits, context, history, question):
    max_history = 3
    history_text = "\n".join(history[-max_history:])

    prompt = f"""
You are {character_name} from A Christmas Carol.
Personality traits: {traits}
Answer strictly using the context below. Respond in-character, politely and naturally.

Context:
{context}

Conversation history:
{history_text}

User question: {question}
"""

    response = MODEL.generate_content(prompt)
    return response.text.strip()
