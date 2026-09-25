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
        print(formatted_res)
        return formatted_res['emotion']
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
