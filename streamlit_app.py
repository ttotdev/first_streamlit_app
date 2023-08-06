import streamlit as sl
import pandas as pd

sl.title("My Parents New Healthy Diner ----")

sl.header("Breakfast Menu")

sl.text('🥣Omega 3 & Blueberry Oatmeal')
sl.text('🥗Kale, Spinach & Rocket Smoothie')
sl.text('🐔Hard-Bolied Fre-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = sl.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

sl.dataframe(fruits_to_show)

# new section to display fruityvice API response
import requests
sl.header('Fruityvice Fruit Advice!')
fruit_choice = sl.text_input('What fruit would you like information about?', 'Kiwi')
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
sl.write('The user entered', fruit_choice)

# json_normalzie convert json structure into flat table
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# output to screen as table
# set dataframe with a table from json_normalize
sl.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute('select * from fruit_load_list()')
my_data_row = my_cur.fetchone()
sl.text('The fruit load list contains:')
#sl.text("Hello from Snowflake:")
sl.text(my_data_row)


