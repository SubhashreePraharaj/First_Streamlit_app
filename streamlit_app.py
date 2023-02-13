import streamlit
streamlit.title('Subhashree')
streamlit.header('My Profile')
streamlit.text('I am a Data Engineer')
streamlit.header('🍌🥭 Stay Healthy 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
