from flask import Flask
from flask_cors import CORS
from flask import jsonify


import bot

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Welcome to the chatBot admin panel!"


@app.route('/answer/<question>', methods=['GET'])
def hello_name(question):
    answer = bot.chat_tfidf(question)
    return jsonify(
        question=question,
        answer=answer.replace('- ', '')
    )


if __name__ == '__main__':
    app.run()
