# Online Payments Fraud Detection using Machine Learning

## 📌 Project Overview
Online Payments Fraud Detection using Machine Learning is a proactive system designed to identify and prevent fraudulent activities during digital payment transactions. With the rapid growth of online banking, UPI payments, card transactions, and e-commerce platforms, detecting fraud in real time has become a critical challenge.

This project leverages historical transaction data and machine learning algorithms to analyze transaction patterns and classify transactions as either legitimate or fraudulent, helping improve the security and reliability of online payment systems.

---

## 🎯 Objectives
- To detect fraudulent online payment transactions using machine learning
- To analyze transaction behavior patterns from historical data
- To provide real-time fraud prediction through a web-based interface
- To enhance trust and security in digital payment platforms

---

## 🧠 How the System Works
1. The user enters transaction details through a web interface.
2. Transaction data is sent to the Flask backend.
3. The machine learning model analyzes features such as:
   - Transaction amount
   - Transaction type
   - Account balance changes
4. The trained model predicts whether the transaction is:
   - ✅ Legitimate  
   - ⚠️ Fraudulent
5. The result is displayed instantly to the user.

The model continuously improves by learning from historical transaction data, allowing it to adapt to evolving fraud patterns.

---

## 💻 Technology Stack
- **Programming Language:** Python  
- **Web Framework:** Flask  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Frontend:** HTML, CSS, JavaScript  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure
frauddetection/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── model/
│ ├── fraud_model.pkl
│ ├── scaler.pkl
│ └── type_encoder.pkl
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── favicon.ico
│
└── data/
└── creditcard.csv (not included in GitHub)

---

## 📊 Dataset Information
Due to GitHub file size limitations, the dataset is **not included** in this repository.

**Dataset Source:**  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Please download the dataset manually and place it inside the `data/` folder before training the model.

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Shahuljani/frauddetection.git
cd frauddetection
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000
