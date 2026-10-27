
import streamlit as st
from huggingface_hub import InferenceClient

st.title("Ghost Story Generator")

topic = st.text_input("Enter a story topic")

if st.button("Generate Story"):
    if topic.strip():
        try:
            client = InferenceClient(
                api_key=st.secrets["HF_TOKEN"]
            )

            with st.spinner("Generating story..."):
                result = client.chat_completion(
                    model="Qwen/Qwen2.5-7B-Instruct",
                    messages=[
                        {
                            "role": "user",
                            "content": "Write a short spooky story about " + topic
                        }
                    ],
                    max_tokens=300
                )

            st.write(result.choices[0].message.content)

        except Exception:
            st.error("AI failed. Check your token and model access.")
    else:
        st.warning("Enter a topic first!")

