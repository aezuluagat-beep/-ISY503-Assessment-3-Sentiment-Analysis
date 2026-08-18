# -ISY503-Assessment-3-Sentiment-Analysis
ISY503 Assessment 3 group project: Amazon Review Sentiment Analysis using NLP, neural networks and a Streamlit web application.

## Project Overview

This project develops a Natural Language Processing sentiment analysis system for Amazon product reviews.

The system classifies product reviews as positive or negative using neural network models. The project includes data preparation, text encoding, model comparison and evaluation, error analysis, and a Streamlit web application for testing new reviews.


## Model Development and Evaluation

Two neural network models were developed and compared:

- Baseline Neural Network
- Bidirectional LSTM (BiLSTM)

Both models were evaluated using the same validation data.

### Model Selection

| Model | Validation Accuracy |
|---|---:|
| Baseline Neural Network | 81.32% |
| BiLSTM | 80.14% |

The baseline model was selected because it achieved slightly better validation performance.

### Final Model Performance

The selected baseline model achieved:

- Test accuracy: 79.97%
- Test loss: 0.4218
- Correct predictions: 942 out of 1,178
- Misclassified reviews: 236
- Negative recall: 82%
- Positive recall: 78%

Error analysis showed that the model had more difficulty with negation, mixed sentiment and context. For example, “It is not bad for the price” was incorrectly classified as negative.


DIANA


## How to Run the Application

Required project files:
- app.py
- sentiment_model.keras
- tokenizer.json
- model_config.json

Run the Streamlit application with:

streamlit run app.py

The application allows a user to enter a new product review, select Analyse Sentiment, and receive a Positive or Negative prediction with a confidence score.

## Team Members

- Andrea Esthefania Zuluaga Toro – A00139192
- Monserrat Marquez Romero – A00156321
- Diana Luz Lozano Velasco – A00140612







