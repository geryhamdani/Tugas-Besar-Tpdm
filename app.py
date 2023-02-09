from flask import Flask, request, render_template
import numpy as np
import pickle


app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)
    return render_template("index.html", prediction_text="Hasilnya adalah ={}".format(prediction))


if __name__ == '__main__':
    app.run(debug=True)