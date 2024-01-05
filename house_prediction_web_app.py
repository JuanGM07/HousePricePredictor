# -*- coding: utf-8 -*-
"""house_prediction_web_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RxK0K9DJ6Gr0WxUpOdFM6FvUADbaqPYQ
"""
import numpy as np
import pickle
import streamlit as st

imagen="edif.jpg"
logo="cover.png"
icono="house.jpg"
path="house_price_predictor.sav"
loaded_house_price_model=pickle.load(open(path,'rb'))

st.set_page_config(page_title="House Price Predictor",
                   page_icon=icono,
                   layout="centered",
                   initial_sidebar_state="auto"
                                       
                    )


def house_price_prediction(input_data,loaded_house_price_model):
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=loaded_house_price_model.predict(input_data_reshaped)
  return prediction


def main ():
  st.image('cover-superdark.png',width=None)
  st.write("Hello, I am Juan Gonzalez, engineer student and data scientist.")
  st.write('For any request my e-mail is: juanglezm3@gmail.com.')
  st.title ('House Price Prediction')
  st.markdown("This House Price Predictor is based on the prices of houses in California")
  st.divider()
  st.subheader('Fill all the missing slots to have the price prediction')
  st.caption('¿How much Square Feets does the house have?')
  SquareFeet=st.number_input('SquareFeet', min_value=10, max_value=5000)
  st.caption('¿How many bedrooms does the house have?')
  Bedrooms=st.number_input('Bedrooms', min_value=1, max_value=10)
  st.caption('¿How many bathrooms does the house have?')
  Bathrooms=st.number_input('Bathrooms', min_value=1, max_value=10)
  opciones_barrios = ['Select a neighborhood','Suburban', 'Urban', 'Rural']
  st.caption('¿In which neighborhood is located the house?')
  barrio_elegido = st.selectbox('Neighborhood',opciones_barrios,index=0)
  mapeo_valores = {'Suburban': 0, 'Rural': 1, 'Urban': 2}
  if barrio_elegido != 'Select a neighborhood':
    Neighborhood = mapeo_valores[barrio_elegido]
  else:
    Neighborhood = None
  st.caption('¿When was the house built (From 1950 to 2020)?')
  YearBuilt=st.number_input('YearBuilt', min_value=1950, max_value=2020)

  diagnosis=''
  if st.button('House Price Prediction',type='primary'):
    diagnosis=house_price_prediction([SquareFeet,Bedrooms,Bathrooms,Neighborhood,YearBuilt],loaded_house_price_model)
    st.subheader(f"The house would have an approximate cost of :green[{diagnosis[0]:,.2f}] $",divider='grey')

    

if __name__=='__main__':
  main()
