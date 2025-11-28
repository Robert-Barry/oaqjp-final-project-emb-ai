''' A Flask server that returns a result from the IBM Watson NLP library,
    emotion detection.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' Receieves text from an HTML interface
        and runs an emotion detector. The output
        is a statedment on the evaluation of each
        emotion, and the dominant emotion.
    '''
    # Get the query parameter textToAnalyze
    text_to_analyse = request.args.get('textToAnalyze')

    # Get a response from the emotion detector suing teh given text
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {response['anger']},"
            f" 'disgust': {response['disgust']}, 'fear': {response['fear']}," \
            f" 'joy': {response['joy']} and 'sadness': {response['sadness']}." \
            f" The dominant emotion is {response['dominant_emotion']}."
    )

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
