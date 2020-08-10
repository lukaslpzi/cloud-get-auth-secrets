import discogs_client
from discogs_client.exceptions import HTTPError
import json

# http://localhost:8080?token={}&secret={}&oauth_code=

def main(request):

    """
    TODO:
    - store consumer_key and consumer_secret in secret thingy.
    - find somme funky user_agent name and store it globaly.

    """

    if not request.args or not 'oauth_code' in request.args or not 'token' in request.args or not 'secret' in request.args:
        return 'bad query params'

    oauth_verifier = request.args['oauth_code']
    token = request.args['token']
    secret = request.args['secret']

    user_agent = 'discogs_api_example/2.0'
    consumer_key = 'DpToaTUkOnKnZaimGtWa'
    consumer_secret = 'cITslCuphJWwiqSQnIgQvKwHXQILTTuq'
    discogsclient = discogs_client.Client(user_agent, consumer_key=consumer_key, consumer_secret=consumer_secret, token=token, secret=secret)


    access_token, access_secret = discogsclient.get_access_token(oauth_verifier)

    user = discogsclient.identity()

    return json.dumps({'access_token': access_token, 'access_secret': access_secret}), 200, {'ContentType': 'application/json'}