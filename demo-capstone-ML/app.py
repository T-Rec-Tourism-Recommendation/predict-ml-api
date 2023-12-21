import os
from flask import Flask, render_template, request, jsonify, send_file
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

from google.cloud import storage

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')

with open('datasets/texts.json') as texts_file:
    texts = json.load(texts_file)

with open('datasets/class_info.json') as class_file:
    class_info = json.load(class_file)

VOCAB_SIZE = 10000
OOV_TOK = '<OOV>'
MAX_LENGTH = 1000
PADDING_TYPE = 'post'
TRUNC_TYPE = 'post'

tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token=OOV_TOK)
tokenizer.fit_on_texts(texts)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json(force=True)
        text = data['text']

        sequence = tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=MAX_LENGTH, padding=PADDING_TYPE, truncating=TRUNC_TYPE) 

        prediction = np.argmax(model.predict(padded_sequence, verbose=0))
        result = {'prediction': class_info[str(prediction)] }

        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid request method'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))
