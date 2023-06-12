import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'Hotel Bookings - EDA',
    initial_sidebar_state = 'expanded'
)

def run() :
    
    # Membuat Title
    st.title('Hotel Bookings Prediction')

    # Membuat Sub Header
    st.subheader('EDA untuk Analisa Dataset Hotel Bookings')

    # Menambahkan Gambar
    image = Image.open('Online-Hotel-Booking.jpg')
    st.image(image, caption='Hotels Reservation')

    # Menambahkan Deskripsi
    st.write('Page ini dibuat oleh **Satriya Fauzan Adhim**')

    st.markdown('---')

    st.write('## Background')
    st.write('''In the hospitality industry, hotels often face the challenge of managing reservations effectively. 
                Understanding whether a guest is likely to cancel their reservation can greatly assist hotels in 
                optimizing their operations, managing resources efficiently, and minimizing revenue loss. 
                As a data scientist, my goal is to develop a classification model that can predict whether a guest will 
                cancel their hotel reservation or not.''')
    st.write('## Problem Statement')
    st.write('''The problem at hand is to predict whether a guest will cancel their hotel reservation based 
                on various factors present in the dataset. By leveraging historical data, we aim to build a 
                reliable classification model that can assist hotels in identifying potential cancellations early on, 
                allowing them to take appropriate measures to mitigate the impact.''')
    
    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
    The objective of this modeling effort is to utilize the Support Vector Machine (SVM) 
    algorithm for classification purposes. The SVM model has been selected due to its ability to handle complex decision 
    boundaries and its effectiveness in handling high-dimensional datasets like the one at hand. To ensure the robustness 
    and generalizability of the model, we have performed feature selection using cross-validation techniques and fine-tuned 
    the model using GridSearchCV for optimal hyperparameter settings.

    By leveraging this classification model, hotels can proactively identify reservations at risk of cancellation 
    and allocate their resources accordingly. This will enable them to optimize their operations, enhance customer 
    satisfaction, and maximize revenue by minimizing the impact of cancellations.

    '''

    # Show DataFrame
    data_url = 'https://raw.githubusercontent.com/kodokgodog/Latihan_hactiv8/main/Hotel%20Reservations.csv'
    data = pd.read_csv(data_url)
    st.dataframe(data)

    # Membuat Barplot
    st.write('#### Plot booking_status')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='booking_status', data=data)
    st.pyplot(fig)

    st.write(
    '''
    Based on the number of guests who cancel their hotel bookings, it can be observed that the quantity is quite significant. 
    This can potentially cause financial losses to the hotel if not addressed and managed properly within a well-structured 
    booking system.
    ''')

    st.markdown('---')

    # Mengatur ukuran gambar
    fig, axes = plt.subplots(figsize=(20, 25))

    # Subplot 1
    axes = plt.subplot(4, 2, 1)
    plt.title('Variable no_of_adults')
    sns.countplot(x='no_of_adults', data=data)

    # Subplot 2
    axes = plt.subplot(4, 2, 2)
    plt.title('Variable no_of_children')
    sns.countplot(x='no_of_children', data=data)

    # Subplot 3
    axes = plt.subplot(4, 2, 3)
    plt.title('Variable no_of_weekend_nights')
    sns.countplot(x='no_of_weekend_nights', data=data)

    # Subplot 4
    axes = plt.subplot(4, 2, 4)
    plt.title('Variable no_of_week_nights')
    sns.countplot(x='no_of_week_nights', data=data)

    # Subplot 5
    axes = plt.subplot(4, 2, 5)
    plt.title('Variable type_of_meal_plan')
    sns.countplot(x='type_of_meal_plan', data=data)

    # Subplot 6
    axes = plt.subplot(4, 2, 6)
    plt.title('Variable required_car_parking_space')
    sns.countplot(x='required_car_parking_space', data=data)

    # Subplot 7
    axes = plt.subplot(4, 2, 7)
    plt.title('Variable room_type_reserved')
    sns.countplot(x='room_type_reserved', data=data)

    # Subplot 8
    axes = plt.subplot(4, 2, 8)
    plt.title('Variable arrival_year')
    sns.countplot(x='arrival_year', data=data)

    # Menampilkan visualisasi menggunakan Streamlit
    st.pyplot(fig)

    st.write(
    '''
    The visualization above represents categorical data from the dataset. Based on the visualization, it can be observed 
    that Room Type 1 is the most popular choice among guests when making hotel reservations. The majority of customers who 
    book the hotel consist of adults only and have relatively short durations of stay. Regarding the meal plan, meal_plan_1 
    is the dominant choice among guests. Knowing the high demand for this particular meal plan, special attention should be 
    given to ensuring an adequate stock of the corresponding food items to meet the expected number of orders.
    ''')

    st.markdown('---')

    df=data

    # Mengatur ukuran gambar
    fig, axes = plt.subplots(figsize=(20, 25))

    # Subplot 1
    axes = plt.subplot(3, 2, 1)
    plt.title('Variable arrival_month')
    sns.countplot(x='arrival_month', data=df)

    # Subplot 2
    axes = plt.subplot(3, 2, 2)
    plt.title('Variable market_segment_type')
    sns.countplot(x='market_segment_type', data=df)

    # Subplot 3
    axes = plt.subplot(3, 2, 3)
    plt.title('Variable repeated_guest')
    sns.countplot(x='repeated_guest', data=df)

    # Subplot 4
    axes = plt.subplot(3, 2, 4)
    plt.title('Variable no_of_previous_cancellations')
    sns.countplot(x='no_of_previous_cancellations', data=df)

    # Subplot 5
    axes = plt.subplot(3, 2, 5)
    plt.title('Variable no_of_special_requests')
    sns.countplot(x='no_of_special_requests', data=df)

    # Menampilkan visualisasi menggunakan Streamlit
    st.pyplot(fig)

    st.write(
    '''
    Based on the visualization above, it can be observed that there is a significant number of guests during the months of 
    September and October, followed by a decrease in guest bookings towards the end of the year, specifically in November and 
    December. The majority of hotel reservations are made online. Knowing this information, the management can provide additional
    benefits to guests who make online bookings and also pay closer attention to the online booking system to prevent any 
    potential issues.
    ''')

    st.markdown('---')

if __name__== '__main__':
    run()