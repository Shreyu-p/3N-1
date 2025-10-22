import streamlit as st

a = st.number_input("Enter a number: ")
a = int(a)
while True:
    if a == 1:
        break
    else:
        if a % 2 == 0:
            a = a // 2
            st.write(a)
        else:
            a = a * 3 + 1
            st.write(a)
