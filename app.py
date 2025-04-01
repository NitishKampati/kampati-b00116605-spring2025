import os
from flask import Flask 

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    app.run(debug=True)