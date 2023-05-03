# pip3 install streamlit
# pip3 install pandas
# pip3 install scikit-learn


# IMPORT STATEMENTS
import streamlit as st
import pandas as pd
import pickle
from PIL import Image


def maternal_health():
    st.title('Maternal Health')
    st.write("Maternal health issues for women arise during pregnancy, childbirth, and the postnatal period. At the time of pregnancy, women are at a higher risk of health complications which may lead to miscarriage and death in many cases. Before pregnancy, the overall lifestyle choices and health of women can affect maternal health risks.Maternal health issues are health concerns that affect women during pregnancy, childbirth, and the postpartum period. Maternal health issues can range from minor discomforts to life-threatening complications, and they can vary widely depending on the woman's overall health, age, and other factors")
    st.header('Working Model')
    st.image(Image.open('images/m3.png'))
    st.sidebar.header('Working Model')
    st.subheader('Maternal Health Dataset')
    df = pd.read_csv("dataset.csv")
    st.dataframe(df)

    def user_report():
        age = st.sidebar.slider('Age', 10, 70, 25)
        systolicBP = st.sidebar.slider('SystolicBP', 70, 160, 120)
        diastolicBP = st.sidebar.slider('DiastolicBP', 49, 100, 70)
        bS = st.sidebar.slider('BS', 6.0, 19.0, 10.1)
        bodyTemp = st.sidebar.slider('BodyTemp', 98, 103, 100)
        fetalHealth = st.sidebar.select_slider('FetalHealth',options=[1,2,3])
        
        st.table({
            'Age': age,
            'SystolicBP': systolicBP,
            'DiastolicBP': diastolicBP,
            'BS': bS,
            'BodyTemp': bodyTemp,
            'FetalHealth' : fetalHealth
        })
        return [[age, systolicBP, diastolicBP, bS, bodyTemp,fetalHealth ]]

    st.image(Image.open('images/m1.png'))
    # st.subheader('Algorithm')
    # st.code("rfc = RandomForestClassifier(random_state = 42) ")
    # st.code(''' 
    #              KNN Test Score	0.704433 
    #              SVM Test Score	0.586207 
    #              Random Forest Test Score 0.822660 
    #              Gaussian NB Test Score	0.551724 ''')
    st.subheader('Input Data')

    # OUTPUT
    rfc_model = pickle.load(open('rfc_maternal1.pkl', 'rb'))
    result = rfc_model.predict(user_report())
    st.subheader('Your Report: ')
    output = ''
    if result == 1:
        st.success("Low risk")
        st.info(
            "As the fetal health is NORMAL and as per the input data, the risk of complications is low.")
    elif result == 3:
        st.error('high risk')
        st.info(
            "As the fetal health is PATHOLOGICAL and as per the input data, the risk of complications is high.")
    else:
        st.warning('Medium risk')
        st.info(
            "As the fetal health is SUSPECTFUL and as per the input data, the risk of complications is medium.")
    st.title(output)


def fetal_health():
    st.title('CTG Interpretation')
    st.write("The cardiotocograph (CTG) is a continuous electronic record of the fetal heart rate obtained via an ultrasound transducer placed on the mother’s abdomen (external or indirect CTG). A second transducer is placed on the mother’s abdomen over the uterine fundus to record simultaneously the presence of any uterine activity. Both fetal heart rate and uterine activity are traced simultaneously onto a paper strip. Components of the fetal heart rate that can be assessed include: baseline rate, baseline variability, accelerations and decelerations. The relationship between fetal heart rate and the timing of uterine contractions is also assessed. Cardiotocography is used widely in maternity care, both in the antepartum and intrapartum periods")
    st.header('Fetal Growth from 4 To 40 Weeks')
    st.image(Image.open('images/f1.jpg'), caption='Fetal Health Prediction')
    st.sidebar.header('Fetal Data')
    st.subheader('Fetal Health Data')
    df = pd.read_csv("fetal_health.csv")
    st.dataframe(df)

    def user_report():
        baseline = st.sidebar.slider('Baseline value', 106, 160, 110)
        accelerations = st.sidebar.number_input("Accelerations", min_value=0.000, max_value=0.019, step=1e-6,
                                                                   format="%.3f")
        fetal_movement = st.sidebar.number_input("Fetal Movement", min_value=0.000, max_value=0.0481, step=1e-6,
                                                 format="%.3f")
        uterine_contractions = st.sidebar.number_input("Uterine Contractions", min_value=0.000, max_value=0.015,
                                                       step=1e-6, format="%.3f")
        light_decelerations = st.sidebar.number_input("Light Decelerations", min_value=0.000, max_value=0.015,
                                                      step=1e-6, format="%.3f")
        severe_decelerations = st.sidebar.number_input("severe_decelerations", min_value=0.000, max_value=0.001,
                                                       step=1e-6, format="%.3f")
        prolongued_decelerations = st.sidebar.number_input("Prolongued Decelerations", min_value=0.000, max_value=0.005,
                                                           step=1e-6, format="%.3f")
        abnormal_short_term_variability = st.sidebar.slider('Abnormal Short Term Variability', 12, 87, 60)
        mean_value_of_short_term_variability = st.sidebar.number_input("Mean Value Of Short Term Variability",
                                                                       min_value=0.2, max_value=7.000, step=1e-6,
                                                                       format="%.3f")
        percentage_of_time_with_abnormal_long_term_variability = st.sidebar.slider(
            'Percentage Of Time With Abnormal Long Term Variability', 0, 91, 40)
        mean_value_of_long_term_variability = st.sidebar.number_input("mean_value_of_long_term_variability",
                                                                      min_value=0.000, max_value=50.700, step=1e-6,
                                                                      format="%.3f")
        histogram_width = st.sidebar.number_input("histogram_width", min_value=3.000, max_value=180.000, step=1e-6,
                                                  format="%.3f")
        histogram_min = st.sidebar.number_input("histogram_min", min_value=50.000, max_value=159.000, step=1e-6,
                                                format="%.3f")
        histogram_max = st.sidebar.number_input("histogram_max", min_value=122.0, max_value=238.000, step=1e-6,
                                                format="%.3f")
        histogram_number_of_peaks = st.sidebar.number_input("histogram_number_of_peaks", min_value=0.0,
                                                            max_value=18.000, step=1e-6, format="%.3f")
        histogram_number_of_zeroes = st.sidebar.number_input("histogram_number_of_zeroes", min_value=0.0,
                                                             max_value=10.000, step=1e-6, format="%.3f")
        histogram_mode = st.sidebar.number_input("histogram_mode", min_value=60.0, max_value=187.000, step=1e-6,
                                                 format="%.3f")
        histogram_mean = st.sidebar.number_input("histogram_mean", min_value=73.0, max_value=182.000, step=1e-6,
                                                 format="%.3f")
        histogram_median = st.sidebar.number_input("histogram_median", min_value=77.0, max_value=186.000, step=1e-6,
                                                   format="%.3f")
        histogram_variance = st.sidebar.number_input("histogram_variance", min_value=0.0, max_value=269.000, step=1e-6,
                                                     format="%.3f")
        histogram_tendency = st.sidebar.number_input("histogram_tendency", min_value=-1.0, max_value=1.000, step=1e-6,
                                                     format="%.3f")
        st.table({
            'Baseline value': baseline,
            'Accelerations': accelerations,
            'Fetal Movement': fetal_movement,
            'Uterine Contractions': uterine_contractions,
            'Light Decelerations': light_decelerations,
            'severe_decelerations': severe_decelerations,
            'Prolongued Decelerations': prolongued_decelerations,
            'Abnormal Short Term Variability': abnormal_short_term_variability,
            'Mean Value Of Short Term Variability': mean_value_of_short_term_variability,
            'Percentage Of Time With Abnormal Long Term Variability': percentage_of_time_with_abnormal_long_term_variability,
            'mean_value_of_long_term_variability': mean_value_of_long_term_variability,
            'histogram_width': histogram_width,
            'histogram_min': histogram_min,
            'histogram_max': histogram_max,
            'histogram_number_of_peaks': histogram_number_of_peaks,
            'histogram_number_of_zeroes': histogram_number_of_zeroes,
            'histogram_mode': histogram_mode,
            'histogram_mean': histogram_mean,
            'histogram_median': histogram_median,
            'histogram_variance': histogram_variance,
            'histogram_tendency': histogram_tendency

        })
        return [
            [baseline, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations,
             prolongued_decelerations, abnormal_short_term_variability, mean_value_of_short_term_variability,
             percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,
             histogram_width, histogram_min, histogram_max, histogram_number_of_peaks, histogram_number_of_zeroes,
             histogram_mode, histogram_mean, histogram_median, histogram_variance, histogram_tendency]]

    st.image(Image.open('images/fetal.png'), caption='Sunrise by the mountains')
    # st.subheader('Algoithm')
    # st.code(''' lgbm = create_model('lightgbm')
    #                ''')
    st.subheader('CTG Response: ')
    # user_report_data = user_report()

    model = pickle.load(open('RF_fetal.pkl', 'rb'))
    result = model.predict(user_report())

    # OUTPUT
    st.subheader('Your Report: ')
    if result == 1:
        st.success("NO FURTHER ACTION AND NORMAL FEATURES")
        st.info("As per the CTG result, all features are normal and require no further action.")
    elif result == 3:
        st.error('IMMEDIATE MANAGEMENT OR URGENT DELIVERY')
        st.info(
            "As per the CTG result, features are likely to be associated with fetal compromise and requires immediate attention. ")
    else:
        st.warning('REQUIRES ATTENTION & MAY REQUIRE FURTHER ACTION')
        st.info(
            "As per the CTG result, features may be associated with fetal compromise and require attention.")


my_page = st.sidebar.radio('Page Navigation', ['Fetal Health Prediction', 'Maternal Health Prediction'])

if my_page == 'Fetal Health Prediction':
    fetal_health()
else:
    maternal_health()







