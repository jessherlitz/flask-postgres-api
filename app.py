from flask import Flask
from routes.users import *
from routes.posts import *
from routes.follows import *
from routes.likes import *

app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(follows)
app.register_blueprint(likes)


@app.route('/')
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
