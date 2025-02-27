import pytest
import numpy as np
from app import app 

def test_flask_predict():
    # Create a test client for the Flask app
    with app.test_client() as client:
        # Define form data as a dictionary matching expected form field names
        to_predict = {
            "features": [13.2, 2.77, 2.51, 18.5, 103.0, 1.15, 2.61, 0.26, 1.46, 3.0, 1.05, 3.33, 820.0]
        }
        
        # Send a POST request to the /predict route with form data
        response = client.post('/predict', json=to_predict)
        
        # Check if the response contains the expected output
        assert response.status_code == 200
        assert 'Predicted Wine Class' in response.get_data(as_text=True)