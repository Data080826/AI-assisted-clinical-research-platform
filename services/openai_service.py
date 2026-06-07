from openai import OpenAI
import streamlit as st

def ask_ai(prompt):

    try:

        client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
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
