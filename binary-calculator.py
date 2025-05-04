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

def float_to_binary(number):
    integer_part = int(number)
    fractional_part = number - integer_part
    
    integer_binary = bin(integer_part)[2:]
    fractional_binary = ""
    
    while fractional_part and len(fractional_binary) < 10:
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += "1"
            fractional_part -= 1
        else:
            fractional_binary += "0"
            
    if fractional_binary:
        return integer_binary + "." + fractional_binary
    else:
        return integer_binary


def convert(num_one, num_two, operation) -> str:
    try:
        x = int(str(num_one), 2) + int(str(num_two), 2)
    except ValueError:
        if num_one is None and num_two is None:
            st.write("Please check/enter both of your **binary** numbers...")
        elif num_one is None:
            st.write("Please check/enter your first **binary** number...")
        elif num_two is None:
            st.write("Please check/enter your second **binary** number...")
    else:
        if operation == "Addition (+)":
            whole = int(str(num_one), 2) + int(str(num_two), 2)
            no = convertd(whole)
            opr = "+"
        elif operation == "Subtract (-)":
            whole = int(str(num_one), 2) - int(str(num_two), 2)
            no = convertd(whole)
            opr = "-"
        elif operation == "Multiply (×)":
            whole = int(str(num_one), 2) * int(str(num_two), 2)
            no = convertd(whole)
            opr = "×"
        elif operation == "Division (÷)":
            whole = int(str(num_one), 2) / int(str(num_two), 2)
            no = float_to_binary(whole)
            opr = "÷"
        elif operation == "Exponent (xʸ)":
            whole = int(str(num_one), 2) ** int(str(num_two), 2)
            no = convertd(whole)
            return r"$\mathsf{{" + str(num_one) + "_2}^{" + str(num_two) + "_2}} = " + str(no) + "_2$"
        elif operation == "AND (&)":
            no = num_one & num_two
            opr = "&"
        elif operation == "OR (|)":
            no = num_one | num_two
            opr = "|"
        elif operation == "NOT (~)":
            no = ~num_one
        elif operation == "XOR (^)":
            no = num_one ^ num_two
            opr = "^"
        elif operation == "Arithmetic Left Shift (<<)":
            no = convertd(num_one << num_two)
            opr = "<<"
        elif operation == "Arithmetic Right Shift (>>)":
            no = convertd(num_one >> num_two)
            opr = ">>"
        if operation == "Exponent (xʸ)" or operation == "NOT (~)":
            if operation == "NOT (~)":
                return f"~{num_one}₂ = {no}₂"
        elif operation != "Exponent (xʸ)" and operation != "NOT (~)":
            return f"{num_one}₂ {opr} {num_two}₂ = {no}₂"
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
                numone = str(binary)
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
    operation = st.selectbox(label=" ", options=("Addition (+)", "Subtract (-)", "Multiply (×)", "Division (÷)", "Exponent (xʸ)", "AND (&)", "OR (|)", "NOT (~)", "XOR (^)", "Arithmetic Left Shift (<<)", "Arithmetic Right Shift (>>)"), index=None, placeholder="Choose an operation...", label_visibility="collapsed")
with col6:
    if operation == "NOT (~)":
        st.write()
    elif operation != "NOT (~)":
        num_two = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1d", placeholder="Enter a your second Binary Number...", label_visibility="collapsed")
if operation is not None:
    try:
        x = int(str(num_one), 2)
    except ValueError:
        if num_one is None and num_two is None:
            st.write("Please check/enter both of your **binary** numbers...")
        elif num_one is None:
            st.write("Please check/enter your first **binary** number...")
        elif num_two is None:
            st.write("Please check/enter your second **binary** number...")
    else:
        if operation == "NOT (~)":
            no = convert(num_one, 0, operation)
            st.write(no)
        elif operation != "NOT (~)":
            no = convert(num_one, num_two, operation)
            st.write(no)
