# Exploratory Data Analysis (EDA) Report

## Overview
This report presents an exploratory data analysis (EDA) of a dataset containing insurance-related information. The analysis aims to summarize the main characteristics of the data, visualize distributions, and identify trends across different categories.

## Data Overview
The dataset consists of **1,000,098 rows and 52 columns**, containing various features related to insurance policies, premiums, and claims.

## Libraries Used
The following libraries were utilized for data manipulation and visualization:
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Seaborn**: For statistical data visualization.
- **scikit-learn**: For machine learning algorithms and data preprocessing.
- **xgboost**: For gradient boosting algorithms.
- **shap**: For model interpretability and explanation.

## Instructions
### 1. Preprocess Data
First, convert and clean the data using the provided Python script:

```bash
python src/txt_to_csv_clean.py
jupyter notebook EDA_analysis.ipynb
jupyter notebook hypothesis_testing.ipynb
jupyter notebook statistical_modeling.ipynb
```