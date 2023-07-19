from database import get_db_connection
from flask import request, Blueprint

conn = get_db_connection()

users = Blueprint('users', __name__)


CREATE_USER = """INSERT INTO users
            (first_name,
            last_name,
            email,
            password,
            profile_img,
            state,
            city,
            country,
            username)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""


@users.route("/users", methods=["POST"])
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
