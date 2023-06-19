import pandas as pd
import streamlit as st
import pickle
import json
import joblib

#model dan preprocessing
with open('best_xgb.pkl', 'rb') as file_1:
  best_xgb= joblib.load(file_1)
  
with open('Drop_Columns.txt', 'r') as file_2:
 Drop_Columns = json.load(file_2)

with open('list_num_cols.txt', 'r') as file_3:
  num_columns = json.load(file_3)

with open('list_cat_columns.txt', 'r') as file_4:
  cat_columns = json.load(file_4)

with open('final_pipeline.pkl', 'rb') as file_5:
  final_pipeline = pickle.load(file_5)

def run():
    # membuat title
    st.title('Credit Default Prediction')
    st.subheader('Predicting Credit Default')
    st.markdown('---')
    st.write("# Debtor Information")
    # Buat form
    with st.form(key='form_credit'):
        st.write("#### Client's Personal Information")
        SK_ID_CURR = st.number_input('Client ID', min_value=0, max_value=9999999, value=0)
        NAME_CONTRACT_TYPE = st.selectbox('Contract Type', ('Cash loans', 'Revolving loans'))
        CODE_GENDER = st.radio('Clients gender', ('F', 'M'))
        FLAG_OWN_CAR = st.radio('Flag if the client owns a car', ('N', 'Y'))
        FLAG_OWN_REALTY= st.radio('Flag if client owns a house or flat', ('N', 'Y'))
        CNT_CHILDREN= st.number_input("Client's Children Count", min_value=0, max_value=20, value=0)

        st.markdown('---')
        st.write("#### Client's Financial Information")

        AMT_INCOME_TOTAL= st.number_input('Client Income', min_value=0, max_value=9999999, value=30000)
        AMT_CREDIT=st.number_input('Client Credit Amount', min_value=0, max_value=9999999, value=30000)
        AMT_ANNUITY=st.number_input('Client Annuity', min_value=0, max_value=9999999, value=3000)
        AMT_GOODS_PRICE=st.number_input('price of the goods for which the loan is given', min_value=0, max_value=9999999, value=50000)
        NAME_TYPE_SUITE=st.selectbox('Who was accompanying client when they were applying for the loan', ('Unaccompanied', 'Family', 'Spouse, partner', 'Group of people', 'Other_B', 'Children', 'Other_A'))
        NAME_INCOME_TYPE=st.selectbox('Clients income type', ('Working', 'State servant', 'Pensioner', 'Commercial associate', 'Businessman', 'Student', 'Unemployed'))
        NAME_EDUCATION_TYPE=st.selectbox('Level of highest education the client achieved', ('Higher education', 'Secondary / secondary special', 'Incomplete higher', 'Lower secondary', 'Academic degree'))
        NAME_FAMILY_STATUS=st.selectbox('Family status of the client', ('Married', 'Single / not married', 'Civil marriage', 'Widow', 'Separated'))
        NAME_HOUSING_TYPE=st.selectbox('What is the housing situation of the client', ('House / apartment', 'With parents', 'Rented apartment', 'Municipal apartment', 'Office apartment', 'Co-op apartment'))
        REGION_POPULATION_RELATIVE=st.slider('Normalized population of region where client lives', min_value=0.000000, max_value=0.080000, value=0.0200, step=0.000001)

        st.markdown('---')

        DAYS_BIRTH_= st.number_input('How many days before the client was born', min_value=7000, max_value=30000, value=15000)
        DAYS_BIRTH = -1 * DAYS_BIRTH_
        DAYS_EMPLOYED_= st.number_input('How many days before the application the person started current employment', min_value=0, max_value=30000, value=5000)
        DAYS_EMPLOYED = -1* DAYS_EMPLOYED_
        DAYS_REGISTRATION_= st.number_input('How many days before the application did client change his registration', min_value=0, max_value=30000, value=5000)
        DAYS_REGISTRATION = -1* DAYS_REGISTRATION_
        DAYS_ID_PUBLISH_ = st.number_input('How many days before the application did client change the identity document with which he applied for the loan', min_value=0, max_value=30000, value=5000)
        DAYS_ID_PUBLISH = -1* DAYS_ID_PUBLISH_

        st.markdown('---')
        OWN_CAR_AGE=st.number_input('Age of client\'s car', min_value=0, max_value=100, value=0)

        st.markdown('---')
        FLAG_MOBIL_=st.radio('Did client provide mobile phone', ('Yes', 'No'), index=0)
        if FLAG_MOBIL_ == 'No':
            FLAG_MOBIL = 0
        else:
            FLAG_MOBIL = 1
        FLAG_EMP_PHONE_=st.radio('Did client provide emp phone', ('Yes', 'No'), index=0)
        if FLAG_EMP_PHONE_ == 'No':
            FLAG_EMP_PHONE = 0
        else:
            FLAG_EMP_PHONE = 1
        FLAG_WORK_PHONE_=st.radio('Did client provide work phone', ('Yes', 'No'), index=0)
        if FLAG_WORK_PHONE_ == 'No':
            FLAG_WORK_PHONE = 0
        else:
            FLAG_WORK_PHONE = 1
        FLAG_CONT_MOBILE_=st.radio('Was mobile phone reachable', ('Yes', 'No'), index=0)
        if FLAG_CONT_MOBILE_ == 'No':
            FLAG_CONT_MOBILE = 0
        else:
            FLAG_CONT_MOBILE = 1
        FLAG_PHONE_=st.radio('Did client provide home phone', ('Yes', 'No'), index=0)
        if FLAG_PHONE_ == 'No':
            FLAG_PHONE = 0
        else:
            FLAG_PHONE = 1
        FLAG_EMAIL_=st.radio('Did client provide email', ('Yes', 'No'), index=0)
        if FLAG_EMAIL_ == 'No':
            FLAG_EMAIL = 0
        else:
            FLAG_EMAIL = 1
        st.markdown('---')
        OCCUPATION_TYPE= st.selectbox('What kind of occupation does the client have', ('Low-skill Laborers', 'Drivers', 'Sales staff', 
                                                                                                           'High skill tech staff', 'Core staff', 'Laborers', 
                                                                                                           'Managers', 'Accountants', 'Medicine staff', 
                                                                                                           'Security staff', 'Private service staff', 'Secretaries', 
                                                                                                           'Cleaning staff', 'Cooking staff', 'HR staff', 
                                                                                                           'Waiters/barmen staff', 'Realty agents', 'IT staff'))
        CNT_FAM_MEMBERS= st.number_input("How many family members does client have", min_value=0, max_value=20, value=0)
        REGION_RATING_CLIENT= st.radio('Our rating of the region where client lives', (1, 2, 3), index=0)
        REGION_RATING_CLIENT_W_CITY= st.radio('Our rating of the region where client lives with taking city into account', (1, 2, 3), index=0)
        st.markdown('---')
        WEEKDAY_APPR_PROCESS_START= st.radio('Day of the week when the client apply for the loan', ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'))
        HOUR_APPR_PROCESS_START= st.number_input('Hour when client apply for the loan', min_value=0, max_value=24, value=0, step=1, help="Input rounded value.")

        st.markdown('---')
        st.write("#### Client's Address in Region")

        REG_REGION_NOT_LIVE_REGION_=st.radio('Permanent address does not match contact address', ('No', 'Yes'))
        if REG_REGION_NOT_LIVE_REGION_ == 'No':
            REG_REGION_NOT_LIVE_REGION = 0
        else:
            REG_REGION_NOT_LIVE_REGION = 1
        REG_REGION_NOT_WORK_REGION_=st.radio('Permanent address does not match work address', ('No', 'Yes'))
        if REG_REGION_NOT_WORK_REGION_ == 'No':
            REG_REGION_NOT_WORK_REGION = 0
        else:
            REG_REGION_NOT_WORK_REGION = 1
        LIVE_REGION_NOT_WORK_REGION= st.radio('Contact address does not match work address', ('No', 'Yes'))
        if LIVE_REGION_NOT_WORK_REGION == 'No':
            LIVE_REGION_NOT_WORK_REGION = 0
        else:
            LIVE_REGION_NOT_WORK_REGION = 1
        st.markdown('---')
        st.write("#### Client's Address in City")

        REG_CITY_NOT_LIVE_CITY= st.radio('Contact address (city) does not match contact address', ('No', 'Yes'))
        if REG_CITY_NOT_LIVE_CITY == 'No':
            REG_CITY_NOT_LIVE_CITY = 0
        else:
            REG_CITY_NOT_LIVE_CITY = 1
        REG_CITY_NOT_WORK_CITY= st.radio('Permanent address (city) does not match work address', ('No', 'Yes'))
        if REG_CITY_NOT_WORK_CITY == 'No':
            REG_CITY_NOT_WORK_CITY = 0
        else:
            REG_CITY_NOT_WORK_CITY = 1
        LIVE_CITY_NOT_WORK_CITY= st.radio('Contact address (city) does not match work address', ('No', 'Yes'))
        if LIVE_CITY_NOT_WORK_CITY == 'No':
            LIVE_CITY_NOT_WORK_CITY = 0
        else:
            LIVE_CITY_NOT_WORK_CITY = 1
        ORGANIZATION_TYPE= st.selectbox('Type of organization where client works', ('Kindergarten', 'Self-employed', 'Transport: type 3',
                                                                                    'Business Entity Type 3', 'Government', 'Industry: type 9',
                                                                                    'School', 'Trade: type 2', 'XNA', 'Services', 'Bank',
                                                                                    'Industry: type 3', 'Other', 'Trade: type 6', 'Industry: type 12',
                                                                                    'Trade: type 7', 'Postal', 'Medicine', 'Housing',
                                                                                    'Business Entity Type 2', 'Construction', 'Military',
                                                                                    'Industry: type 4', 'Trade: type 3', 'Legal Services', 'Security',
                                                                                    'Industry: type 11', 'University', 'Business Entity Type 1',
                                                                                    'Agriculture', 'Security Ministries', 'Transport: type 2',
                                                                                    'Industry: type 7', 'Transport: type 4', 'Telecom', 'Emergency',
                                                                                    'Police', 'Industry: type 1', 'Transport: type 1', 'Electricity',
                                                                                    'Industry: type 5', 'Hotel', 'Restaurant', 'Advertising', 'Mobile',
                                                                                    'Trade: type 1', 'Industry: type 8', 'Realtor', 'Cleaning',
                                                                                    'Industry: type 2', 'Trade: type 4', 'Industry: type 6', 'Culture',
                                                                                    'Insurance', 'Religion', 'Industry: type 13', 'Industry: type 10',
                                                                                    'Trade: type 5'))
        
        st.markdown('---')
        st.write("#### Credit Score")
        EXT_SOURCE_1= st.slider('Credit Score from Source 1', min_value=0.0, max_value=20.0, value=0.1, step=1.0, help="Input rounded value.")
        EXT_SOURCE_2= st.slider('Credit Score from Source 2', min_value=0.0, max_value=20.0, value=0.1, step=1.0, help="Input rounded value.")
        EXT_SOURCE_3= st.slider('Credit Score from Source 3', min_value=0.0, max_value=20.0, value=0.1, step=1.0, help="Input rounded value.")
        st.markdown('---')

        st.write("#### Client's social surroundings")
        OBS_30_CNT_SOCIAL_CIRCLE= st.number_input('Observation 30 days past due',min_value=0, max_value=50, value=0, step=1, help="Input rounded value.")
        DEF_30_CNT_SOCIAL_CIRCLE= st.number_input('Number of default 30 days past due', min_value=0, max_value=50, value=0, step=1, help="Input rounded value.")
        OBS_60_CNT_SOCIAL_CIRCLE= st.number_input('Observation 60 days past due', min_value=0, max_value=50, value=0, step=1, help="Input rounded value.")
        DEF_60_CNT_SOCIAL_CIRCLE= st.number_input('Number of default 60 days past due', min_value=0, max_value=50, value=0, step=1, help="Input rounded value.")

        DAYS_LAST_PHONE_CHANGE_ = st.number_input('How many days before application did client change phone', min_value=0, max_value=10000, value=1000)
        DAYS_LAST_PHONE_CHANGE = -1 * DAYS_LAST_PHONE_CHANGE_

        st.markdown('---')

        st.write("#### Client's Document")
        flag_document_2= st.radio('Did client provide Identification?', ('No', 'Yes'))
        if flag_document_2 == 'No':
            FLAG_DOCUMENT_2 = 0
        else:
            FLAG_DOCUMENT_2 = 1
        FLAG_DOCUMENT_3_= st.radio('Did client provide proof of address?', ('No', 'Yes'))
        if FLAG_DOCUMENT_3_ == 'No':
            FLAG_DOCUMENT_3 = 0
        else:
            FLAG_DOCUMENT_3 = 1
        FLAG_DOCUMENT_4_= st.radio('Did client provide bank statement?', ('No', 'Yes'))
        if FLAG_DOCUMENT_4_ == 'No':
            FLAG_DOCUMENT_4 = 0
        else:
            FLAG_DOCUMENT_4 = 1
        FLAG_DOCUMENT_5_= st.radio('Did client provide employment certificate?', ('No', 'Yes'))
        if FLAG_DOCUMENT_5_ == 'No':
            FLAG_DOCUMENT_5 = 0
        else:
            FLAG_DOCUMENT_5 = 1
        FLAG_DOCUMENT_6_= st.radio('Did client provide other document (code = 6)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_6_ == 'No':
            FLAG_DOCUMENT_6 = 0
        else:
            FLAG_DOCUMENT_6 = 1
        FLAG_DOCUMENT_7_= st.radio('Did client provide library card?', ('No', 'Yes'))
        if FLAG_DOCUMENT_7_ == 'No':
            FLAG_DOCUMENT_7 = 0
        else:
            FLAG_DOCUMENT_7 = 1       
        FLAG_DOCUMENT_8_= st.radio('Did client provide car registration?', ('No', 'Yes'))
        if FLAG_DOCUMENT_8_ == 'No':
            FLAG_DOCUMENT_8 = 0
        else:
            FLAG_DOCUMENT_8 = 1
        FLAG_DOCUMENT_9_= st.radio('Did client provide passport?', ('No', 'Yes'))
        if FLAG_DOCUMENT_9_ == 'No':
            FLAG_DOCUMENT_9 = 0
        else:
            FLAG_DOCUMENT_9 = 1

        FLAG_DOCUMENT_10_= st.radio("Did client provide driver's license?", ('No', 'Yes'))
        if FLAG_DOCUMENT_10_ == 'No':
            FLAG_DOCUMENT_10 = 0
        else:
            FLAG_DOCUMENT_10 = 1

        FLAG_DOCUMENT_11_= st.radio('Did client provide other document (code = 11)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_11_ == 'No':
            FLAG_DOCUMENT_11 = 0
        else:
            FLAG_DOCUMENT_11 = 1

        FLAG_DOCUMENT_12_= st.radio('Did client provide other document (code = 12)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_12_ == 'No':
            FLAG_DOCUMENT_12 = 0
        else:
            FLAG_DOCUMENT_12 = 1

        FLAG_DOCUMENT_13_= st.radio('Did client provide other document (code = 13)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_13_ == 'No':
            FLAG_DOCUMENT_13 = 0
        else:
            FLAG_DOCUMENT_13 = 1

        FLAG_DOCUMENT_14_= st.radio('Did client provide other document (code = 14)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_14_ == 'No':
            FLAG_DOCUMENT_14 = 0
        else:
            FLAG_DOCUMENT_14 = 1

        FLAG_DOCUMENT_15_= st.radio('Did client provide other document (code = 15)', ('No', 'Yes'))
        if FLAG_DOCUMENT_15_ == 'No':
            FLAG_DOCUMENT_15 = 0
        else:
            FLAG_DOCUMENT_15 = 1

        FLAG_DOCUMENT_16_= st.radio('Did client provide other document (code = 16)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_16_ == 'No':
            FLAG_DOCUMENT_16 = 0
        else:
            FLAG_DOCUMENT_16 = 1

        FLAG_DOCUMENT_17_= st.radio('Did client provide other document (code = 17)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_17_ == 'No':
            FLAG_DOCUMENT_17 = 0
        else:
            FLAG_DOCUMENT_17 = 1

        FLAG_DOCUMENT_18_= st.radio('Did client provide other document (code = 18)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_18_ == 'No':
            FLAG_DOCUMENT_18 = 0
        else:
            FLAG_DOCUMENT_18 = 1

        FLAG_DOCUMENT_19_= st.radio('Did client provide other document (code = 19)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_19_ == 'No':
            FLAG_DOCUMENT_19 = 0
        else:
            FLAG_DOCUMENT_19 = 1

        FLAG_DOCUMENT_20_= st.radio('Did client provide other document (code = 20)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_20_ == 'No':
            FLAG_DOCUMENT_20 = 0
        else:
            FLAG_DOCUMENT_20 = 1

        FLAG_DOCUMENT_21_= st.radio('Did client provide other document (code = 21)?', ('No', 'Yes'))
        if FLAG_DOCUMENT_21_ == 'No':
            FLAG_DOCUMENT_21 = 0
        else:
            FLAG_DOCUMENT_21 = 1

        st.markdown('---')

        st.write("#### Number of Enquiries")

        AMT_REQ_CREDIT_BUREAU_HOUR= st.slider('One hour before application', min_value=0, max_value=24, value=0, step=1, help="Input rounded value.")
        AMT_REQ_CREDIT_BUREAU_DAY= st.slider('One day before application', min_value=0, max_value=31, value=0, step=1, help="Input rounded value.")
        AMT_REQ_CREDIT_BUREAU_WEEK= st.slider('One week before application', min_value=0, max_value=10, value=0, step=1, help="Input rounded value.")
        AMT_REQ_CREDIT_BUREAU_MON= st.slider('One month before application', min_value=0, max_value=24, value=0, step=1, help="Input rounded value.")
        AMT_REQ_CREDIT_BUREAU_QRT= st.slider('Three months before application', min_value=0, max_value=12, value=0, step=1, help="Input rounded value.")
        AMT_REQ_CREDIT_BUREAU_YEAR= st.slider('One year before application', min_value=0, max_value=30, value=0, step=1, help="Input rounded value.")

        st.markdown('---')

        st.write("#### Additional Data")
        DAYS_CREDIT= st.slider('Days Credit', min_value=-3000, max_value=10, value=0, step=1, help="How many days before current application did client apply for Credit Bureau credit.")
        DAYS_CREDIT_UPDATE= st.slider('Days Credit Update', min_value=-45000, max_value=30, value=0, step=1, help="How many days before current application did client apply for Credit Bureau credit.")
        DAYS_DECISION= st.slider('Days Decision', min_value=-2922, max_value=10, value=0, step=1, help="How many days before current application did client apply for Credit Bureau credit.")
        NAME_CONTRACT_STATUS_prev = st.selectbox('Contract Status', ('Approved', 'Refused', 'Canceled', 'Unused offer'))
        NAME_YIELD_GROUP = st.selectbox('Yield Group', ('middle', 'low_action', 'high', 'low_normal', 'XNA'))
        CREDIT_ACTIVE = st.selectbox('Credit Active Status', ('Closed', 'Active', 'Sold', 'Bad debt'))
        submitted = st.form_submit_button('Predict')

        # dataframe
        st.write("# Debtor Summary")
        data_inf = {
                    "SK_ID_CURR":SK_ID_CURR,
                    "NAME_CONTRACT_TYPE":NAME_CONTRACT_TYPE,
                    "CODE_GENDER":CODE_GENDER,
                    "FLAG_OWN_CAR":FLAG_OWN_CAR,
                    "FLAG_OWN_REALTY":FLAG_OWN_REALTY,
                    "CNT_CHILDREN":CNT_CHILDREN,
                    "AMT_INCOME_TOTAL":AMT_INCOME_TOTAL,
                    "AMT_CREDIT":AMT_CREDIT,
                    "AMT_ANNUITY":AMT_ANNUITY,
                    "AMT_GOODS_PRICE":AMT_GOODS_PRICE,
                    "NAME_TYPE_SUITE":NAME_TYPE_SUITE,
                    "NAME_INCOME_TYPE":NAME_INCOME_TYPE,
                    "NAME_EDUCATION_TYPE":NAME_EDUCATION_TYPE,
                    "NAME_FAMILY_STATUS":NAME_FAMILY_STATUS,
                    "NAME_HOUSING_TYPE":NAME_HOUSING_TYPE,
                    "REGION_POPULATION_RELATIVE":REGION_POPULATION_RELATIVE,
                    "DAYS_BIRTH":DAYS_BIRTH,
                    "DAYS_EMPLOYED":DAYS_EMPLOYED,
                    "DAYS_REGISTRATION":DAYS_REGISTRATION,
                    "DAYS_ID_PUBLISH":DAYS_ID_PUBLISH,
                    "OWN_CAR_AGE":OWN_CAR_AGE,
                    "FLAG_MOBIL":FLAG_MOBIL,
                    "FLAG_EMP_PHONE":FLAG_EMP_PHONE,
                    "FLAG_WORK_PHONE":FLAG_WORK_PHONE,
                    "FLAG_CONT_MOBILE":FLAG_CONT_MOBILE,
                    "FLAG_PHONE":FLAG_PHONE,
                    "FLAG_EMAIL":FLAG_EMAIL,
                    "OCCUPATION_TYPE":OCCUPATION_TYPE,
                    "CNT_FAM_MEMBERS":CNT_FAM_MEMBERS,
                    "REGION_RATING_CLIENT":REGION_RATING_CLIENT,
                    "REGION_RATING_CLIENT_W_CITY":REGION_RATING_CLIENT_W_CITY,
                    "WEEKDAY_APPR_PROCESS_START":WEEKDAY_APPR_PROCESS_START,
                    "HOUR_APPR_PROCESS_START":HOUR_APPR_PROCESS_START,
                    "REG_REGION_NOT_LIVE_REGION":REG_REGION_NOT_LIVE_REGION,
                    "REG_REGION_NOT_WORK_REGION":REG_REGION_NOT_WORK_REGION,
                    "LIVE_REGION_NOT_WORK_REGION":LIVE_REGION_NOT_WORK_REGION,
                    "REG_CITY_NOT_LIVE_CITY":REG_CITY_NOT_LIVE_CITY,
                    "REG_CITY_NOT_WORK_CITY":REG_CITY_NOT_WORK_CITY,
                    "LIVE_CITY_NOT_WORK_CITY":LIVE_CITY_NOT_WORK_CITY,
                    "ORGANIZATION_TYPE":ORGANIZATION_TYPE,
                    "EXT_SOURCE_1":EXT_SOURCE_1,
                    "EXT_SOURCE_2":EXT_SOURCE_2,
                    "EXT_SOURCE_3":EXT_SOURCE_3,
                    "OBS_30_CNT_SOCIAL_CIRCLE":OBS_30_CNT_SOCIAL_CIRCLE,
                    "DEF_30_CNT_SOCIAL_CIRCLE":DEF_30_CNT_SOCIAL_CIRCLE,
                    "OBS_60_CNT_SOCIAL_CIRCLE":OBS_60_CNT_SOCIAL_CIRCLE,
                    "DEF_60_CNT_SOCIAL_CIRCLE":DEF_60_CNT_SOCIAL_CIRCLE,
                    "DAYS_LAST_PHONE_CHANGE":DAYS_LAST_PHONE_CHANGE,
                    "FLAG_DOCUMENT_2":FLAG_DOCUMENT_2,
                    "FLAG_DOCUMENT_3":FLAG_DOCUMENT_3,
                    "FLAG_DOCUMENT_4":FLAG_DOCUMENT_4,
                    "FLAG_DOCUMENT_5":FLAG_DOCUMENT_5,
                    "FLAG_DOCUMENT_6":FLAG_DOCUMENT_6,
                    "FLAG_DOCUMENT_7":FLAG_DOCUMENT_7,
                    "FLAG_DOCUMENT_8":FLAG_DOCUMENT_8,
                    "FLAG_DOCUMENT_9":FLAG_DOCUMENT_9,
                    "FLAG_DOCUMENT_10":FLAG_DOCUMENT_10,
                    "FLAG_DOCUMENT_11":FLAG_DOCUMENT_11,
                    "FLAG_DOCUMENT_12":FLAG_DOCUMENT_12,
                    "FLAG_DOCUMENT_13":FLAG_DOCUMENT_13,
                    "FLAG_DOCUMENT_14":FLAG_DOCUMENT_14,
                    "FLAG_DOCUMENT_15":FLAG_DOCUMENT_15,
                    "FLAG_DOCUMENT_16":FLAG_DOCUMENT_16,
                    "FLAG_DOCUMENT_17":FLAG_DOCUMENT_17,
                    "FLAG_DOCUMENT_18":FLAG_DOCUMENT_18,
                    "FLAG_DOCUMENT_19":FLAG_DOCUMENT_19,
                    "FLAG_DOCUMENT_20":FLAG_DOCUMENT_20,
                    "FLAG_DOCUMENT_21":FLAG_DOCUMENT_21,
                    "AMT_REQ_CREDIT_BUREAU_HOUR":AMT_REQ_CREDIT_BUREAU_HOUR,
                    "AMT_REQ_CREDIT_BUREAU_DAY":AMT_REQ_CREDIT_BUREAU_DAY,
                    "AMT_REQ_CREDIT_BUREAU_WEEK":AMT_REQ_CREDIT_BUREAU_WEEK,
                    "AMT_REQ_CREDIT_BUREAU_MON":AMT_REQ_CREDIT_BUREAU_MON,
                    "AMT_REQ_CREDIT_BUREAU_QRT":AMT_REQ_CREDIT_BUREAU_QRT,
                    "AMT_REQ_CREDIT_BUREAU_YEAR":AMT_REQ_CREDIT_BUREAU_YEAR,
                    "DAYS_CREDIT":DAYS_CREDIT,
                    "DAYS_CREDIT_UPDATE":DAYS_CREDIT_UPDATE,
                    "DAYS_DECISION":DAYS_DECISION,
                    "NAME_CONTRACT_STATUS_prev":NAME_CONTRACT_STATUS_prev,
                    "NAME_YIELD_GROUP":NAME_YIELD_GROUP,
                    "CREDIT_ACTIVE":CREDIT_ACTIVE

        }

        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf.T, width=800, height=495)

    if submitted:
        data_inf = data_inf.loc[:, ['EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_CREDIT', 'NAME_EDUCATION_TYPE',
                            'DAYS_LAST_PHONE_CHANGE', 'CODE_GENDER', 'DAYS_ID_PUBLISH',
                            'REG_CITY_NOT_WORK_CITY', 'NAME_INCOME_TYPE',
                            'REG_CITY_NOT_LIVE_CITY', 'FLAG_DOCUMENT_3', 'DAYS_EMPLOYED',
                            'NAME_CONTRACT_STATUS_prev', 'DAYS_REGISTRATION',
                            'NAME_YIELD_GROUP', 'AMT_GOODS_PRICE', 'REGION_POPULATION_RELATIVE',
                            'DAYS_CREDIT_UPDATE', 'NAME_HOUSING_TYPE',
                            'DEF_30_CNT_SOCIAL_CIRCLE', 'CREDIT_ACTIVE', 'LIVE_CITY_NOT_WORK_CITY', 'DAYS_DECISION']]
        data_inf = final_pipeline.fit_transform(data_inf)
        y_pred_inf = best_xgb.predict(data_inf)
        if y_pred_inf == 0:
            pred = 'Not Default'
        else:
            pred = 'Default'
        st.markdown('---')
        st.write('# Prediction : ', (pred))
        st.markdown('---')

if __name__ == '__main__':
    run()