import pandas as pd

df=pd.read_csv("iraqi_dataset.csv")
df.dropna(inplace=True)
df.rename(columns={"CLASS": "disease"},inplace=True)
df.to_csv("cleaned_dataset.csv",index=False)
print("Dataset cleaned successfully")
