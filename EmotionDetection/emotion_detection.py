'''
    Module for retrieving emotion predictions generated
    by the Watson NLP Library.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' Function to retrieve an emotion preditcion using a
        given string passed the Watson NLP library.
    '''

    # Data needed for the request
    url = 'https://sn-watson-emotion.labs.skills.network' \
          '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }

    # Access the API
    response = requests.post(url, json=obj, headers=header, timeout=8)

    # Check for a status code of 400 and return the dictionary with None if found
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    # Convert the response into a Python object
    json_format = json.loads(response.text)

    # Narrow down the object to the data needed
    emotion = json_format['emotionPredictions'][0]['emotion']

    # Convert the data into a new Python dictionary
    emotion_scores = {
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness']
    }

    # Find the dominant emotion and add it to the emotion_scores dictionary
    dominant = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant
    return emotion_scores
