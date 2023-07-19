from database import get_db_connection
from flask import request, Blueprint

conn = get_db_connection()

posts = Blueprint('posts', __name__)


CREATE_POST = """INSERT INTO posts (
    parent_post_id,
    post_text,
    asset,
    post_user_id
    ) VAlUES (%s, %s, %s, %s)"""


@posts.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    parent_post_id = data["parentPostId"]
    post_text = data["postText"]
    asset = data["asset"]
    post_user_id = data["userId"]

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(CREATE_POST, (parent_post_id,
                               post_text, asset, post_user_id))
        return "OK"
    except ValueError:
        return "There was an error."
