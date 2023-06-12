import streamlit as st
import pandas as pd
import numpy as np
import json
import joblib

# load file joblib dengan .pkl
with open('model_svm.pkl', 'rb') as file_1:
  model_svm= joblib.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler=joblib.load(file_2)

with open('list_num_cols.txt', 'r') as file_3:
  num_cols= json.load (file_3)

with open('list_cat_columns.txt', 'r') as file_4:
  cat_cols= json.load (file_4)

def run() :

  with st.form(key='Hotel Bookings'):
      Booking_ID = st.text_input('Booking ID', value='')
      no_of_adults = st.number_input('No of Adults', min_value=0, max_value=3, value=1, step=1)
      no_of_children = st.number_input('No of Childrens', min_value=0, max_value=3, value=1, step=1)
      no_of_weekend_nights = st.number_input('No of Weekend Nights', min_value=0, max_value=10, value=1, step=1)
      no_of_week_nights = st.number_input('no_of_week_nights', min_value=0, max_value=25, value=1, step=1)
      st.markdown('---')
      
      avg_price_per_room = st.slider('Room Price', 1, 600, 100)
      lead_time = st.slider('Lead Time', min_value=0, max_value=450, value=1)
      arrival_year = st.slider('Arrival Year', 2023, 2025, 2023)
      arrival_month = st.slider('Arrival Month', 1, 12, 1)
      arrival_date = st.slider('Arrival Date', 1, 31, 1)     
      no_of_previous_cancellations = st.slider('Previous Cancellations', 0, 20, 0)
      no_of_previous_bookings_not_canceled = st.slider('Previous Not Cancellations', 0, 50, 0)
      no_of_special_requests = st.slider('Special Request', 0, 5, 0) 
      st.markdown('---')

      type_of_meal_plan = st.selectbox('Meal Plan', ('Meal Plan 1', 'Meal Plan 2','Meal Plan 3','Not Ordering'), index=1)
      required_car_parking_space = st.selectbox('Car Parking Space', ('No', 'Yes'), index=1)
      room_type_reserved = st.selectbox('Room Type', ('Room_Type 1', 'Room_Type 2','Room_Type 3','Room_Type 4','Room_Type 5','Room_Type 6','Room_Type 7'), index=1)
      market_segment_type = st.selectbox('Market Segment Type', ('Offline' ,'Online' ,'Corporate' ,'Aviation' ,'Complementary'), index=1)
      repeated_guest = st.selectbox('Repeated Guest', ('No', 'Yes'), index=1)

      submitted = st.form_submit_button('Predict')

  data_inf = {
      'Booking_ID': Booking_ID,
      'no_of_adults': no_of_adults,
      'no_of_children: ': no_of_children,
      'no_of_weekend_nights': no_of_weekend_nights,
      'no_of_week_nights': no_of_week_nights,
      'avg_price_per_room': avg_price_per_room,
      'lead_time': lead_time,
      'arrival_year': arrival_year,
      'arrival_month': arrival_month,
      'arrival_date': arrival_date,
      'no_of_previous_cancellations': no_of_previous_cancellations,
      'no_of_previous_bookings_not_canceled': no_of_previous_bookings_not_canceled,
      'no_of_special_requests': no_of_special_requests,
      'type_of_meal_plan': type_of_meal_plan,
      'required_car_parking_space': required_car_parking_space,
      'room_type_reserved': room_type_reserved,
      'market_segment_type': market_segment_type,
      'repeated_guest': repeated_guest

  }

  data_inf = pd.DataFrame([data_inf])
  data_inf


  if submitted:
    #Numerical Columns
    data_inf_num = data_inf[num_cols]
    #data_inf_cat = data_inf[cat_cols]
    data_inf_final= data_inf.copy()
    # Feature Scaling
    data_inf_final[num_cols]= model_scaler.transform(data_inf_num)

    selected_columns = ['lead_time', 'no_of_special_requests', 'avg_price_per_room', 'repeated_guest', 'no_of_week_nights']
    data_inf_final = data_inf_final[selected_columns]

    # Convert the string "No" to a float
    data_inf_final['lead_time'] = data_inf_final['lead_time'].replace('No', '0')
    data_inf_final['no_of_special_requests'] = data_inf_final['no_of_special_requests'].replace('No', '0')
    data_inf_final['avg_price_per_room'] = data_inf_final['avg_price_per_room'].replace('No', '0')
    data_inf_final['repeated_guest'] = data_inf_final['repeated_guest'].replace('No', '0')
    data_inf_final['no_of_week_nights'] = data_inf_final['no_of_week_nights'].replace('No', '0')

    # Convert the string "Yes" to a float
    data_inf_final['lead_time'] = data_inf_final['lead_time'].replace('Yes', '1')
    data_inf_final['no_of_special_requests'] = data_inf_final['no_of_special_requests'].replace('Yes', '1')
    data_inf_final['avg_price_per_room'] = data_inf_final['avg_price_per_room'].replace('Yes', '1')
    data_inf_final['repeated_guest'] = data_inf_final['repeated_guest'].replace('Yes', '1')
    data_inf_final['no_of_week_nights'] = data_inf_final['no_of_week_nights'].replace('Yes', '1')
    
    
    # Predict using SVM
    y_pred_inf = model_svm.predict(data_inf_final)
    prediction_label = "Worried about canceling the books" if y_pred_inf == 0 else "Not gonna canceling the books"
    st.write('# Rating : ', prediction_label)

if __name__== '__main__':
    run()