import pandas as pd
import numpy as np
import streamlit as st
import datetime
import pickle
import json
from PIL import Image
from tensorflow.keras.models import load_model

# Load the Models
with open('final_pipeline.pkl', 'rb') as file_1:
  final_pipeline = pickle.load(file_1)
  
with open('Drop_Columns.txt','r') as file_2:
  Drop_Columns = json.load(file_2)

model_seq2 = load_model('model_seq2.h5')

def run() :
  # membuat title
  st.title('CUSTOMER CHURN PREDICTION')
  st.subheader('Predicting customer churn')
  # Menambahkan Gambar
  image = Image.open('churn.png')
  st.image(image, caption='Customer Churn')
  st.markdown('---')
  st.write("# Customer Information")

  #Form
  with st.form(key='Customer Churn'):
      user_id = st.text_input('User ID', value='')
      age = st.number_input("Customer's Age", min_value=0, max_value=100, value=25, step=1)
      gender = st.radio("Customer's gender", ('M', 'F'))
      region_category = st.radio('Region customer belongs to', ('City', 'Village', 'Town'))
      membership_category = st.selectbox("Customer's membership category", ('No Membership', 'Basic Membership', 'Silver Membership', 
                                                            'Gold Membership', 'Premium Membership', 'Platinum Membership'))
      join_date = st.date_input("Customer's join date as a member", datetime.date(2023, 6, 1))
      joined_through_referral = st.radio("Customer's using referral code when signing up", ('Yes', 'No'))
      preferred_offer_types = st.selectbox("Customer's preferrences of offers", ('Without Offers', 'Credit/Debit Card Offers', 'Gift Vouchers/Coupons'))
      medium_of_operation = st.radio('Type of medium that customer prefers', ('Desktop', 'Smartphone', 'Both'))
      internet_option = st.radio("Customer's preferrences of connection", ('Wi-Fi', 'Fiber_Optic', 'Mobile_Data'))
      last_visit_time = st.time_input('Last time customer visitting our webs', datetime.time(21, 00), step=300)
      days_since_last_login = st.number_input("Days since customers last login", min_value=0, max_value=30, value=1, step=1)
      avg_time_spent = st.number_input('Average time customer spent in the webs (minutes)', min_value=0, max_value=4000, value=10, step=1)
      avg_transaction_value = st.number_input("Customer's average transaction value", min_value=0, max_value=100000, value=0, step=1)
      avg_frequency_login_days = st.number_input("Customer's login frequency on the webs", min_value=0, max_value=100, value=0, step=1)
      points_in_wallet = st.number_input("Customer's point of transaction", min_value=0, max_value=100, value=0, step=1)
      used_special_discount = st.radio('Customer using discounts code', ('Yes', 'No'))
      offer_application_preference = st.radio("Customer using application offers", ('Yes', 'No'))
      past_complaint = st.radio("Has the customers raised complaint", ('Yes', 'No'))
      complaint_status = st.selectbox("Customer's past complain statusses", ('No Information Available', 'Not Applicable', 'Unsolved', 'Solved', 'Solved in Follow-up'))
      feedback = st.selectbox("Custome's feedback", ('Poor Website', 'Poor Customer Service', 'Too many ads', 
                                                                                 'Poor Product Quality', 'No reason specified', 'Products always in Stock', 
                                                                                 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website'))

      submitted = st.form_submit_button('Predict')

  data_inf = {
      'user_id': user_id,
      'age': age,
      'gender: ': gender,
      'region_category': region_category,
      'membership_category': membership_category,
      'join_date': join_date,
      'joined_through_referral': joined_through_referral,
      'preferred_offer_types': preferred_offer_types,
      'medium_of_operation': medium_of_operation,
      'internet_option': internet_option,
      'last_visit_time': last_visit_time,
      'days_since_last_login': days_since_last_login,
      'avg_time_spent': avg_time_spent,
      'avg_transaction_value': avg_transaction_value,
      'avg_frequency_login_days': avg_frequency_login_days,
      'points_in_wallet': points_in_wallet,
      'used_special_discount': used_special_discount,
      'offer_application_preference': offer_application_preference,
      'past_complaint': past_complaint,
      'complaint_status': complaint_status,
      'feedback': feedback

  }

  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf.T, width=800, height=495)


  if submitted:
    # Predict using created pipeline
    data_inf_drop = data_inf
    feedback_class = {
    'No reason specified': 'No reason specified',
    'Too many ads': 'Negative Feedback',
    'Poor Customer Service': 'Negative Feedback',
    'Poor Website': 'Negative Feedback',
    'Poor Product Quality': 'Negative Feedback',
    'User Friendly Website': 'Positive Feedback',
    'Quality Customer Care': 'Positive Feedback',
    'Products always in Stock': 'Positive Feedback',
    'Reasonable Price': 'Positive Feedback'
}
    data_inf_drop['feedback'] = data_inf_drop['feedback'].replace(feedback_class)
    data_inf_transform = final_pipeline.transform(data_inf_drop)
    y_pred_inf = model_seq2.predict(data_inf_transform)
    y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)
    if y_pred_inf == 0:
         pred = 'Not Churn'
    else:
         pred = 'Churn'
    st.markdown('---')
    st.write('# Prediction : ', (pred))
    st.markdown('---')

if __name__== '__main__':
    run()