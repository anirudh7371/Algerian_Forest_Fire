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
