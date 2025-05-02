import streamlit as st

def convertb(no):
    whole = 0
    exp = 0
    strno = str(no)
    num = 0
    place = len(str(no)) - 1
    placeno = len(str(no))
    while place != exp:
        num = strno[-placeno:-1]
        whole = whole + num * 2 ** place
st.title("A Binary Calculator")
st.write("By Bhavish\n")
st.write("Binary Convertor")
col1, col2, col3 = st.columns(3)
with col2:
    convertor = st.selectbox(options=("Binary to Decimal", "Decimal to Binary"), index=None)
with col1:
    if convertor == "Binary to Decimal":
        binary = st.number_input(min_value=0, value=None, step=1, format="%1b", placeholder="Enter a Binary Number...")
    elif convertor == "Decimal to Binary":
        decimal = st.number_input(min_value=0, value=None, step=1, format="%1d", placeholder="Enter a Decimal Number...")
with col3:
    if convertor == "Binary to Decimal":
        num = convertb(binary)
        st.latex(num + r"_10")
    elif convertor == "Decimal to Binary":
        num = convertd(decimal)
        st.latex(num + r"_2")
