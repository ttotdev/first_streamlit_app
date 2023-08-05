import streamlit as sl
import pandas as pd

sl.title("My Parents New Healthy Diner")

sl.header("Breakfast Menu")

sl.text('🥣Omega 3 & Blueberry Oatmeal')
sl.text('🥗Kale, Spinach & Rocket Smoothie')
sl.text('🐔Hard-Bolied Fre-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = sl.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

sl.dataframe(fruits_to_show)

# new section to display fruityvice API response
import requests
sl.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
sl.text(fruityvice_response.json()) 
