import joblib
import pandas as pd

preprocessor = joblib.load("/model/preprocessor.joblib")
model = joblib.load("/model/xgb_model.joblib")


# Define a function
def data_preprocessor(payload: dict):
    # Create a DataFrame from the payload with index 0
    payload_df = pd.DataFrame(payload, index=[0])

    # Estimate X_min and X_max based on the original data
    X_min = 0.00
    X_max = 952765.716

    scaled_value = model.predict(preprocessor.transform(payload_df))

    # Unscaled value approximation
    original_value = scaled_value * (X_max - X_min) + X_min
    return original_value
