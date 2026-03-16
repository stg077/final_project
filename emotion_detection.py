import requests
import json
def emotion_detector(text_a_analizar):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_a_analizar } }
    response = requests.post(URL, json=myobj, headers=Headers)
    # El método .json() ya convierte la respuesta en diccionario
    formatted_response = response.json()

    print(formatted_response["emotionPredictions"][0])
    formatted_response=formatted_response["emotionPredictions"][0]
    anger_score = formatted_response['emotion']['anger']
    disgust_score = formatted_response['emotion']['disgust']   
    fear_score = formatted_response['emotion']['fear']    
    joy_score= formatted_response['emotion']['joy'] 
    sadness_score= formatted_response['emotion']['sadness'] 
    emocion_dominante = max(formatted_response['emotion'], key=formatted_response['emotion'].get)
    valor_dominante = formatted_response['emotion'][emocion_dominante]

    data={
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion':emocion_dominante
        }
    return data
