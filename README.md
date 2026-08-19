# -ISY503-Assessment-3-Sentiment-Analysis
ISY503 Assessment 3 group project: Amazon Review Sentiment Analysis using NLP, neural networks and a Streamlit web application.

## Project Overview

This project develops a Natural Language Processing sentiment analysis system for Amazon product reviews.

The system classifies product reviews as positive or negative using neural network models. The project includes data preparation, text encoding, model comparison and evaluation, error analysis, and a Streamlit web application for testing new reviews.

MONSERRAT



## Model Development and Evaluation

Two neural network models were developed and compared:

- Baseline Neural Network
- Bidirectional LSTM (BiLSTM)

Both models were evaluated using the same validation data.

### Model Selection

| Model | Validation Accuracy | Validation Loss |
|---|---:|---:|
| Baseline Neural Network | 79.88% | 0.4264 |
| BiLSTM | 78.95% | 0.4641 |

The baseline model was selected because it achieved slightly higher validation accuracy and lower validation loss.

### Final Model Performance

The selected baseline model achieved:

- Test accuracy: 80.05%
- Test loss: 0.4151
- Correct predictions: 943 out of 1,178
- Misclassified reviews: 235
- Negative recall: 86%
- Positive recall: 74%

The confusion matrix was:

|  | Predicted Negative | Predicted Positive |
|---|---:|---:|
| Actual Negative | 503 | 80 |
| Actual Positive | 155 | 440 |

The model identified negative reviews more effectively than positive reviews. Error analysis also showed difficulties with negation, mixed sentiment and context.


## Deployment, Limitations and Ethics
 
A Streamlit web application was created to allow users to enter a product review and receive a Positive or Negative prediction.
 
The application uses the saved model, tokenizer and preprocessing settings from the final model. It also displays a confidence score.
 
The final demonstration was accessed through a temporary Cloudflare tunnel.
 
### Limitations and Ethical Considerations
 
The model has several limitations:
 
- positive and negative labels can include subjective human decisions;
- negation and mixed sentiment can be difficult for the model;
- the dataset contains only four Amazon product categories;
- confidence does not guarantee that a prediction is correct;
- the final model identified negative reviews more effectively than positive reviews, with recall of 86% for negative reviews and 74% for positive reviews.
 
These results show that performance is not identical across the two sentiment classes. Model predictions should therefore be interpreted carefully and used as support rather than treated as definitive judgements.

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







