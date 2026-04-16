# Cloud-Based Smart Health Prediction System

A full-stack machine learning application that predicts diabetes risk using patient health data. This project integrates **Machine Learning + FastAPI + Docker + AWS** to build a real-time healthcare prediction system.

---

## Features

- Predicts diabetes risk based on user input
- Real-time prediction using FastAPI
- Machine Learning model (Logistic Regression)
- Interactive modern web interface
- Dockerized application
- Deployed on AWS EC2
- Model and data stored in Amazon S3

---

## Machine Learning Model

- Algorithm: Logistic Regression  
- Dataset: PIMA Indian Diabetes Dataset (Kaggle)  
- Problem Type: Binary Classification  

### Model Performance

| Metric    | Value   |
|----------|--------|
| Accuracy | 70.78% |
| Precision| 60%    |
| Recall   | 50%    |
| F1 Score | 54.55% |

> Note: Recall can be improved for better detection of diabetic cases.

---

## Project Architecture
```
User Interface (HTML/CSS/JS)
↓
FastAPI Backend (Prediction API)
↓
ML Model (Logistic Regression)
↓
AWS EC2 (Deployment)
↓
Amazon S3 (Model Storage)
```
---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI  
- **Machine Learning:** Scikit-learn  
- **Containerization:** Docker  
- **Cloud:** AWS EC2, Amazon S3  

---

## Project Structure
```
health-project/
│
├── app.py # FastAPI backend
├── model.pkl # Trained ML model
├── index.html # Frontend UI
├── Dockerfile # Docker configuration
├── requirements.txt # Dependencies
```

---

## How to Run Locally

### 1️ Clone Repository
```
git clone https://github.com/YOUR_USERNAME/smart-health-predictor.git
cd smart-health-predictor
```
### 2 Install Dependencies
```
Install Dependencies
```
### 3 Open in Browser
```
http://127.0.0.1:8000/docs
```
### 4 Run with Docker
```
docker build -t health-app .
docker run -p 8000:8000 health-app
```

## AWS Deployment
- The application is deployed on AWS EC2 for public access.
- Amazon S3 is used for storing the trained model.
<img width="1905" height="856" alt="image" src="https://github.com/user-attachments/assets/bd5ac6f6-94a3-4d40-80a2-171cea16adbf" />
<img width="1839" height="463" alt="image" src="https://github.com/user-attachments/assets/4055b577-c4e4-44d8-a474-383162dba9c2" />
<img width="1908" height="1012" alt="image" src="https://github.com/user-attachments/assets/cab846be-3b6d-45ee-8e55-af03bb640b0b" />
<img width="1896" height="959" alt="image" src="https://github.com/user-attachments/assets/2f3faf6c-9b87-4f91-a7b3-dc9fd897f5e0" />

## Conclusion
This project demonstrates how machine learning and cloud computing can be integrated to build scalable healthcare solutions. It highlights real-world deployment of an ML model using modern backend frameworks and cloud infrastructure.


