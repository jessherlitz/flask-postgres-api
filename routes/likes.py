from database import get_db_connection
from flask import request, Blueprint

conn = get_db_connection()

likes = Blueprint('likes', __name__)


CREATE_LIKE = """INSERT INTO likes (
    post_id,
    likes_user_id
    ) VAlUES (%s, %s)"""


@likes.route("/likes", methods=["POST"])
def create_like():
    data = request.get_json()
    post_id = data["postId"]
    likes_user_id = data["userId"]

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(CREATE_LIKE, (post_id, likes_user_id))
        return "OK"
    except ValueError:
        return "There was an error."
