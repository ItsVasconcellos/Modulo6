import flask, flask_cors

app = flask.Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    return print("Hello World")

@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)