from flask import request, Blueprint
import boto3
import json

channels = Blueprint('channels', __name__)


@channels.route("/channel", methods=["POST"])
def create_channel():
    data = request.get_json()
    user_id = data['userId']

    client = boto3.client('ivs')
    response = client.create_channel(
        authorized=False,
        latencyMode='LOW',
        name='testing',
        type='BASIC'
    )

    print(data, user_id)
    print(json.dumps(response, indent=1))
