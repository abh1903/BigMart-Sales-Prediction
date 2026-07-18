
import streamlit as st
import pickle
import pandas as pd

with open('bigmart_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('columns.pkl', 'rb') as f:
    cols = pickle.load(f)

st.title('BigMart Sales Prediction')

item_weight = st.number_input('Item Weight', min_value=0.0, value=12.0)
item_visibility = st.number_input('Item Visibility', min_value=0.0, value=0.05)
item_mrp = st.number_input('Item MRP', min_value=0.0, value=150.0)
outlet_year = st.number_input('Outlet Establishment Year', min_value=1990, max_value=2024, value=2010)

item_fat = st.selectbox('Item Fat Content', ['Low Fat', 'Regular'])
outlet_size = st.selectbox('Outlet Size', ['Small', 'Medium', 'High'])
outlet_location = st.selectbox('Outlet Location Type', ['Tier 1', 'Tier 2', 'Tier 3'])
outlet_type = st.selectbox('Outlet Type', ['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])
item_type = st.selectbox('Item Type', ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene', 'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood'])

if st.button('Predict Sales'):
    input_data = {
        'Item_Weight': item_weight,
        'Item_Visibility': item_visibility,
        'Item_MRP': item_mrp,
        'Outlet_Establishment_Year': outlet_year,
        'Item_Fat_Content_' + item_fat: 1,
        'Outlet_Size_' + outlet_size: 1,
        'Outlet_Location_Type_' + outlet_location: 1,
        'Outlet_Type_' + outlet_type: 1,
        'Item_Type_' + item_type: 1,
    }
    input_df = pd.DataFrame([input_data])
    for col in cols:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[cols]
    pred = model.predict(input_df)
    st.success(f'Predicted Sales: Rs {pred[0]:,.2f}')
