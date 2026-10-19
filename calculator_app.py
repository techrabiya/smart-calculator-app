import streamlit as st

st.title("🧮 Smart Calculator & Unit Converter")

option = st.sidebar.selectbox("Choose Mode", ["Basic Calculator", "Length Converter"])

if option == "Basic Calculator":
    st.header("Basic Calculator")
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Division by zero is not allowed!")

elif option == "Length Converter":
    st.header("Length Converter (Meters to Feet)")
    meters = st.number_input("Enter length in meters", value=0.0)
    if st.button("Convert"):
        feet = meters * 3.28084
        st.success(f"{meters} meters is equal to {feet:.2f} feet.")
