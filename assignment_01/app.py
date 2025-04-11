import streamlit as st

st.title("🚀 Streamlit Crash Course")
st.header("Welcome to Your First Web App!")
st.write("This is a beginner-friendly tutorial for creating Python-powered web apps with Streamlit.")

# Add an input
name = st.text_input("What's your name?")
if name:
    st.success(f"Nice to meet you, {name}! 👋")

# Add a button
if st.button("Click Me"):
    st.balloons()

# Add a slider
age = st.slider("Select your age", 1, 100)
st.write(f"You're {age} years young! 🎂")
import pandas as pd
import numpy as np

st.subheader("📈 Random Data Plot")
data = pd.DataFrame({
    'a': np.random.randn(50),
    'b': np.random.randn(50)
})
st.line_chart(data)
