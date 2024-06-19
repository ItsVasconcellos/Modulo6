import flask, flask_cors
# Testar o modelo
import cv2
import numpy as np
# Carrega o modelo
from tensorflow.keras.models import load_model
modelo = load_model('modelo_mnist.h5')


app = flask.Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    return print("Hello World")

@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000)