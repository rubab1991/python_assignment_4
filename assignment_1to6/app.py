import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Home
if section == "Home":
    st.title("👋 Hello, I'm Rubab!")
    st.subheader("Frontend Developer | AI & Web3 Enthusiast")
    st.write("Welcome to my portfolio website built with Streamlit.")
    st.image("https://picsum.photos/400", caption="Just a placeholder image")

# About
elif section == "About":
    st.header("About Me")
    st.write("""
    I'm passionate about building interactive websites using **Next.js, TypeScript, and Tailwind CSS**.
    I'm currently a student at GIAIC studying **AI, Web 3.0, and Metaverse**.
    """)
    st.download_button("📄 Download My Resume", "Fake_Resume_Content", file_name="Rubab_Resume.pdf")

# Projects
elif section == "Projects":
    st.header("Projects")
    st.write("- 🎈 Birthday Wish App")
    st.write("- 🎮 Number Guessing Game")
    st.write("- 📺 Netflix Clone")
    st.write("- 🛍️ E-commerce Dashboard")

# Contact
elif section == "Contact":
    st.header("Contact Me")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        if name and email and message:
            st.success("✅ Message sent! (Just simulated)")
        else:
            st.warning("⚠️ Please fill out all fields.")
