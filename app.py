from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# import Linear Regression and Scaler models
linear_reg_model = pickle.load(open('models/regressor.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# routing to the app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Convert input data to floats
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Scale the input data
        new_data = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

        # Predict using the model
        result = linear_reg_model.predict(new_data)

        result_list = result.tolist()

        # Return the prediction result as JSON
        return jsonify({'prediction': result_list[0]})
    else:
        return render_template('prediction.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
