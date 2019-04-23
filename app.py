import os
from flask import Flask, render_template, g
from gifs import get_giphy_results
from helpers import divide_chunks


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    gifs = get_giphy_results()
    gifs = divide_chunks(gifs, int(len(gifs)/4))
    return render_template(
        'index.html',
        gif_set_0=gifs[0],
        gif_set_1=gifs[1],
        gif_set_2=gifs[2],
        gif_set_3=gifs[3],
        nav_link="https://media.giphy.com/media/xUOwG3nVH6Of928xJm/giphy.gif",
        nav_path="./map",
    )

@app.errorhandler(404)
def page_not_found(page_name):
    return index()

@app.route('/map', strict_slashes=False)
def map():
    return render_template(
        'map.html',
        nav_link="https://media.giphy.com/media/TFedSWdWdQnoOJ3YWL/giphy.gif",
        nav_path="./",
    )

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', False))
