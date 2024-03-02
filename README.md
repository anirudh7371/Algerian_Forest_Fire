
# Algerian Wildfire Predictor

## Overview
The Algerian Wildfire Predictor is a machine learning project aimed at predicting the likelihood of forest fires in Algeria based on various environmental factors. This project utilizes a dataset containing information about temperature, relative humidity, wind speed, rainfall, and other relevant features to train a predictive model. The trained model can then be used to provide insights into the potential occurrence of forest fires, aiding in fire prevention efforts.

## Project Structure
- **notebooks/**: Directory containing Jupyter notebooks for data preprocessing (`Algerian_Forest_Fire.ipynb`) and model training (`model_training.ipynb`).
- **dataset/**: Contains two datasets: one raw and the other cleaned.
- **app.py**: Flask application for deploying the trained model as a web service.
- **templates/**: Directory containing HTML templates for the web interface.
- **models/**: Directory containing serialized trained models and scalers.
- **requirements.txt**: List of Python dependencies required to run the project.
- **README.md**: Documentation file providing an overview of the project and instructions for running it.

## Dataset Description

The Algerian Wildfire Predictor project utilizes the Algerian Forest Fires dataset, which is publicly available on the UCI Machine Learning Repository. This dataset contains information about forest fires in Algeria, focusing on various environmental factors that may contribute to the occurrence of wildfires. Here's a brief overview of the dataset:

- **Title**: Algerian Forest Fires Dataset
- **Source**: UCI Machine Learning Repository
- **URL**: [Algerian Forest Fires Dataset](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset)
- **Attributes**:
  1. **day**: Day of the month (1-31).
  2. **month**: Month of the year (1-12).
  3. **year**: Year (2012 or 2013).
  4. **temperature**: Temperature in Celsius degrees.
  5. **RH**: Relative humidity (%).
  6. **WSPM**: Wind speed in meters per second.
  7. **rain**: Rainfall in millimeters per square meter.
  8. **FFMC**: Fine Fuel Moisture Code (numeric rating of the moisture content of litter and other cured fine fuels).
  9. **DMC**: Duff Moisture Code (numeric rating of the average moisture content of loosely compacted organic layers of moderate depth).
  10. **DC**: Drought Code (numeric rating of the average moisture content of deep, compact organic layers).
  11. **ISI**: Initial Spread Index (numeric rating of the expected rate of fire spread).
  12. **BUI**: Buildup Index (numeric rating of the total amount of fuel available for combustion).
  13. **FWI**: Fire Weather Index (numeric rating of fire intensity).
  14. **Classes**: Class attribute indicating the severity of the fire danger (Classes: 'low', 'moderate', 'high', 'very high', 'extreme').

This dataset provides a comprehensive set of features related to weather conditions and environmental indices, along with the corresponding severity of fire danger. It serves as the foundation for training the predictive model in the Algerian Wildfire Predictor project, enabling accurate assessments of wildfire risks based on current environmental factors.

By leveraging this dataset and machine learning techniques, the Algerian Wildfire Predictor aims to enhance wildfire prevention efforts by providing timely predictions and insights into the likelihood of forest fires in Algeria.

## Getting Started
To run the Algerian Wildfire Predictor project on your local machine, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone <repository_url>
   ```

2. Install the required dependencies listed in the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

3. Set up the dataset by updating the dataset location in the data processing script (`notebooks/Algerian_Forest_Fire.ipynb`). Open the notebook in a Jupyter environment and locate the `read_csv` function. Update the file path in the `read_csv` function to point to the dataset file on your system.

4. Run the data processing script (`notebooks/Algerian_Forest_Fire.ipynb`) to preprocess the dataset.

5. Train the machine learning model by running the model training script (`notebooks/model_training.ipynb`). This script will train the model using the preprocessed data and save the trained model and scaler.

6. Set up the Flask application by updating the paths to the trained model and scaler in the `app.py` file to point to the location of the saved model and scaler on your system.

7. Start the Flask application by running the `app.py` script:

   ```
   python app.py
   ```

8. Access the web interface of the Algerian Wildfire Predictor by opening a web browser and navigating to `http://localhost:5001`. You can input environmental factors to get predictions on the likelihood of forest fires.

## Contribution
Contributions to the Algerian Wildfire Predictor project are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.
