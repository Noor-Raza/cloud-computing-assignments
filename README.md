# Cloud Computing Assignments

This repository contains my work from the **Cloud Computing course**.  
Each project explores different aspects of cloud computing — from introductory experiments, to APIs, and finally serverless ML deployment.

---

## 📂 Repository Structure
- **cloud-intro-notebook/** → Cloud-based Jupyter notebook experiments.  
- **api-service-with-langserver/** → Python-based API + language server.  
- **serverless-ml-deployment/** → AWS Lambda + API Gateway ML deployment.  

Each section below includes detailed descriptions, setup instructions, and learnings.

---

# 1) Cloud Intro Notebook

This notebook contains exploratory work as part of **Assignment 1** in the Cloud Computing course.  

## 📝 Overview
- Understanding the basics of cloud computing environments.  
- Experimenting with cloud-based Jupyter notebook execution.  
- Running small-scale data experiments in a hosted environment.  

## 📂 Files
- `Assignment 1.ipynb` → Jupyter Notebook with exercises, explanations, and outputs.

## 🚀 How to Run
1. Open the notebook in Jupyter or Google Colab.
2. Run the cells in order to reproduce the outputs.

## 🎯 Key Learnings
- How to leverage cloud notebooks for experimentation.  
- Experience with cloud-hosted execution environments.  
- Familiarization with basic data processing in the cloud.

---

# 2) API Service with Language Server

This project demonstrates creating and running a **custom API service** and a **language server** in Python.

## 📝 Overview
- Built a simple Python-based API.  
- Implemented a language server to handle requests.  
- Practiced designing and running services in a cloud-ready architecture.  

## 📂 Files
- `assignment 2_myapi.py` → Defines the custom API service.  
- `assignment 2_langserv.py` → Implements the language server.

---

# 3) Serverless Machine Learning Deployment

This project demonstrates deploying a machine learning model using **AWS Lambda** and **API Gateway**.  
It covers training, packaging, deploying, and testing a serverless ML application.

## 📝 Overview
- Trained a simple ML model.  
- Packaged the model for serverless deployment.  
- Wrote a Lambda handler to serve predictions.  
- Integrated AWS Lambda with API Gateway for REST API access.  
- Tested predictions using real inputs.  

## 📂 Files
- `assignment 3_model.ipynb` → Model training notebook.  
- `assignment 3_model.py` → Python script version of the trained model.  
- `assignment 3_lambda.py` → AWS Lambda handler.  
- `assignment 3_lambda_output.py` → Example Lambda response.  
- `assignment 3_url.txt` → API Gateway endpoint URL.  
- `assignment 3_test.txt` → Example input for API testing.  
   ```bash
   python assignment\ 2_myapi.py
