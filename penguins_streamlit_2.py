import streamlit as st
import pickle

rf_pickle = open('random_forest_penguin.pickle', 'rb')
map_pickle = open('output_penguin.pickle', 'rb')

rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()

island = st.selectbox('Isla pinguino', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Sexo', options=['Female', 'Male'])
bill_length = st.number_input('Longitud del pico (mm)', min_value=0)
bill_depth = st.number_input('Profundidad del pico (mm)', min_value=0)
flipper_length = st.number_input('Longitud aleta (mm)', min_value=0)
body_mass = st.number_input('Masa corporal (g)', min_value=0)

user_input = [island, sex, bill_length, bill_depth, flipper_length, body_mass]
st.write(f"""Las entradas del usuario son {user_input}""".format())




