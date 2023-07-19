from database import get_db_connection
from flask import request, Blueprint

conn = get_db_connection()

follows = Blueprint('follows', __name__)


FOLLOW = """INSERT INTO follows (
    followee_user_id,
    follower_user_id
    ) VAlUES (%s, %s)"""


@follows.route("/follows", methods=["POST"])
def create_follow():
    data = request.get_json()
    followee_user_id = data["followeeId"]
    follower_user_id = data["followerId"]

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(FOLLOW, (followee_user_id, follower_user_id))
        return "OK"
    except ValueError:
        return "There was an error."
