from flask import Flask, redirect, render_template, request
from transformers import pipeline
import torch

app = Flask(__name__)

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

def generate(text, max_len=50):
	return generator(text, max_length=max_len)[0]['generated_text']

response = None
@app.route('/', methods=['GET', 'POST'])
def idex():
    if request.method == 'POST':
        text = request.form['prompt']
        response = generate(text, int(request.form['maxlen']))
        return render_template('index.html', response = response)
    return render_template('index.html', response = None)

if __name__ == '__main__':
    app.run(debug=True)
