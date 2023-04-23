# pip3 install streamlit
# pip3 install pandas
# pip3 install scikit-learn


# IMPORT STATEMENTS
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def maternal_health() :
    st.title('Maternal_health')
    st.write("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    st.header('Working Model')
    st.image(Image.open('images/m3.png'), caption='Sunrise by the mountains')
    st.sidebar.header('Working Model')
    st.subheader('Mothers Data Stats')
    df = pd.read_csv("dataset.csv")
    st.dataframe(df)
    def user_report():
        age = st.sidebar.slider('Age', 10, 70, 25)
        systolicBP = st.sidebar.slider('SystolicBP', 70, 160, 120)
        diastolicBP = st.sidebar.slider('DiastolicBP', 49, 100, 70)
        bS = st.sidebar.slider('BS', 6.0, 19.0, 10.1)
        bodyTemp = st.sidebar.slider('BodyTemp', 98, 103, 100)
        st.table({
            'Age': age,
            'SystolicBP': systolicBP,
            'DiastolicBP': diastolicBP,
            'BS': bS,
            'BodyTemp': bodyTemp
        })
        return [[age, systolicBP, diastolicBP, bS, bodyTemp]]


    st.image(Image.open('images/m1.png'), caption='Sunrise by the mountains')
    st.image(Image.open('images/m2.png'), caption='Sunrise by the mountains')
    st.subheader('Algorithm')
    st.code("rfc = RandomForestClassifier(random_state = 42) ")
    st.code( ''' 
                 KNN Test Score	0.704433 
                 SVM Test Score	0.586207 
                 Random Forest Test Score 0.822660 
                 Gaussian NB Test Score	0.551724 ''')
    st.subheader('You can predict your health')
    st.write("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")
    # OUTPUT
    rfc_model = pickle.load(open('rfc_maternal.pkl', 'rb'))
    result = rfc_model.predict(user_report())
    st.subheader('Your Report: ')
    output = ''
    if result == 1:
        st.success("Low risk")
        st.info("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")
    elif result == 3:
        st.error('high risk')
        st.info("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")
    else:
        st.warning('Medium risk')
        st.info("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")
    st.title(output)
def fetal_health():
    st.title('Fetal Health Prediction')
    st.write("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    st.header('Fetal Growth from 4 To 40 Weeks')
    st.image(Image.open('images/f1.jpg'), caption='Fetal Health Prediction')
    st.sidebar.header('Fetal Data')
    st.subheader('Fetal Data Stats')
    df = pd.read_csv("fetal_health.csv")
    st.dataframe(df)
    def user_report():
        baseline = st.sidebar.slider('Baseline value', 106, 160, 110)
        accelerations = st.sidebar.number_input("Accelerations", min_value=0.000,max_value=0.019, step=1e-6, format="%.3f")
        fetal_movement = st.sidebar.number_input("Fetal Movement", min_value=0.000,max_value=0.0481, step=1e-6, format="%.3f")
        uterine_contractions = st.sidebar.number_input("Uterine Contractions", min_value=0.000,max_value=0.015, step=1e-6, format="%.3f")
        light_decelerations = st.sidebar.number_input("Light Decelerations", min_value=0.000,max_value=0.015, step=1e-6, format="%.3f")
        severe_decelerations = st.sidebar.number_input("severe_decelerations", min_value=0.000,max_value=0.001, step=1e-6, format="%.3f")
        prolongued_decelerations = st.sidebar.number_input("Prolongued Decelerations", min_value=0.000,max_value=0.005, step=1e-6, format="%.3f")
        abnormal_short_term_variability = st.sidebar.slider('Abnormal Short Term Variability', 12, 87, 60)
        mean_value_of_short_term_variability = st.sidebar.number_input("Mean Value Of Short Term Variability", min_value=0.2, max_value=7.000, step=1e-6, format="%.3f")
        percentage_of_time_with_abnormal_long_term_variability = st.sidebar.slider('Percentage Of Time With Abnormal Long Term Variability', 0, 91, 40)
        mean_value_of_long_term_variability = st.sidebar.number_input("mean_value_of_long_term_variability",min_value=0.000, max_value=50.700, step=1e-6,format="%.3f")
        histogram_width = st.sidebar.number_input("histogram_width",  min_value=3.000, max_value=180.000, step=1e-6, format="%.3f")
        histogram_min = st.sidebar.number_input("histogram_min", min_value=50.000, max_value=159.000, step=1e-6,format="%.3f")
        histogram_max = st.sidebar.number_input("histogram_max", min_value=122.0, max_value=238.000, step=1e-6,format="%.3f")
        histogram_number_of_peaks = st.sidebar.number_input("histogram_number_of_peaks", min_value=0.0, max_value=18.000, step=1e-6, format="%.3f")
        histogram_number_of_zeroes = st.sidebar.number_input("histogram_number_of_zeroes", min_value=0.0,  max_value=10.000, step=1e-6, format="%.3f")
        histogram_mode = st.sidebar.number_input("histogram_mode", min_value=60.0,max_value=187.000, step=1e-6, format="%.3f")
        histogram_mean = st.sidebar.number_input("histogram_mean", min_value=73.0, max_value=182.000,step=1e-6, format="%.3f")
        histogram_median = st.sidebar.number_input("histogram_median", min_value=77.0, max_value=186.000,step=1e-6, format="%.3f")
        histogram_variance = st.sidebar.number_input("histogram_variance", min_value=0.0, max_value=269.000, step=1e-6,  format="%.3f")
        histogram_tendency = st.sidebar.number_input("histogram_tendency", min_value=-1.0, max_value=1.000, step=1e-6,  format="%.3f")
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
        return [[baseline, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations, prolongued_decelerations,abnormal_short_term_variability, mean_value_of_short_term_variability,percentage_of_time_with_abnormal_long_term_variability,mean_value_of_long_term_variability,histogram_width,histogram_min,histogram_max,histogram_number_of_peaks,histogram_number_of_zeroes, histogram_mode,histogram_mean, histogram_median,histogram_variance,histogram_tendency]]

    st.image(Image.open('images/fetal.png'), caption='Sunrise by the mountains')
    st.subheader('Algoithm')
    st.code(''' lgbm = create_model('lightgbm')
                   ''')
    st.subheader('All the data you entered: ')
    user_report_data = user_report()
   
    # lgbm_model = pickle.load(open('lgbm_fetal.pkl', 'rb'))
    # result = lgbm_model.predict(user_report())
    result = 1
    # OUTPUT
    st.subheader('Your Report: ')
    if result == 1:
        st.success("Low risk")
        st.info("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")
    elif result == 3:
        st.error('high risk')
        st.info("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")
    else:
        st.warning('Medium risk')
        st.info("s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")

my_page = st.sidebar.radio('Page Navigation', ['Fetal Health Prediction', 'Maternal Health Prediction'])

if my_page == 'Fetal Health Prediction':
    fetal_health()
else:
    maternal_health()





