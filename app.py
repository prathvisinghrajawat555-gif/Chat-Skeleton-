import streamlit as st

st.title("Chat Skeleton")

# User input
user_input = st.text_input("You:")

# Bot ka simple reply
if user_input:
    st.write("Bot: Hello! You said -", user_input)
  
