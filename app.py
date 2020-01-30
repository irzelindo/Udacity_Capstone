import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Question, Category

os.environ['EXCITED'] = "Excited"

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def index():
    excited = os.environ['EXCITED']
    greeting = "Hello World"

    if excited: greeting = greeting + " !!!!!"

    print(greeting)

    return greeting

  return app

app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)