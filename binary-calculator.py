import streamlit as st

def convertb(no: int) -> int:
    whole = 0
    exp = 1
    strno = str(no)
    num = 0
    place = len(strno) - 1
    placeno = len(strno)
    while place != exp:
        num = strno[-exp:-1]
        whole = whole + (num * (2 ** place))
        exp += 1
    return whole
def convertd(no: int) -> int:
    q = 1
    num = 0
    while q != 0:
        q, r = divmod(no, 2)
        no = q
        num = num + r
    return num[::-1]
st.title("A Binary Calculator")
st.write("By Bhavish\n")
st.write("Binary Convertor")
col1, col2, col3 = st.columns(3)
with col2:
    convertor = st.selectbox(label=" ", options=("Binary to Decimal", "Decimal to Binary"), index=None, label_visibility="collapsed")
with col1:
    if convertor == "Binary to Decimal":
        binary = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1b", placeholder="Enter a Binary Number...", label_visibility="collapsed")
    elif convertor == "Decimal to Binary":
        decimal = st.number_input(label=" ", min_value=0, value=None, step=1, format="%1d", placeholder="Enter a Decimal Number...", label_visibility="collapsed")
with col3:
    if convertor == "Binary to Decimal":
        num = convertb(binary)
        st.latex(num + r"_10")
    elif convertor == "Decimal to Binary":
        num = convertd(decimal)
        st.latex(num + r"_2")
