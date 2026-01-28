# Restaurant Review Sentiment Analysis

## Overview
Built machine learning models to classify restaurant reviews as positive or negative
using customer text data.

## Why this project
To understand how different ML models perform on real-world text data and identify
which approach works best for sentiment analysis in the hospitality domain.

## Data
- Yelp restaurant reviews dataset
- Reviews labeled as positive (4–5 stars) or negative (1–2 stars)
- Neutral reviews removed for clearer classification

## Approach
- Cleaned and preprocessed review text
- Converted text to numerical features using TF-IDF
- Applied PCA and scaling where required
- Trained and compared multiple classification models

## Models Used
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree (CART)  
- Multinomial Naïve Bayes  
- Multiple Linear Regression (baseline)

## Key Findings
- Multinomial Naïve Bayes performed best (~92% accuracy)
- Logistic Regression and MLR also performed strongly
- KNN struggled with high-dimensional text data

## Tools
Python, Pandas, Scikit-learn, TF-IDF, PCA, Matplotlib
