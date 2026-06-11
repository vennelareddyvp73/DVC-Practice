"""
version pulling 




"""
import pandas as pd 
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:/Users/venne/Videos/DVC-Practice/data/diabetes.csv")
X = df.drop(columns = ["Outcome"])
y = df['Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

df_scaled = pd.DataFrame(X_scaled, columns = X.columns)
df_scaled['Outcome'] = y

df_scaled.to_csv("C:/Users/venne/Videos/DVC-Practice/data/diabetes.csv", index = False)


"""

dvc add data/

git add data.dvc
git commit -m "Add scaled diabetes data"

dvc push 

## Go to version 1
git checkout HEAD ~1 data.dvc
dvc checkout

## Go to version 2

git checkout main data.dvc
dvc checkout

"""
