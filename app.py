import streamlit as st 
st.title("power calculator")
st.write("enter a number to calculate its square , cube and fifth power ")


n=st.number_input("enter an integerr",value=1, step=1)


square=n**2
cube=n**3
fifth_power=n**5 


st.write(f"the square of a {n} is :{square}")

st.write(f"the cube of a {n} is :{cube}")
         
st.write(f"the fifth power of a {n} is :{fifth_power}")