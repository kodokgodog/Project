import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'Customer Churn - EDA',
    initial_sidebar_state = 'expanded'
)

def run() :
    
    # Membuat Title
    st.title('Customer Churn Prediction')

    # Membuat Sub Header
    st.subheader('EDA for Analysis of Customer Churn Dataset')

    # Menambahkan Gambar
    image = Image.open('churn.png')
    st.image(image, caption='Customer Churn')

    # Menambahkan Deskripsi
    st.write('Page Made by **Satriya Fauzan Adhim**')

    st.markdown('---')

    st.write('## Background')
    st.write('''Customer Churn on company across businesses always give negative impact 
                to the company especially the profit loss. . Customer churn is a common 
                challenge for many businesses across various industries, where customers 
                stop using the company's products or services and switch to competitors..''')
    st.write('## Problem Statement')
    st.write('''The problem statement is to develop a predictive model using deep 
                learning Artificial Neural Networks (ANN) to identify customers who 
                are most likely to churn. The goal is to leverage available customer 
                data, such as demographics, purchase history, customer interactions, 
                and feedback, to build an accurate model that can predict churn behavior..''')
    
    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
    The objective is to develop a robust and accurate churn prediction model 
    that can be used to identify customers at risk of churn. This will enable 
    the company to take proactive measures, such as targeted marketing campaigns, 
    personalized offers, or improved customer service, to retain customers and 
    reduce churn..

    By utilizing deep learning techniques, we aim to uncover intricate patterns 
    and relationships in the data that traditional models may struggle to capture. 
    The ANN model will be trained on historical customer data, where the churn 
    status is known, to learn the underlying patterns and create a predictive model.

    '''

    # Show DataFrame
    data_url = 'https://raw.githubusercontent.com/kodokgodog/Latihan_hactiv8/main/churn.csv'
    data = pd.read_csv(data_url)
    st.dataframe(data)

    # Membuat Barplot
    st.write('#### Plot churn_risk_score')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='churn_risk_score', data=data)
    st.pyplot(fig)

    st.write(
    '''
    From the visualization above, we can see that the amount of customer that gonna churn 
    is higher compared to not churn. Those numbers will have a significant negative impact 
    on the company's business, with churn rate exceeding more than half of the total 
    customers. Based on the data percentage, we can also observe that the data distribution 
    appears to be balanced.
    ''')

    st.markdown('---')

    # Mengatur ukuran gambar
    fig, axes = plt.subplots(figsize=(20, 25))

    # Subplot 1
    axes = plt.subplot(4, 2, 1)
    plt.title('Variable gender')
    sns.countplot(x='gender', data=data)

    # Subplot 2
    axes = plt.subplot(4, 2, 2)
    plt.title('Variable region_category')
    sns.countplot(x='region_category', data=data)

    # Subplot 3
    axes = plt.subplot(4, 2, 3)
    plt.title('Variable membership_category')
    sns.countplot(x='membership_category', data=data)

    # Subplot 4
    axes = plt.subplot(4, 2, 4)
    plt.title('Variable joined_through_referral')
    sns.countplot(x='joined_through_referral', data=data)

    # Subplot 5
    axes = plt.subplot(4, 2, 5)
    plt.title('Variable preferred_offer_types')
    sns.countplot(x='preferred_offer_types', data=data)

    # Subplot 6
    axes = plt.subplot(4, 2, 6)
    plt.title('Variable internet_option')
    sns.countplot(x='internet_option', data=data)

    # Subplot 7
    axes = plt.subplot(4, 2, 7)
    plt.title('Variable used_special_discount')
    sns.countplot(x='used_special_discount', data=data)

    # Subplot 8
    axes = plt.subplot(4, 2, 8)
    plt.title('Variable offer_application_preference')
    sns.countplot(x='offer_application_preference', data=data)

    # Subplot 9
    axes = plt.subplot(4, 2, 8)
    plt.title('Variable past_complaint')
    sns.countplot(x='past_complaint', data=data)

    # Subplot 10
    axes = plt.subplot(4, 2, 8)
    plt.title('Variable complaint_status')
    sns.countplot(x='complaint_status', data=data)

    # Menampilkan visualisasi menggunakan Streamlit
    st.pyplot(fig)

    st.markdown('---')

    df=data

    # Mengatur ukuran gambar
    fig, axes = plt.subplots(figsize=(20, 25))

    # Subplot 1
    axes = plt.subplot(3, 2, 1)
    plt.title('Variable age')
    sns.countplot(x='age', data=df)

    # Subplot 2
    axes = plt.subplot(3, 2, 2)
    plt.title('Variable days_since_last_login')
    sns.countplot(x='days_since_last_login', data=df)

    # Subplot 3
    axes = plt.subplot(3, 2, 3)
    plt.title('Variable avg_time_spent')
    sns.countplot(x='avg_time_spent', data=df)

    # Subplot 4
    axes = plt.subplot(3, 2, 4)
    plt.title('Variable avg_transaction_value')
    sns.countplot(x='avg_transaction_value', data=df)

    # Subplot 5
    axes = plt.subplot(3, 2, 5)
    plt.title('Variable avg_frequency_login_days')
    sns.countplot(x='avg_frequency_login_days', data=df)
    
    # Subplot 6
    axes = plt.subplot(3, 2, 5)
    plt.title('Variable points_in_wallet')
    sns.countplot(x='points_in_wallet', data=df)

    # Menampilkan visualisasi menggunakan Streamlit
    st.pyplot(fig)

    st.write(
    '''
    Based on the visualization above, we can see that the majority of churned customers are 
    either non-members or have low membership levels. Based on this data, a business strategy
    can be developed. For example, offering attractive promotions or offers specifically 
    targeted at customers with low membership levels could be implemented. Additionally, 
    providing promotions like offers for new members can also be effective.

    By targeting these specific segments, the business can aim to retain existing customers 
    with low membership levels and attract new customers through enticing offers. It is 
    important to create personalized and compelling incentives to encourage customer loyalty 
    and minimize churn.

    it can be observed that the average transaction value for customers who are likely to 
    churn is quite high. Therefore, if this issue is not addressed, the company will face a 
    significant negative impact, particularly in terms of high profit loss.

    To mitigate this situation, the company could consider implementing retention 
    strategies specifically targeting high-value customers. These strategies could include 
    personalized offers, loyalty programs, or enhanced customer service tailored to their 
    needs. By providing incentives and a positive customer experience, the company can 
    encourage these customers to remain loyal and continue making high-value transactions.
    ''')

    st.markdown('---')

if __name__== '__main__':
    run()