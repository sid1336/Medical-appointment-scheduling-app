from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

app = Flask(__name__)

# Load and train the model on historical data when the app starts
def load_and_train_model():
    # Load historical data
    historical_data = pd.read_excel('historical_appointments.xlsx')

    # Separate features and target
    X = historical_data[['age', 'previous_no_show', 'time_between_scheduling_and_appointment']]
    y = historical_data['appointment_cancelled']

    # Train the model
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

# Initialize model
model = load_and_train_model()

# Render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for uploading today's appointments
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read the uploaded Excel file into a pandas DataFrame
        today_df = pd.read_excel(file)

        # Check if required columns are in the uploaded file
        required_columns = ['age', 'previous_no_show', 'time_between_scheduling_and_appointment']
        if not all(col in today_df.columns for col in required_columns):
            return jsonify({'error': 'Uploaded file is missing required columns'}), 400

        # Use the model to predict cancellations for today's appointments
        today_df['prediction'] = model.predict(today_df[['age', 'previous_no_show', 'time_between_scheduling_and_appointment']])
        today_df['prediction'] = today_df['prediction'].apply(lambda x: 'Cancelled' if x == 1 else 'Not Cancelled')

        # Generate recommendations based on predictions and age groups
        recommendations = []
        for _, row in today_df.iterrows():
            if row['prediction'] == 'Cancelled':
                if row['age'] < 18:
                    recommendations.append("Send a reminder email to parents or guardians.")
                elif 18 <= row['age'] < 30:
                    recommendations.append("Consider sending a personalized text reminder.")
                elif 30 <= row['age'] < 50:
                    recommendations.append("Consider offering a rescheduling option.")
                else:
                    recommendations.append("Send an early reminder email and provide an easy option to reschedule.")
            else:
                recommendations.append("No preventive action required.")

        # Add recommendations to the DataFrame
        today_df['recommendation'] = recommendations

        # Convert the comparison results to JSON format for the frontend
        result_data = today_df[['age', 'previous_no_show', 'time_between_scheduling_and_appointment', 'prediction', 'recommendation']].to_dict(orient='records')
        return jsonify({'comparison': result_data})

    except Exception as e:
        return jsonify({'error': f'Failed to process file: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
