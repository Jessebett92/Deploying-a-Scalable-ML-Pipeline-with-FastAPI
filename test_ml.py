import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics

# add necessary import

# implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # train_model test

    Testing that train_model function will return
    a trained RandomForestClassifier model
    when given training data. 
    """

    # Create dummy training data
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])
    model = train_model(X_train, y_train)
    
    # Check that the model is a RandomForestClassifier instance
    assert isinstance(model, RandomForestClassifier)


# implement the second test. Change the function name and input as needed
def test_inference():
    """
    # Inference test

    I'm testing that the inference function returns 
    reasonable predictions based on the values below. 
    """
    
    # Create dummy training data and train model
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])
    model = train_model(X_train, y_train)
    
    # Create dummy test data
    X_test = np.array([[2, 3], [4, 5]])
    
    preds = inference(model, X_test)
    
    # Check that predictions length matches input samples
    assert len(preds) == X_test.shape[0]
    
    # Check that predictions have class labels (integers).
    assert all(isinstance(p, (int, np.integer)) for p in preds)


# TODO: implement the third test. Change the function name and input as needed
def test_model_metrics():
    """
    Model Metrics Test

    I'm testing that the compute_model_metrics function returns 
    precision, recall, and fbeta scores between the valid range
     of 0 and 1. 
    """
    
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    print(f"precision: {precision: .4f}, Recall: {recall: .4f}, F1: {fbeta: .4f}")

    assert (precision, recall, fbeta) == pytest.approx((1.0, 2/3, 0.8))
    
    # Check that all metrics are floats between 0 and 1
    for metric in (precision, recall, fbeta):
        assert isinstance(metric, float)
        assert 0.0 <= metric <= 1.0
