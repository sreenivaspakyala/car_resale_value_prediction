import streamlit as st
import pickle
import numpy as np
import datetime as dt
import sklearn

current_year = dt.date.today().year

rf_model = pickle.load(open('car_resale_value_predictor.pkl','rb'))

st.title("Car Re-Sale Value Predictor")
st.subheader("Check your Car's Re-Sale value with just a few clicks")

with st.form("Car Re-Sale Value Predictor"):
    st.write("Please fill all these details of your car to get your car's re-sale value")
    Present_Price = st.number_input("Enter the present price of the Car")
    Kms_Driven = st.number_input("Enter the Kms Driven by the car")

    col1, col2, col3 = st.columns(3)

    with col1:
        Fuel_Type = st.selectbox(
            'Select the Fuel type of the car',
            ('0 - CNG', '1 - Diesel', '2 - Petrol'))

    with col2:
        Transmission_Type = st.selectbox(
            'Select the Transmission type of the car',
            ('0 - Automatic', '1 - Manual'))

    with col3:
        Seller_Type = st.selectbox(
            'Select the Seller type',
            ('0 - Dealer', '1 - Individual'))

    Owner = st.number_input("Enter the Number of previous Owners of the car")
    year = st.number_input("Enter the Year in which the year the car is purchased")
    fuel = Fuel_Type[0]
    transmission = Transmission_Type[0]
    seller = Seller_Type[0]
    years_diff = current_year - year

    input_list = [float(Present_Price),float(Kms_Driven),int(fuel),int(seller),int(transmission),int(Owner),years_diff]
    input_arr = np.array(input_list)
    re_sale_price = np.round(rf_model.predict(input_arr.reshape(1,-1))[0],2)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("The Re-Sale Value of your car is : ",re_sale_price,"Lakhs")

st.subheader("Thank You!  Visit Again !",)
