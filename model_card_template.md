# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Developer: Jesse Bettridge
Model Date: 9/15/2026
Model Version: 1.0
Model Type: Random forest Classifier

Training Algorithms and Parameters: 

The model is trained using sklearn's Random Forest algorithm with 100 estimators and a fixed random seed to support reproducibility. Features are derived from census data and include demographic and socioeconomic variables like age, workclass, education, marital status, occupation, relationship, race, sex, capital, hours worked per week, and native country.

Contact: 

For questions about the model, contact jbettri@wgu.edu

## Intended Use

The model predicts whether an individual's income exceeds $50k per year and uses census data. 

Intended users include data scientists, population data researchers, and others interested in income prediction models.

Out-of-Scope Use Case:

This model is not intended for high-stakes decisions without oversight. This includes credit approval or hiring of individuals. 

## Training Data

Datasets: 
The data consists of the census.csv dataset, split into training and test datasets. 

## Evaluation Data

Datasets: 

The model is evaluated on a test set made from the census.csv Income dataset. This assesses the model's generalization and fairness on unseen data. 

## Metrics
The model was evaluated using precision, recall, and F1 score, standard metrics for classification tasks that provide insight into the balance between false positives and false negatives.

Precision: 0.7317 | Recall: 0.6114 | F1: 0.6662

The precision score indicates that nearly 73% of the model's positive predictions were correct. The recall shows that the model identifies nearly 61% of all actual positive cases. 

The F1 score balances these two metrics and provides an overall measure of predictive accuracy. These results suggest the model performs reasonably well but could benefit from further tuning. 

## Ethical Considerations

The model may contain biases in the training data, such as socioeconomic or demographic features. Do not use the model for decisions that will impact individuals. The dataset maintains individual privacy by using publicly available data that anonymizes individuals. 

## Caveats and Recommendations

Performance may vary across demographic groups. Use the model as a decision-support tool rather than an automated decision-making tool. Future work includes incorporating fairness constraints and expanding evaluation to more diverse datasets. 