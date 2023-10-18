# SalesSense - Real-time Interactive Sales Forecasting Web Application 📈📊

SalesSense is an intuitive web app powered by cutting-edge machine learning models that provides real-time sales forecasts, helping businesses optimize inventory, boost profits, and make data-driven decisions effortlessly 💼💰🤖

## Introduction 

The SalesSense app leverages machine learning models to provide real-time sales forecasts for businesses. It offers an intuitive and user-friendly interface to input relevant data and instantly receive sales predictions.

## Features 

- Real-time sales predictions.
- Interactive user interface.
- Visualize sales trends over time.
- User-friendly design.
- Support for different product families.
- Data preprocessing and model training.


## App Structure 

- `src`: The main application directory.
- `app/`: Directory containing app components, utility functions and the main application script `app.py`.
- `model/`: Directory for storing pre-trained model and preprocessing tool.
- `notebook/`: Directory containing the data and the jupyter notebook for model training.

## Usage 📊

### Making Predictions 📈

1. Fill in the required fields such as the family of the store, store type, date, items on promotion, previous sales, and rolling mean.
2. Click the "Submit" button to receive a real-time sales prediction.

### Viewing Sales Trends 📉

1. Click the "View Trends" tab on the app.
2. Explore the historical sales trends using the line chart.
3. Click the "Make Prediction" button to go back to the prediction form.

## Technologies Used 💻🔬

- Streamlit: Python web application framework.
- Pandas: Data manipulation and analysis library.
- Scikit-Learn: Machine learning library.
- XGBoost: Gradient boosting library.
- Joblib: Serialization and deserialization of models.
- HTML/CSS: Styling and layout.

## Data Preprocessing 🧹🧮

The app preprocesses input data to ensure compatibility with the machine learning model. It scales and transforms the data as needed for accurate predictions using the preprocessor exported from the notebook.

## Model Training 🤖📓

The app employs a pre-trained XGBoost machine learning model (Details about training can be found in the notebook). The model was trained on historical sales data to provide accurate forecasts.


## Author✍️

Aryee Kwaku Geoffrey
