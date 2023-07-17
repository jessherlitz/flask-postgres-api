from flask import Flask, request
from database import get_db_connection

app = Flask(__name__)

conn = get_db_connection()


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


CREATE_USER = "INSERT INTO users \
            (first_name, \
            last_name, \
            email, \
            password, \
            profile_img, \
            state, \
            city, \
            country, \
            username) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    first_name = data["firstName"]
    last_name = data["lastName"]
    email = data["email"]
    password = data["password"]
    profile_img = data["profileImg"]
    state = data["state"]
    city = data["city"]
    country = data["country"]
    username = data["username"]

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(CREATE_USER, (first_name, last_name, email,
                                             password, profile_img, state, city, country, username))
        return "OK"
    except ValueError:
        return "There was an error."


if __name__ == "__main__":
    app.run()
