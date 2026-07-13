import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Clasificador de Pinguinos')
st.write('Esta app usa 6 entradas para predecir las especies de pinguinos usando'
         'un modelo construido sobre el conjunto de datos Pinguinos Palmer. use la forma abajo'
         ' para empezar')


penguin_file = st.file_uploader('Cargar su propio datos de pinguino')

if penguin_file is None:
    rf_pickle = open('random_forest_penguin.pickle', 'rb')
    map_pickle = open('output_penguin.pickle', 'rb')
    rfc = pickle.load(rf_pickle)
    unique_penguin_mapping = pickle.load(map_pickle)
    rf_pickle.close()
    map_pickle.close()
else:
    penguin_df = pd.read_csv(penguin_file)
    penguin_df = penguin_df.dropna()
    output = penguin_df['species']
    features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]
    features = pd.get_dummies(features)
    output, unique_penguin_mapping = pd.factorize(output)
    x_train, x_test, y_train, y_test = train_test_split(features, output, test_size = .8)
    rfc = RandomForestClassifier(random_state=15)
    rfc.fit(x_train.values, y_train)
    y_pred = rfc.predict(x_test.values)
    score = round(accuracy_score(y_pred, y_test), 2)
   
    st.write(
        f"""Entrenamos un modelo Random Forest sobre estos datos, tiene una puntuación de {score} ! 
        Use la entrada abajo para entrenar el modelo """
    )

    with st.form('user_inputs'):
        island = st.selectbox('Isla pinguino', options=['Biscoe', 'Dream', 'Torgerson'])
        sex = st.selectbox('Sexo', options=['Female', 'Male'])
        bill_length = st.number_input('Longitud del pico (mm)', min_value=0)
        bill_depth = st.number_input('Profundidad del pico (mm)', min_value=0)
        flipper_length = st.number_input('Longitud aleta (mm)', min_value=0)
        body_mass = st.number_input('Masa corporal (g)', min_value=0)
        st.form_submit_button()
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
            
        new_prediction = rfc.predict(
            [
                [
                    bill_length, 
                    bill_depth, 
                    flipper_length, 
                    body_mass, 
                    island_biscoe, 
                    island_dream, 
                    island_torgerson, 
                    sex_female, 
                    sex_male
                ]
            ]
        )
        
        prediction_species = unique_penguin_mapping[new_prediction][0]
        st.write(f'Predecimos su pinguino es del {prediction_species} especie')







