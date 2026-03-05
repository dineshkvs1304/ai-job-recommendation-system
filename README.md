# AI Job Recommendation System

## Overview

This project is an end-to-end machine learning system that recommends relevant job roles based on a user’s skills. The system takes a list of skills entered by the user and suggests the most relevant job titles by comparing those skills with a dataset of job descriptions.

The goal of this project was to build a practical machine learning application that goes beyond a notebook experiment. Instead of only training a model, the project demonstrates how a machine learning model can be integrated into a real software system with an API, database, frontend interface, and containerized deployment.

The system uses Natural Language Processing techniques to convert job descriptions and user skills into numerical features. These features are then compared using a similarity-based recommendation model to find the most relevant job matches.

This project was designed to simulate how machine learning systems are built and deployed in real production environments.

---

## System Architecture

The system follows a simple but realistic machine learning architecture.

User enters skills through the web interface  
                ↓  
Frontend sends request to FastAPI backend  
                ↓  
Backend processes the input skills  
                ↓  
ML recommendation engine calculates similarity  
                ↓  
Relevant job roles are retrieved from the dataset/database  
                ↓  
Recommended jobs are returned to the user

---

## Tech Stack

### Programming Language
Python

### Machine Learning
Scikit-learn  
TF-IDF Vectorization  
Nearest Neighbors Recommendation

### Backend
FastAPI  
Uvicorn

### Database
PostgreSQL

### Frontend
HTML  
CSS  
JavaScript

### Data Processing
Pandas  
NumPy

### Deployment
Docker  
Docker Compose

---

## Features

- Skill-based job recommendation system
- Natural Language Processing using TF-IDF
- Similarity based recommendation model
- FastAPI backend for model inference
- PostgreSQL database integration
- Simple web interface for user interaction
- Containerized deployment using Docker
- Clean modular project structure

---

## Project Structure

job-recommendation-system
│
├── api
│   └── app.py
│
├── data
│   └── jobs_dataset.csv
│
├── database
│   └── schema.sql
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── model
│   └── job_recommender.pkl
│
├── src
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── recommend.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## How the Recommendation Model Works

The recommendation system uses a simple but effective NLP approach.

1. Job descriptions and skills are cleaned and preprocessed.
2. The text data is converted into numerical vectors using TF-IDF.
3. A similarity search is performed using a Nearest Neighbors model.
4. When the user enters skills, the system converts them into a TF-IDF vector.
5. The model finds the closest matching job roles based on vector similarity.

This approach works well for matching skill keywords with job descriptions and provides fast recommendations.

---

## Running the Project Locally

### 1. Clone the repository

git clone https://github.com/yourusername/job-recommendation-system.git

cd job-recommendation-system


### 2. Create a virtual environment

python -m venv venv


Activate the environment

Windows

venv\Scripts\activate


Mac / Linux
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Start the FastAPI server

uvicorn api.app:app --reload


### 5. Open the application

Frontend page

http://127.0.0.1:5500/frontend/index.html


API documentation

http://127.0.0.1:8000/docs


---

## Running the Project with Docker

If Docker is installed, the entire system can be started using a single command.

### Build and start containers
docker-compose up --build


This will automatically start

- FastAPI backend
- PostgreSQL database
- Machine learning inference service

The API will be available at

http://localhost:8000/docs


---

## Example Usage

User enters skills such as

python machine learning sql


The system returns relevant job roles such as

- Machine Learning Engineer
- Data Scientist
- AI Engineer
- Data Analyst

---

## Future Improvements

Possible improvements that could be added to this system

- Larger real-world job dataset
- Deep learning based recommendation models
- User profile personalization
- Resume parsing and skill extraction
- Cloud deployment (AWS / GCP)
- Experiment tracking with MLflow

---

## Author

Kandyana Venkata Sai Dinesh

This project was developed as part of a machine learning engineering learning journey to understand how ML systems are designed, built, and deployed in real-world applications.
