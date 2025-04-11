import streamlit as st

# App title
st.title("💪 BMI Calculator")

# User input
st.header("Enter your details:")
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, step=1.0)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, step=1.0)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI categories
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid height and weight.")
