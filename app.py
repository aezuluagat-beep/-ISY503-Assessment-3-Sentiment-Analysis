
import json
import re

import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json


# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="Amazon Review Sentiment Analysis",
    page_icon="🧠",
    layout="centered"
)


# ======================================================
# Load Model and Preprocessing Settings
# ======================================================

@st.cache_resource
def load_resources():

    # Load the selected trained model.
    model = tf.keras.models.load_model(
        "sentiment_model.keras"
    )

    # Load the tokenizer used during training.
    with open(
        "tokenizer.json",
        "r",
        encoding="utf-8"
    ) as file:

        tokenizer = tokenizer_from_json(
            file.read()
        )

    # Load preprocessing configuration.
    with open(
        "model_config.json",
        "r",
        encoding="utf-8"
    ) as file:

        model_config = json.load(file)

    return model, tokenizer, model_config


model, tokenizer, model_config = load_resources()

MAX_SEQUENCE_LENGTH = model_config[
    "max_sequence_length"
]


# ======================================================
# Text Cleaning
# ======================================================

def clean_text(text):
    """Standardise text before tokenisation."""

    text = text.lower()
    text = text.replace("\n", " ")

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# ======================================================
# Sentiment Prediction
# ======================================================

def predict_sentiment(review_text):
    """Predict the sentiment of a new product review."""

    # Apply the same text cleaning used during training.
    cleaned_review = clean_text(
        review_text
    )

    # Convert the review into the same token representation.
    review_sequence = tokenizer.texts_to_sequences(
        [cleaned_review]
    )

    # Pad the review to the same sequence length used in training.
    padded_sequence = pad_sequences(
        review_sequence,
        maxlen=MAX_SEQUENCE_LENGTH,
        padding="post",
        truncating="post"
    )

    # Predict probability of positive sentiment.
    positive_probability = float(
        model.predict(
            padded_sequence,
            verbose=0
        )[0][0]
    )

    # Convert probability into sentiment class.
    if positive_probability >= 0.5:

        sentiment = "Positive review"
        confidence = positive_probability

    else:

        sentiment = "Negative review"
        confidence = 1 - positive_probability

    return sentiment, confidence, positive_probability


# ======================================================
# Application Interface
# ======================================================

st.title("🧠 Amazon Review Sentiment Analysis")

st.write(
    "Enter a product review below and the trained neural "
    "network will classify its sentiment as positive or negative."
)

st.divider()


# ======================================================
# Review Form
# ======================================================

with st.form("sentiment_form"):

    review_text = st.text_area(
        "Product review",
        value="",
        placeholder="Example: This product works perfectly and I would buy it again.",
        height=180,
        key="review_input"
    )

    analyse_button = st.form_submit_button(
        "Analyse Sentiment",
        use_container_width=True,
        type="primary"
    )


# ======================================================
# Display Prediction
# ======================================================

if analyse_button:

    if not review_text.strip():

        st.warning(
            "Please enter a review before analysing."
        )

    else:

        try:

            sentiment, confidence, positive_probability = (
                predict_sentiment(review_text)
            )

            st.subheader("Analysis Result")

            if sentiment == "Positive review":

                st.success(
                    f"✅ {sentiment}"
                )

            else:

                st.error(
                    f"❌ {sentiment}"
                )

            st.metric(
                "Confidence",
                f"{confidence:.2%}"
            )

            st.caption(
                f"Positive sentiment probability: "
                f"{positive_probability:.4f}"
            )

        except Exception as error:

            st.error(
                "The review could not be analysed."
            )

            st.exception(error)


# ======================================================
# Model Information
# ======================================================

st.divider()

with st.expander("About the model"):

    st.write("""
    **Task:** Amazon product review sentiment classification

    **Selected model:** Baseline Neural Network

    **Test accuracy:** 79.97%

    **Classes:** Positive and Negative

    **Maximum sequence length:** 200 tokens
    """)


with st.expander("Model limitations"):

    st.write("""
    The model may have difficulty interpreting complex
    language patterns such as:

    - Negation, for example "not bad"
    - Mixed positive and negative opinions
    - Sarcasm
    - Context-dependent language

    Predictions should therefore be interpreted as model
    estimates rather than definitive judgements.
    """)
