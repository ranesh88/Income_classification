# Income Classification - Machine Learning Project

 ## Overview
This project aims to classify individuals' income based on demographic and socio-economic attributes using machine learning. It leverages various data preprocessing techniques and machine learning algorithms to predict whether an individual earns less than or more than 50K per year. The project utilizes a dataset that includes features such as age, education level, occupation, hours worked per week, and other personal information.

Table of Contents
Overview

Objective

Dataset

Technologies Used

Installation

Usage

Data Cleaning & Feature Engineering

Modeling

Results

Conclusion

License

Objective
The goal of this project is to develop a machine learning model that can predict whether an individual's income exceeds $50K per year based on various demographic and socio-economic features. This model can be useful for applications in financial planning, market targeting, and social-economic research.

Dataset
The dataset used for this project is the Adult Income Dataset from the UCI Machine Learning Repository. The dataset consists of the following columns:

age: Age of the individual

workclass: Type of employment

fnlwgt: Final weight (census sampling weight)

education: Education level

education_num: Number of years of education

marital_status: Marital status

occupation: Occupation type

relationship: Relationship status

race: Race of the individual

sex: Gender of the individual

capital_gain: Capital gain

capital_loss: Capital loss

hours_per_week: Number of hours worked per week

native_country: Country of origin

income: Income (<=50K or >50K)

Technologies Used
Python: Main programming language

Pandas: Data manipulation and analysis

Numpy: Numerical computing

Matplotlib & Seaborn: Data visualization

Scikit-learn: Machine learning models and utilities

XGBoost: Boosting algorithm for improved performance

Git LFS: For large file management

Installation
Prerequisites
To run this project locally, you need to have Python installed. You can download Python from here.

Steps to Install
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/ranesh88/Income_classification.git
Navigate to the project directory:

bash
Copy
Edit
cd Income_classification
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Once the installation is complete, you can run the Jupyter notebook or Python script to execute the machine learning workflow.

Running the Notebook
Install Jupyter Notebook if you don't have it:

bash
Copy
Edit
pip install notebook
Run the notebook:

bash
Copy
Edit
jupyter notebook
Open the notebook income_classification.ipynb in your browser and run the cells.

Running the Python Script
To run the script, simply execute the following:

bash
Copy
Edit
python income_classification.py
Data Cleaning & Feature Engineering
Data Cleaning
Missing Values: Rows with missing values represented by "?" were removed from critical columns like workclass, occupation, and native_country.

Whitespace and Inconsistencies: Removed leading/trailing whitespaces from categorical variables to ensure consistency.

Target Encoding: The income column was label-encoded to a binary format (0 for <=50K and 1 for >50K).

Feature Engineering
Education Hours: Combined education_num and hours_per_week to create a new feature called education_hours to capture the relationship between education and time spent working.

Age Group: Categorized age into age groups to identify income patterns across different age ranges.

Modeling
The machine learning model used for this project is the Random Forest Classifier. The model was chosen for its strong performance in classification tasks and its ability to handle both numerical and categorical features.

Model Performance
Accuracy: 91.4%

ROC AUC Score: 0.967

F1 Score: 0.91

Precision (class 1): 0.95

Recall (class 1): 0.87

Confusion Matrix
Predicted: 0	Predicted: 1
Actual: 0	4,677	221
Actual: 1	612	4,212

Insight: The model shows good performance with high precision for class 1 (income > 50K). However, there is a slightly higher false negative rate (612 cases where income >50K was predicted as <=50K), which is important for applications like financial targeting.

Results
Top 5 Feature Importances
Age (Importance: 0.1519): Strong correlation between age and accumulated work experience, which often leads to higher-paying jobs.

fnlwgt (Importance: 0.1510): Although not directly linked to income, fnlwgt serves as a proxy for demographic factors influencing income.

Capital Gain (Importance: 0.0772): Strong indicator that individuals with capital gains tend to earn more than $50K.

Marital Status: Married-civ-spouse (Importance: 0.0629): Marriage, especially in a civil union, is associated with higher income levels.

Hours per Week (Importance: 0.0432): Individuals working more hours generally earn more, although this varies by job type.

## Conclusion
This project demonstrates the power of machine learning in predicting income based on demographic and socio-economic factors. The Random Forest model performs exceptionally well, offering high accuracy and predictive power. Further refinements can be made by tuning hyperparameters or exploring other machine learning algorithms.

License
This project is licensed under the MIT License.

This README file offers a professional overview of your project, ensuring that anyone reviewing it will understand the context, installation process, usage, and results. 








