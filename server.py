'''
function initiates the application of emotion
detector to be executed over the Flask
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def get_emotion_detector():
    """
    Analyze emotion analysis based on text input
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Response for empty/invalid query parameters
    if not text_to_analyze:
        return "Invalid text. Please try again!"

    # Call request
    resp = emotion_detector(text_to_analyze)

    # Extract dominant emotion
    dominant_emotion = resp.get('dominant_emotion')

    # If None. Meaning not 200
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {resp['anger']}, "
        f"'disgust': {resp['disgust']}, "
        f"'fear': {resp['fear']}, "
        f"'joy': {resp['joy']} and "
        f"'sadness': {resp['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index():
    """
    Render Index page of app
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
