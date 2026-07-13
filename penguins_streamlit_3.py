import streamlit as st
import pickle

st.title('Clasificador de Pinguinos')
st.write('Esta app usa 6 entradas para predecir las especies de pinguinos usando'
         'un modelo construido sobre el conjunto de datos Pinguinos Palmer. use la forma abajo'
         ' para empezar')

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
island_biscoe, island_dream, island_torgerson = 0, 0, 0

if island == 'Biscoe':
    island_biscoe = 1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgerson':
    island_torgerson = 1
sex_female, sex_male = 0, 0

if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male = 1

new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length, body_mass, island_biscoe, island_dream, island_torgerson, sex_female, sex_male]])

prediction_species = unique_penguin_mapping[new_prediction][0]

st.write(f'Predecimos su pinguino es del {prediction_species} especie')







