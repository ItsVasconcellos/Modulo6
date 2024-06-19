from flask import Flask, request, render_template, session, redirect, url_for
import numpy as np
import tensorflow as tf  # Import TensorFlow for model loading
import cv2  # Example using OpenCV
from keras.layers import Flatten


# Load your trained MNIST model (replace with your path)
model = tf.keras.models.load_model('models/modelo_mnist.h5')

# Load your trained linear model (replace with your path)
linear_model = tf.keras.models.load_model('models/modelo_mnist_linear.h5')

app = Flask(__name__)

@app.route('/')
def index():
    prediction = session.get('prediction', None)  # Get prediction from session
    return render_template('index.html', prediction=prediction)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return ({'error': 'No image uploaded'}), 400

    image_file = request.files['image']

    image_data = image_file.read()

    image = cv2.imdecode(np.fromstring(image_data, np.uint8), cv2.IMREAD_GRAYSCALE)

    image = cv2.resize(image, (28, 28))  
    image = image.astype('float32') / 255.0

    image = image.reshape(1, 28, 28, 1)  
    
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction[0])

    return render_template('index.html', prediction=predicted_class, prediction_linear=None)

@app.route('/predict-linear', methods=['POST'])
def previewLinear():
    if 'image' not in request.files:
        return {'error': 'No image uploaded'}, 400

    image_file = request.files['image']

    image_data = image_file.read()
    image_array = np.frombuffer(image_data, np.uint8)  # Decode byte stream to NumPy array
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))
    image = image / 255.0
    image = image.flatten()
    image = np.expand_dims(image, axis=0)
    prediction = linear_model.predict(image)
    predicted_class = np.argmax(prediction[0])

    return render_template('index.html', prediction=None, prediction_linear=predicted_class)


if __name__ == '__main__':
    app.run(debug=True)
