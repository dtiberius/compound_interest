import streamlit as st
from calculator import monthly_compound_interest

st.title("Compound Interest Calculator")

initial = st.number_input('Initial inestment', min_value=0, max_value=200000000)
monthly = st.number_input('Monthly deposit', min_value=0, max_value=200000000)
years = st.number_input('Years investing', min_value=0, max_value=100000)
annual_rate = st.number_input('Estimated annual percentage rate of return: ', min_value=0, max_value=1000)

total = round(monthly_compound_interest(initial, monthly, years, annual_rate),2)

st.markdown(f'After {int(years)} years you would have £{"{:,}".format(total)} :sunglasses:')