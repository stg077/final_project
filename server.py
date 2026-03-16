from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app=Flask("Detector de emociones")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    data=emotion_detector(text_to_analyze)
    if data is None:
        data={
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness':None,
        'dominant_emotion':None
        }
        return {'message':data,'status_code':400}
        
    return {'message':data,'status_code':200}

@app.route("/")
def pagina_principal():
    return render_template("index.html")

# @app.ExecpcionHandler(e)
# def error_handler():
#     return {'message':"ERROR!!!"}  

if name == "main":
    app.run(host="0.0.0.0", port=5000)=