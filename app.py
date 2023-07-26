import streamlit as st
from flair.models import TextClassifier
from flair.data import Sentence

# Load the French sentiment classifier from Flair
classifier = TextClassifier.load('sentiment-fast')

# Main function
def main():
    # Title of the application
    st.title("Sentiment Analysis")

    # Language selection dropdown
    language = st.selectbox("Choose the language", ("English", "French"))

    if language == "English":
        examples = [
            "I love this movie! It's fantastic.",
            "Today is a beautiful day.",
            "I feel so happy right now.",
            "I'm really sad about the news.",
        ]
    else:
        examples = [
            "J'adore ce film ! Il est fantastique.",
            "Aujourd'hui est une belle journée.",
            "Je me sens tellement heureux en ce moment.",
            "Je suis vraiment triste des nouvelles.",
        ]

    st.subheader(f"Examples of Texts ({language})")
    for example in examples:
        st.write(f"- {example}")

    # User input textarea
    user_input = st.text_area(f"Enter your text here in {language}", "")

    # Analyze button
    if st.button("Analyze"):
        if user_input.strip():
            # Perform sentiment analysis using Flair
            sentence = Sentence(user_input)
            classifier.predict(sentence)

            # Display sentiment score and result
            st.subheader(f"Sentiment Analysis Results ({language})")
            st.write(f"The sentiment in the text is {sentence.labels[0].value}.")
            st.write(f"Sentiment score: {sentence.labels[0].score:.4f}")

            # Display sentiment scores for each class (positive, negative, neutral)
            st.subheader("Sentiment Score Details:")
            for label in sentence.labels:
                st.write(f"{label.value.capitalize()} Score: {label.score:.4f}")

            # Interpret sentiment score
            sentiment_result = interpret_sentiment_score(sentence.labels[0].value)
            st.write(f"Interpretation: The sentiment in the text is {sentiment_result}.")
        else:
            st.warning(f"Please enter some text for sentiment analysis in {language}.")

# Function to interpret the sentiment score
def interpret_sentiment_score(sentiment_label):
    if sentiment_label == 'POSITIVE':
        return "positive"
    elif sentiment_label == 'NEGATIVE':
        return "negative"
    else:
        return "neutral"

# Run the main function
if __name__ == "__main__":
    main()
