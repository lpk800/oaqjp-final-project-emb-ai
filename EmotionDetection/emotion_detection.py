import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_pyload_2llm = { "raw_document": { "text": text_to_analyze } }


    # Send POST request to Watson NLP API
    res = requests.post(url, json=input_pyload_2llm, headers=header, timeout=30)

    if res.status_code == 200:
        # Parse JSON response
        formatted_res = json.loads(res.text)
        emotions = formatted_res['emotionPredictions'][0]['emotion']
        
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        #print(f"dominat emotion {dominant_emotion}")

        emotion_scores['dominant_emotion'] = dominant_emotion
        #print(emotion_scores)
        return emotion_scores 
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
