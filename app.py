from flask import Flask
from routes.users import *

app = Flask(__name__)

app.register_blueprint(users)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
