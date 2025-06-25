import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier

# imprt the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

# Brand
Company = st.selectbox('Brand',df['Company'].unique())

# Type of  laptop
Type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

#Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen Size
screen_size  = st.number_input('Screen Size (in inches)', min_value=0.1, step=0.1)

# Resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900',
            '3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# CPU
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
      
    
 # query
 ppi = None
if touchscreen == 'Yes':
        touchscreen = 1
else:
        touchscreen = 0

if ips == 'yes':
        ips = 1
else:
        ips = 0
X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])

ppi = ((X_res**2)+(Y_res**2))**0.5 / screen_size

query_df = pd.DataFrame([[
        Company, Type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os
    ]], columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'ppi',
                 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])
    
prediction =(np.exp(pipe.predict(query_df)))[0]
st.success(f"Estimated Laptop Price: ₹ {int(prediction)}")




