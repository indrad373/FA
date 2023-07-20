import streamlit as st
import webbrowser
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
from sklearn.metrics import accuracy_score

# membaca dataset dari file CSV
data = pd.read_csv("./pages/personas.csv")

#Baca Dataframe
#st.write(data.head(10))

nan_df = data[data.isna().any(axis=1)]

data = data.dropna(axis=0)
#st.write(data.head())
#st.write(data.info())
#st.write(data.describe())

# Mentranformasi data kedalam bentuk angka
labelencoder = LabelEncoder()
data['Nama_Anak'] = labelencoder.fit_transform(data['Nama_Anak'])
data['Jenis_Kelamin'] = labelencoder.fit_transform(data['Jenis_Kelamin'])
data['Jawaban_1'] = labelencoder.fit_transform(data['Jawaban_1'])
data['Jawaban_2'] = labelencoder.fit_transform(data['Jawaban_2'])
data['Jawaban_3'] = labelencoder.fit_transform(data['Jawaban_3'])
data['Jawaban_4'] = labelencoder.fit_transform(data['Jawaban_4'])
data['Jawaban_5'] = labelencoder.fit_transform(data['Jawaban_5'])
data['Jawaban_6'] = labelencoder.fit_transform(data['Jawaban_6'])
data['Jawaban_7'] = labelencoder.fit_transform(data['Jawaban_7'])
data['Jawaban_8'] = labelencoder.fit_transform(data['Jawaban_8'])
data['Jawaban_9'] = labelencoder.fit_transform(data['Jawaban_9'])
data['Jawaban_10'] = labelencoder.fit_transform(data['Jawaban_10'])
data['Jawaban_11'] = labelencoder.fit_transform(data['Jawaban_11'])
data['Jawaban_12'] = labelencoder.fit_transform(data['Jawaban_12'])
data['Jawaban_13'] = labelencoder.fit_transform(data['Jawaban_13'])
data['Jawaban_14'] = labelencoder.fit_transform(data['Jawaban_14'])
data['Jawaban_15'] = labelencoder.fit_transform(data['Jawaban_15'])
data['Jawaban_16'] = labelencoder.fit_transform(data['Jawaban_16'])
data['VARK Label'] = labelencoder.fit_transform(data['VARK Label'])

#st.write(sns.heatmap(data.corr(method='spearman'), linewidths=4, annot=True))

data['Nama_Anak'] = pd.to_numeric(data['Nama_Anak'])
data['Jenis_Kelamin'] = pd.to_numeric(data['Jenis_Kelamin'])
data['Jawaban_1'] = pd.to_numeric(data['Jawaban_1'])
data['Jawaban_2'] = pd.to_numeric(data['Jawaban_2'])
data['Jawaban_3'] = pd.to_numeric(data['Jawaban_3'])
data['Jawaban_4'] = pd.to_numeric(data['Jawaban_4'])
data['Jawaban_5'] = pd.to_numeric(data['Jawaban_5'])
data['Jawaban_6'] = pd.to_numeric(data['Jawaban_6'])
data['Jawaban_7'] = pd.to_numeric(data['Jawaban_7'])
data['Jawaban_8'] = pd.to_numeric(data['Jawaban_8'])
data['Jawaban_9'] = pd.to_numeric(data['Jawaban_9'])
data['Jawaban_10'] = pd.to_numeric(data['Jawaban_10'])
data['Jawaban_11'] = pd.to_numeric(data['Jawaban_11'])
data['Jawaban_12'] = pd.to_numeric(data['Jawaban_12'])
data['Jawaban_13'] = pd.to_numeric(data['Jawaban_13'])
data['Jawaban_14'] = pd.to_numeric(data['Jawaban_14'])
data['Jawaban_15'] = pd.to_numeric(data['Jawaban_15'])
data['Jawaban_16'] = pd.to_numeric(data['Jawaban_16'])
data['VARK Label'] = pd.to_numeric(data['VARK Label'])

#st.write(data.head())

data['VARK Label'] = np.where(((data['Visual'] > 4) & (data['Auditory'] <= 4) & (data['Read/Write'] <= 4) &  (data['Kinesthetic'] <= 4)) ,'Visual',
          np.where(((data['Visual'] <= 4) & (data['Auditory'] > 4) & (data['Read/Write'] <= 4) &  (data['Kinesthetic'] <= 4)), 'Auditory',
          np.where(((data['Visual'] <= 4) & (data['Auditory'] <= 4) & (data['Read/Write'] > 4) &  (data['Kinesthetic'] <= 4)), 'Read/Write',
          np.where(((data['Visual'] <= 4) & (data['Auditory'] <= 4) & (data['Read/Write'] <= 4) &  (data['Kinesthetic'] > 4)), 'Kinesthetic',
          np.where(((data['Visual'] > 4) & (data['Auditory'] > 4) & (data['Read/Write'] <= 4) &  (data['Kinesthetic'] <= 4)), 'Mixed Vis-Au',
          np.where(((data['Visual'] > 4) & (data['Auditory'] <= 4) & (data['Read/Write'] > 4) &  (data['Kinesthetic'] <= 4)), 'Mixed Vis-RW',
          np.where(((data['Visual'] > 4) & (data['Auditory'] <= 4) & (data['Read/Write'] <= 4) &  (data['Kinesthetic'] > 4)), 'Mixed Vis-Kines',
          np.where(((data['Visual'] <= 4) & (data['Auditory'] > 4) & (data['Read/Write'] > 4) &  (data['Kinesthetic'] <= 4)), 'Mixed Au-RW',
          np.where(((data['Visual'] <= 4) & (data['Auditory'] > 4) & (data['Read/Write'] <= 4) &  (data['Kinesthetic'] > 4)), 'Mixed Au-Kines',
          np.where(((data['Visual'] <= 4) & (data['Auditory'] <= 4) & (data['Read/Write'] > 4) &  (data['Kinesthetic'] > 4)), 'Mixed Rw-Kines', 'Lainnya'))))))))))

#st.write(data.head())

#################################################################################################

# memisahkan fitur dan target
X = data.drop(columns=["Nama_Anak","Jenis_Kelamin","VARK Label"])
y = data["VARK Label"]

# membagi dataset menjadi data latih 80% dan data uji 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# membuat model Random Forest
clf = DecisionTreeClassifier()

# melatih model dengan data latih
clf.fit(X_train, y_train)

# melakukan prediksi dengan data uji
y_pred = clf.predict(X_test)

#################################################################################################

# Preprocessing
X = data.drop(columns=data.iloc[:, :19])
y = data["VARK Label"]

# Encode categorical variables using LabelEncoder
le = LabelEncoder()
X_encoded = X.copy()
for col in X.columns:
    if X[col].dtype == "object":
        X_encoded[col] = le.fit_transform(X[col])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    "max_depth": [3, 5, 7],
    "min_samples_split": [2, 3, 4],
    "criterion": ["gini", "entropy"]
}
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(),
    param_grid=param_grid,
    cv=5,
    scoring="accuracy"
)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_

# Train the decision tree classifier with best parameters
clf = DecisionTreeClassifier(**best_params)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)


#################################################################################################

def redirect(_url):
    link = _url
    webbrowser.open(link)

st.subheader("Result")

if "pred_result" not in st.session_state:
    st.text("Hasil gaya belajar baru dapat ditentukan setelah anda mengisi kuisioner dihalaman\nkuisioner. Silahkan mengisi kuisioner terlebih dahulu")
    
else:
    # Implementasi machine learning
    new_data = {"Visual": st.session_state["vis"], "Auditory" : st.session_state["aud"], "Read/Write" : st.session_state["readW"],"Kinesthetic" : st.session_state["kines"]}

    # membuat array 2 dimensi dari data baru
    X_new = pd.DataFrame([new_data])

    # melakukan prediksi dengan model
    y_new = clf.predict(X_new)

    # menampilkan hasil prediksi
    st.write("Hasil gaya belajar yang tepat untuk anak anda adalah:", y_new[0])

    reset = st.button("Reset hasil")
    if reset:
        redirect('http://localhost:8502/Question')

#################################################################################################