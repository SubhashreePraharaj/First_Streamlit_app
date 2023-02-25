import streamlit
streamlit.title('Subhashree')
streamlit.header('My Profile')
streamlit.text('I am a "Happy-Go-Lucky" person')
streamlit.header('🍌🥭 Stay Healthy 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
streamlit.text(fruityvice_response.json())
streamlit.dataframe(fruityvice_response)

