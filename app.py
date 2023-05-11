import streamlit as st
import os

os.environ["OPENAI_API_KEY"] = st.secrets.my_key

from generate_chains import task_prompt, audit_prompt, task_chain, audit_chain

# Set up the Streamlit layout
st.title("Can JSON stop attacks?")

# Sidebar for API key input
api_key = st.sidebar.text_input("Enter your API key")

# Set the API key in the environment variable
if api_key == st.secrets.password:
    os.environ["OPENAI_API_KEY"] = st.secrets.my_key
else:
    os.environ["OPENAI_API_KEY"] = api_key

# User input
user_input = st.text_input("Enter your prompt")

# Task agent column
st.header("Task agent")
with st.expander("Compiled prompt"):
    st.text(task_prompt.format(prompt=user_input))
with st.subheader("Output"):
    st.text(task_chain.run(user_input))

# Audit agent column
st.header("Audit agent")
with st.expander("Compiled prompt"):
    st.text(audit_prompt.format(prompt=user_input))
with st.subheader("Output"):
    st.text(audit_chain.run(user_input))