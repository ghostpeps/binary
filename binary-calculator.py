import streamlit as st

def convertd(no: int) -> str:
    if no is not None:
        if no < 0:
            return "Input must be a non-negative integer."
        
        if no == 0:
            return "0"
        
        binary_digits = []
        
        while no > 0:
            binary_digits.append(str(no % 2))
            no //= 2
        
        binary_digits.reverse()
        return ''.join(binary_digits)
st.title("A Binary Calculator")
st.write("By Bhavish\n")
st.write("Binary Convertor")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
with col2:
    convertor = st.selectbox(label=" ", options=("Binary to Decimal", "Decimal to Binary"), index=None, label_visibility="collapsed")
with col1:
    if convertor == "Binary to Decimal":
        binary = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1d", placeholder="Enter a Binary Number...", label_visibility="collapsed")
    elif convertor == "Decimal to Binary":
        decimal = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1d", placeholder="Enter a Decimal Number...", label_visibility="collapsed")
with col3:
    if convertor == "Binary to Decimal":
        if binary is None:
            st.write("Decimal Number comes out here...")
        elif binary is not None:
            try:
                num = int(str(binary), 2)
            except ValueError:
                st.write("Please enter a valid binary number...")
            else:
                num = int(str(binary), 2)
                st.write(f"{num}₁₀")
    elif convertor == "Decimal to Binary":
        num = convertd(decimal)
        if num is None:
            st.write("Binary Number comes out here...")
        elif num is not None:
            st.write(f"{num}₂")
with col4:
    num_one = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1d", placeholder="Enter a your first Binary Number...", label_visibility="collapsed")
with col5:
    operation = st.selectbox(label=" ", options=("Addition (+)", "Subtract (-)", "Multiply (×)", "Division (÷)", "Exponent (xʸ)", "AND (&)", "OR (|)", "NOT (~)", "XOR (^)", "Arithmetic Left Shift (<<)", "Arithmetic Right Shift (>>)", "Logical Left Shift (<<<)", "Logical Right Shift (>>>)"), index=None, placeholder="Choose an operation...", label_visibility="collapsed")
with col6:
    if operation == "NOT (~)":
        st.write()
    elif operation != "NOT (~)":
        num_two = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1d", placeholder="Enter a your second Binary Number...", label_visibility="collapsed")
