from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the full pipeline (preprocessor + model)
try:
    full_pipeline = joblib.load('full_pipeline.joblib')  # This contains both the preprocessor and the model
except Exception as e:
    print(f"Error loading the pipeline: {e}")
    raise

# 👉 Home route to render HTML form
@app.route('/')
def home():
    return render_template('index.html')

# 👉 POST handler for form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form

        # Create DataFrame from form input
        input_dict = {
            'age': [int(form['age'])],
            'workclass': [form['workclass']],
            'fnlwgt': [int(form['fnlwgt'])],
            'education': [form['education']],
            'education_num': [int(form['education_num'])],
            'marital_status': [form['marital_status']],
            'occupation': [form['occupation']],
            'relationship': [form['relationship']],
            'race': [form['race']],
            'sex': [form['sex']],
            'capital_gain': [int(form['capital_gain'])],
            'capital_loss': [int(form['capital_loss'])],
            'hours_per_week': [int(form['hours_per_week'])],
            'native_country': [form['native_country']],
            'education_hours': [form['education_hours']],
            'age_group': [form['age_group']]
        }

        input_df = pd.DataFrame(input_dict)

        # Make prediction using the full pipeline (preprocessor + model)
        prediction = full_pipeline.predict(input_df)[0]  # full_pipeline contains both the model and preprocessor

        # Return appropriate message based on the prediction result
        if prediction == 1:
            result_message = "Possibility of Income is Low (<=50K)"
        else:
            result_message = "Possibility of Income is High (>50K)"

        # Render the result on the HTML page
        return render_template('index.html', result_message=result_message)

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
