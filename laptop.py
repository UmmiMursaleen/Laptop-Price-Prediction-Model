import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained Pipeline
pipe = pickle.load(open(r'LaptopPricePrediction.pkl', 'rb'))
laptop = pd.DataFrame(pickle.load(open(r'laptop.pkl', 'rb')))

st.title('Laptop Price Prediction App 💻')

brand_name = ['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
              'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
              'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG']

Typ_Name = ['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible', 'Workstation']

# User Inputs
company = st.selectbox('Brand Name', brand_name)
laptop_type = st.selectbox('Category', Typ_Name)
ram = st.selectbox('RAM in (GB)', [4, 6, 8, 12, 16, 32])
weight = st.number_input('Weight of the Laptop')
ips = 1 if st.selectbox('IPs Panel', ['Yes', 'No']) == 'Yes' else 0
touchscreen = 1 if st.selectbox('Touch Screen', ['Yes', 'No']) == 'Yes' else 0
screen_size = st.slider('Screensize in inches', 10.0, 18.0, 13.0)
resolution = st.selectbox('Screen Resolution', 
    ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', 
     '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox('CPU', laptop['Processor'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', laptop['Gpu_Brand'].unique())
os = st.selectbox('OS', laptop['Os'].unique())

if st.button('Predict Price'):
    # Extract screen resolution
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
    
    # **Convert Query to Pandas DataFrame with correct column names**
    query = pd.DataFrame([[company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
                         columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'IPS Panel', 'ppi',
                                  'Processor', 'HDD', 'SSD', 'Gpu_Brand', 'Os'])
    
    # Predict Price
    predicted_price = pipe.predict(query)[0]
    
    # **Apply np.exp() only if log transformation was used**
    st.header(f"The predicted price of this configuration is: {int(np.exp(predicted_price)) if predicted_price < 50 else int(predicted_price)}.")
