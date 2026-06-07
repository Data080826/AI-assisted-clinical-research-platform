from openai import OpenAI

def ask_ai(prompt, api_key):

    try:

        client = OpenAI(
            api_key=api_key
        )

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"
