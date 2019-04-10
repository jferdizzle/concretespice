import os
from flask import Flask, render_template
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@app.rount('/random')
def random():
    api_instance = giphy_client.DefaultApi()
    api_key      = os.environ.get('GIPHY_API_KEY', '')
    tag          = 'spicy'
    rating       = 'g'
    fmt          = 'json'

    try:
      api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
      pprint(api_response)
    except ApiException as e:
      print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)

if __name__ == '__main__':
    app.run(debug=False)
