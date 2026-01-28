# House Price Prediction (MLR vs KNN)

## Overview
Predicted house prices using Multiple Linear Regression and K-Nearest Neighbors
to understand key price drivers and compare model accuracy.

## Why this project
To analyze which housing features most influence price and evaluate whether a
traditional regression model or a machine-learning approach performs better.

## Data
- King County (Seattle) housing dataset (~21K records)
- Features include size, location, quality, and amenities

## Approach
- Cleaned and prepared numerical and categorical features
- Selected key predictors (grade, bathrooms, sqft, location, waterfront)
- Trained and validated MLR and KNN models (80/20 split)

## Key Findings
- Location, quality, and house size strongly impact price
- KNN (K=10) produced more accurate predictions
- MLR provided better interpretability

## Tools
Python, Pandas, Scikit-learn, Matplotlib
