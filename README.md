# 🌱 Crop Recommendation AI

A machine learning project that recommends the most suitable crop based on soil and environmental conditions.

The system uses **Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall** as input features and uses a trained machine learning model to predict the recommended crop.

## 🚀 Try the Live Prediction App

👉 **[Open Crop Recommendation AI](https://croprecommendationai-ccubrnhhqg3gvwstnpz8ec.streamlit.app/)**

Click the button above to open the live Streamlit application and test the crop recommendation model.

### How it works

1. Open the Streamlit app.
2. Enter:

   * Nitrogen (N)
   * Phosphorus (P)
   * Potassium (K)
   * Temperature
   * Humidity
   * pH
   * Rainfall
3. Click **Recommend Crop**.
4. The application displays the predicted crop.

---

## 📌 Project Overview

Choosing an appropriate crop depends on several soil and environmental conditions. This project applies machine learning to learn the relationship between these conditions and suitable crops.

The project follows a complete machine learning workflow:

**Data Collection → Data Exploration → Data Preprocessing → Model Training → Model Comparison → Model Evaluation → Prediction → Model Saving → Deployment**

The best-performing model in the project is a **Random Forest Classifier**.

---

## 🎯 Objectives

The main objectives of this project are to:

* Analyze agricultural soil and environmental data.
* Understand the relationship between input conditions and crop types.
* Train multiple machine learning classification models.
* Compare their performance.
* Select the best-performing model.
* Predict a suitable crop for new input conditions.
* Calculate prediction probabilities.
* Save the trained model for later use.
* Prepare the model for deployment using Streamlit.

---

## 📊 Dataset

The dataset contains **2,200 observations** and **8 columns**.

### Input Features

| Feature       | Description        |
| ------------- | ------------------ |
| `N`           | Nitrogen content   |
| `P`           | Phosphorus content |
| `K`           | Potassium content  |
| `temperature` | Temperature        |
| `humidity`    | Humidity           |
| `ph`          | Soil pH            |
| `rainfall`    | Rainfall           |

### Target

| Column  | Description      |
| ------- | ---------------- |
| `label` | Recommended crop |

The dataset contains **22 crop classes**, with **100 observations for each crop**, making the dataset balanced.

---

## 🔎 Data Quality

The dataset was checked for:

* Missing values
* Duplicate records
* Data types
* Statistical characteristics
* Target-class distribution

The dataset contains **no missing values** and the duplicate check returned **zero duplicates**.

---

## 🧠 Machine Learning Models

Four classification algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting

### Model Comparison

| Model               | Test Accuracy |
| ------------------- | ------------: |
| Logistic Regression |        97.27% |
| Decision Tree       |        97.95% |
| Random Forest       |    **99.55%** |
| Gradient Boosting   |        98.86% |

Based on the test accuracy, **Random Forest Classifier** was selected as the final model.

---

## 🌳 Final Model

The final model is:

**RandomForestClassifier**

The model achieved approximately:

**99.55% test accuracy**

on the project's test set.

The dataset was divided into:

* **80% training data:** 1,760 samples
* **20% testing data:** 440 samples

The train/test split used stratification to preserve the distribution of crop classes.

---

## 📈 Model Evaluation

The Random Forest model was evaluated using:

* Accuracy
* Classification report
* Confusion matrix
* Correct and incorrect prediction analysis
* Feature importance

The model correctly classified **438 out of 440 test samples**, resulting in approximately **99.55% accuracy**.

---

## 🔥 Feature Importance

The Random Forest model identified the following feature importance values:

| Feature     | Importance |
| ----------- | ---------: |
| Rainfall    |     21.96% |
| Humidity    |     21.71% |
| K           |     18.08% |
| P           |     15.13% |
| N           |     10.34% |
| Temperature |      7.55% |
| pH          |      5.23% |

According to the trained Random Forest model, **rainfall** had the highest feature importance.

---

## 🤖 Prediction

After training, the model can predict a crop from new agricultural conditions.

Example inputs include:

```text
Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH
Rainfall
```

The prediction system returns:

* Predicted crop
* Prediction probability

For example:

```text
Predicted Crop: orange
Prediction Probability: 97.50%
```

The displayed probability represents the model's predicted probability for the selected class.

---

## 💾 Saved Model

The trained model is saved as:

```text
best_crop_prediction_model.pkl
```

The saved model can be loaded later without retraining the entire machine learning pipeline.

Example:

```python
import joblib

loaded_model = joblib.load("best_crop_prediction_model.pkl")
```

---

## 🖥️ Streamlit Application

The trained model is prepared for use in a **Streamlit web application**.

The application allows users to enter:

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* pH
* Rainfall

and receive a crop recommendation from the trained machine learning model.

---

## 📁 Project Structure

A recommended project structure is:

```text
Crop_Recommendation_AI/
│
├── data/
│   └── Crop_recommendation.csv
│
├── notebooks/
│   └── Crop_Recommendation_AI.ipynb
│
├── Deployment/
│   ├── app.py
│   ├── best_crop_prediction_model.pkl
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

### Main Files

**`data/Crop_recommendation.csv`**

Contains the crop recommendation dataset.

**`notebooks/Crop_Recommendation_AI.ipynb`**

Contains the complete machine learning workflow, including data analysis, model training, evaluation, feature importance, and prediction.

**`Deployment/app.py`**

Contains the Streamlit application.

**`Deployment/best_crop_prediction_model.pkl`**

Contains the trained Random Forest model.

**`Deployment/requirements.txt`**

Contains the Python packages required to run the application.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* Jupyter Notebook / VS Code
* Git
* GitHub

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/amanuelgebreabezgi01-bit/Crop_Recommendation_AI.git
```

Move into the project directory:

```bash
cd Crop_Recommendation_AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r Deployment/requirements.txt
```

---

## ▶️ Run the Streamlit Application

From the project directory, run:

```bash
streamlit run Deployment/app.py
```

Streamlit will start the local web application.

Open the displayed local address in your browser.

---

## 🔬 Machine Learning Workflow

The project follows these main steps:

### 1. Load the dataset

The agricultural dataset is loaded using Pandas.

### 2. Explore the data

The dataset is examined using:

```python
df.head()
df.info()
df.describe()
```

### 3. Check data quality

Missing values and duplicates are checked.

### 4. Separate features and target

The seven agricultural/environmental variables are used as input features, while `label` is the target.

### 5. Split the dataset

The data is divided into training and testing sets using an 80/20 split.

### 6. Train multiple models

Four classification algorithms are trained and compared.

### 7. Select the best model

Random Forest achieved the highest test accuracy.

### 8. Evaluate the model

The selected model is evaluated using accuracy, classification report, confusion matrix, and prediction analysis.

### 9. Analyze feature importance

Random Forest feature importance is used to understand which input variables contribute most strongly to predictions.

### 10. Save the model

The final model is saved using Joblib.

### 11. Deploy

The saved model is used by the Streamlit application for interactive crop recommendations.

---

## 📌 Limitations

This project is a machine learning prediction system and should not be interpreted as a complete agricultural decision-making system.

The prediction depends on the quality and distribution of the training dataset. Real-world agricultural decisions can also depend on factors that are not included in this dataset, such as:

* Local soil characteristics
* Seed variety
* Pest and disease conditions
* Farming practices
* Geographic location
* Seasonal conditions
* Market conditions

Therefore, the model should be considered a decision-support tool rather than a replacement for professional agricultural expertise.

---

## 🚀 Future Improvements

Possible future improvements include:

* Adding more geographically diverse agricultural data.
* Including additional soil properties.
* Adding location-based recommendations.
* Improving the user interface.
* Adding visual explanations for predictions.
* Adding model monitoring.
* Testing the model on external agricultural datasets.
* Adding more advanced machine learning models.
* Improving prediction interpretability.

---

## 👨‍💻 Author

**Amanuel Gebreabezgi**

Crop Recommendation AI — Machine Learning Project

---

## 📄 License

This project is intended for educational and demonstration purposes.
