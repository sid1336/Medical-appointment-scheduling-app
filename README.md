# 🏥 Predictive Scheduling Web App for Patient Appointments

## Overview
This project is a **machine-learning-powered web application** designed to predict patient appointment cancellations and optimize scheduling. Built using **Flask, Python, JavaScript, and HTML/CSS**, this app allows hospital receptionists to upload daily appointment schedules, compare them against historical data, and receive predictions on potential no-shows, late arrivals, and cancellations.

By leveraging a **Random Forest Classifier**, the system provides actionable recommendations, helping healthcare facilities optimize their resources, reduce wait times, and improve patient experiences.

---

## 🚀 Features
✅ **Machine Learning Model:** Uses a trained Random Forest Classifier to analyze patient appointment trends and predict cancellations.  
✅ **Excel File Upload:** Enables receptionists to easily upload the daily schedule for automated predictions.  
✅ **Actionable Recommendations:** Provides tailored strategies (e.g., reminders, rescheduling) based on patient demographics.  
✅ **Interactive Dashboard:** Displays predictions and insights through **dynamic charts and visualizations**.  
✅ **User-Friendly Interface:** Built with **Flask (backend)** and **JavaScript, HTML, CSS (frontend)** for seamless interaction.  
✅ **Scalable & Extendable:** Can integrate additional parameters such as weather conditions, past attendance trends, and other hospital data.

---

## 📌 Tech Stack
- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)  
- **Frontend:** HTML, CSS, JavaScript  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Plotly, Matplotlib  
- **Database:** SQLite (or can be extended to PostgreSQL/MySQL)  

---

## 📂 Project Structure
📂 predictive-scheduling-app  
│── 📂 static/             # CSS, JavaScript, images  
│── 📂 templates/          # HTML templates for Flask  
│── 📂 models/             # ML model training & storage  
│── 📂 uploads/            # Directory for uploaded Excel files  
│── app.py                # Main Flask backend  
│── requirements.txt       # Dependencies  
│── README.md              # Project documentation  
│── ml_model.py            # Machine learning


## ⚙️ Installation

1. **Clone the repository:**

   git clone https://github.com/yourusername/predictive-scheduling-app.git
   cd predictive-scheduling-app

2. **Install dependencies:**

   pip install -r requirements.txt

3. **Run the Flask app:**

   python app.py

4. **Open your browser and go to:**

   http://127.0.0.1:5000

---

## 📊 Machine Learning Model

The app leverages a **Random Forest Classifier**, an ensemble learning method that builds multiple decision trees and combines them for accurate predictions.

### 🔍 How It Works:
- Trained on **historical patient scheduling data** to identify patterns in cancellations.
- Uses **patient age, previous no-shows, and scheduling delays** to predict outcomes.
- Outputs a **"Cancelled"** or **"Not Cancelled"** label with **recommendations** to mitigate risks.

---

## 🏥 Use Case: Hospital Receptionists

**Problem:** Hospitals struggle with last-minute cancellations, leading to inefficiencies.  
**Solution:** This app **predicts** potential no-shows, allowing hospitals to **proactively** manage schedules.

### 📌 Example Use Case:

| Age | Previous No-Shows | Days Between Scheduling & Appointment | Prediction | Recommendation |
|----|------------------|---------------------------------|------------|---------------|
| 35  | 0              | 1                               | Cancelled  | Send a reminder email. |
| 50  | 1              | 10                              | Not Cancelled | No action needed. |
| 25  | 0              | 3                               | Cancelled  | Consider offering a rescheduling option. |

---

## 🤝 Contributing

Want to contribute? Follow these steps:

1. **Fork the repo**
2. **Create a new branch**  
   
   git checkout -b feature-name

3. **Commit your changes**  

   git commit -m 'Added feature'

4. **Push the branch**  

   git push origin feature-name

---

## 📜 License

This project is licensed under the **MIT License**.

---

**🚀 Made with ❤️ by Sid Sachdeva.**


