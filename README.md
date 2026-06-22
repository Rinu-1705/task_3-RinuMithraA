# Recommendation System

The Recommendation System is a Python-based job role matcher that analyzes user skills and recommends the most suitable job positions. It uses **TF-IDF vectorization** and **cosine similarity** to find the best matches between user skills and available job roles.

## Features
- **Interactive Input**: Users enter their skills as a space-separated string
- **Intelligent Matching**: Uses machine learning algorithms (TF-IDF + Cosine Similarity) for accurate recommendations
- **Top Results**: Returns the top 3 most relevant job roles based on skill match
- **Scoring System**: Displays similarity scores for each recommendation

## How It Works

### Algorithm
1. **Vectorization**: Converts skill descriptions (both user input and job role descriptions) into numerical vectors using TF-IDF
2. **Similarity Calculation**: Computes cosine similarity between user profile and each job role
3. **Ranking**: Sorts results by similarity score in descending order
4. **Output**: Displays top 3 matches with their confidence scores


### Example
```
Enter your skills (space-separated): Python Machine Learning AWS Statistics Data Analysis

Top Recommendations:
Data Scientist (score: 0.89)
AI Engineer (score: 0.78)
Backend Developer (score: 0.45)
```

## How to Interpret Results
- **Score Range**: 0.00 to 1.00
- **Higher Score**: Better match between user skills and job role requirements
- **Score 0.80+**: Strong recommendation
- **Score 0.50-0.79**: Moderate match
- **Score Below 0.50**: Weak match but still listed in top 3

## Input Tips
For best results, enter your skills clearly and specifically:
- Good: "Python SQL Machine Learning AWS"
- Poor: "good at programming and stuff"
