# pip3 install streamlit
# pip3 install pandas
# pip3 install scikit-learn


# IMPORT STATEMENTS
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset.csv")

# //! HEADINGS  ======================>
st.title('Maternal Health Prediction')
st.sidebar.header('Patient Data')
st.subheader('Training Data Stats')
st.write(df)
st.write(df.describe())


# FUNCTION

def user_report():
    age = st.sidebar.slider('Age', 10, 70, 25)
    systolicBP = st.sidebar.slider('SystolicBP', 70, 160, 120)
    diastolicBP = st.sidebar.slider('DiastolicBP', 49, 100, 70)
    # bS = st.sidebar.slider('BS', 6,19, 10 )
    bS = st.sidebar.slider('BS', 6.0, 19.0, 10.1)
    bodyTemp = st.sidebar.slider('BodyTemp', 98, 103, 100)
   # heartRate = st.sidebar.slider('HeartRate', 7, 90, 120)

    user_report_data = {
        'Age': age,
        'SystolicBP': systolicBP,
        'DiastolicBP': diastolicBP,
        'BS': bS,
        'BodyTemp': bodyTemp
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


# PATIENT DATA

user_data = user_report()
st.subheader('Patient Data')
st.write(user_data)

RiskLevel = {'low risk': 1,
             'mid risk': 2,
             'high risk': 3}

# apply using map
df['RiskLevel'] = df['RiskLevel'].map(RiskLevel).astype(int)

# X AND Y DATA
x = df.drop(['RiskLevel'], axis=1)
y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# MODEL
# rf  =  SVC(kernel = 'linear', random_state = 0)
rf = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
rf.fit(x_train, y_train)
user_result = rf.predict(user_data)

# OUTPUT
st.subheader('Your Report: ')
output = ''
if user_result[0] == 1:
    output = 'low risk'
elif user_result[0] == 3:
    output = 'high risk'
else:
    output = 'Medium risk'

st.title(output)

st.subheader('Accuracy: ')

st.write(str(accuracy_score(y_test, rf.predict(x_test)) * 100) + '%')
