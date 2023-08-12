from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from services.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/load_germanword": {"origins": "*"}})  # Allow all origins

services = Services()


@app.route('/')
def home():
    with open("web/german.html", "r") as f:
        return f.read()

"""
@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()
"""

@app.route('/get_word', methods=["POST"])
@cross_origin()  # Allow CORS for this route
def get_word():
    data = request.get_json()
    app.logger.info(f"/get_word - Got request: {data}")
    word_info = services.get_word_details(data.get('word'))
    app.logger.info(f"/get_word - Output: {word_info}")
    return jsonify(word_info)

@app.route('/get_translation', methods=["POST"])
@cross_origin()  # Allow CORS for this route
def get_translation():
    data = request.get_json()
    app.logger.info(f"/get_translation - Got request: {data}")
    word_info = services.get_from_english(data.get('word'))
    app.logger.info(f"/get_translation - Output: {word_info}")
    return jsonify(word_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
