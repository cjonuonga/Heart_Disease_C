# Exploratory data analysis plotting libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Models from Sci-kit-Learn & More

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier


# Model Evaluations
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score,f1_score
from sklearn.metrics import RocCurveDisplay
from sklearn.preprocessing import StandardScaler

# Exportation of Model
import joblib
from joblib import dump, load

'''
Necessary Patient Data:
Data Dictionary

1. age in years
2. sex - (1 = male; 0 = female)
3. cp - chest pain type:
    0: Typical angina: chest pain related decrease blood supply to the heart 
    1: Atypical angina: chest pain not related to heart 
    2: Non-anginal pain: typically esophageal spasms (non heart related) 
    3: Asymptomatic: chest pain not showing signs of disease

4. trestbps - resting blood pressure (in mm Hg on admission to the hospital) anything above 130-140 is typically cause for concern
5. chol - serum cholestoral in mg/dl serum = LDL + HDL + .2 * triglycerides above 200 is cause for concern
6. fbs - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) '>126' mg/dL signals diabetes
7.restecg - resting electrocardiographic results 
    0: Nothing to note 
    1: ST-T Wave abnormality can range from mild symptoms to severe problems 
        signals non-normal heart beat 
    2: Possible or definite left ventricular hypertrophy Enlarged heart's main 
        pumping chamber

8. thalach - maximum heart rate achieved
9. exang - exercise induced angina (1 = yes; 0 = no)
10. oldpeak - ST depression induced by exercise relative to rest looks at stress of heart during excercise unhealthy heart will stress more
11. slope - the slope of the peak exercise ST segment 0: Upsloping: better heart rate with excercise (uncommon) 1: Flatsloping: minimal change (typical healthy heart) 2: Downslopins: signs of unhealthy heart
12. ca - number of major vessels (0-3) colored by flourosopy colored vessel means the doctor can see the blood passing through the more blood movement the better (no clots)
13. thal - thalium stress result 1,3: normal 6: fixed defect: used to be defect but ok now 7: reversable defect: no proper blood movement when excercising
14. target - have disease or not (1=yes, 0=no) (= the predicted attribute)

'''
class HeartD:
    def __init__(self):
        # Loading Heart Disease Classification Model
        self.model = joblib.load('heart-disease-classification-mdl.pkl')

    def make_pred(self):
        self.age = int(input("Enter your age: "))
        self.sex = int(input("Enter sex (1 for male, 0 for female): "))
        self.cp = int(input("Enter level of chest pain 0: Typical angina: chest pain related decrease blood supply to the heart \n 1: Atypical angina: chest pain not related to heart \n 2: Non-anginal pain: typically esophageal spasms (non heart related) \n 3: Asymptomatic: chest pain not showing signs of disease: "))
        self.trestbps = int(input("Enter your resting blood pressure (in mm Hg on admission to the hospital) anything above 130-140 is typically cause for concern: "))
        self.chol = int(input("Enter your serum cholestoral in mg/dl serum = LDL + HDL + .2 * triglycerides above 200 is cause for concern: "))
        self.fbs = int(input("Enter your fasting blood sugar > 120 mg/dl (1 = true; 0 = false) '>126' mg/dL signals diabetes: "))
        self.restecg = int(input("Enter your resting electrocardiographic results \n 0: Nothing to note \n 1: ST-T Wave abnormality can range from mild symptoms to severe problems signals non-normal heart beat \n 2: Possible or definite left ventricular hypertrophy Enlarged heart's main pumping chamber: "))
        self.thalac = int(input("Enter your maximum heart rate achieved: "))
        self.exang = int(input("Enter your exercise induced angina (1 = yes; 0 = no): "))
        self.oldpeak = int(input("Enter your ST depression induced by exercise relative to rest looks at stress of heart during excercise unhealthy heart will stress more:  "))
        self.slope = int(input("Enter your the slope of the peak exercise ST segment \n 0: Upsloping: better heart rate with excercise (uncommon) \n 1: Flatsloping: minimal change (typical healthy heart) \n 2: Downslopins: signs of unhealthy heart: "))
        self.ca = int(input("number of major vessels (0-3) colored by flourosopy colored vessel means the doctor can see the blood passing through the more blood movement the better (no clots): "))
        self.thal = int(input("thalium stress result 1,3: normal \n 6: fixed defect: used to be defect but ok now \n 7: reversable defect: no proper blood movement when excercising: "))

        self.patient_attributes = (self.age, self.sex, self.cp, self.trestbps, self.chol, self.fbs, self.restecg, self.thalac, self.exang, self.oldpeak, self.slope, self.ca, self.thal)

        self.paitent_data = np.array([self.patient_attributes])


    #Model Making Prediction
        self.predict = self.model.predict(self.paitent_data)


        if self.predict[0] == 1:
            print(f"There is a moderate likelihood of heart disease detected.")
        else:
            print(f"There is a low likelihood of heart disease detected.")


HeartDisease = HeartD()

HeartDisease.make_pred()



