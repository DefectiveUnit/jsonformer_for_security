from generate_chains import task_prompt, audit_prompt, task_chain, audit_chain
import streamlit as st

# Set up the Streamlit layout
st.title("Agent App")

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