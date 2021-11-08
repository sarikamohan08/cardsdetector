from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin



from com_ai_utils.utils import decodeImage
from research.obj import CardsDetector

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        modelPath = 'research/my_cards_model'
        self.objectDetection = CardsDetector(self.filename, modelPath)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.objectDetection.getPrediction()
    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    port = 9000
    app.run(host='127.0.0.1', port=port)
    #app.run(host='0.0.0.0', port=7000, debug=True)
