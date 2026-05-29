import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df=pd.read_csv("cleaned_dataset.csv")
#features
X =df[["AGE","Chol","TG","HDL","LDL","VLDL","BMI","HbA1c"]]
#Target column
encoder = LabelEncoder()
y=encoder.fit_transform(df["disease"])
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
#train model
model =RandomForestClassifier(n_estimators=150,random_state=42)
model.fit(X_train,y_train)
#save model
joblib.dump(model,"model.pkl")
#save encoder
joblib.dump(encoder,"encoder.pkl")
print("Model trained successfully")
