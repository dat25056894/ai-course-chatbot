import streamlit as st
from openai import OpenAI

# Initialize OpenAI client (replace with your API key)
client = OpenAI(api_key="YOUR_API_KEY")

# App title
st.title("🤖 AI Course Assistant")

st.write("Ask me anything about Artificial Intelligence!")

# User input
question = st.text_input("Enter your question:")

# Generate response
if question:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI tutor that explains AI concepts in a simple and clear way for students."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content
    st.write("### 📘 Answer:")
    st.write(answer)
