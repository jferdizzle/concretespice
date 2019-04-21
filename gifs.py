import os
from giphypop import Giphy
from random import shuffle


backup_gifs = [
    "https://media.giphy.com/media/US08vOBGfQJsQ/giphy.gif",
    "https://media.giphy.com/media/28V8SHk997ah2/giphy.gif",
    "https://media.giphy.com/media/OwSlpGFab7fq0/giphy.gif",
    "https://media.giphy.com/media/DYWl99j1LFF2o/giphy.gif",
    "https://media.giphy.com/media/A4mX199uSixI4/giphy.gif",
    "https://media.giphy.com/media/3o7bu61TjB7YQll4yc/giphy.gif",
    "https://media.giphy.com/media/26u4oPZwxsfSjet7q/giphy.gif",
    "https://media.giphy.com/media/26Ff4YURfhIP1huog/giphy.gif",
    "https://media.giphy.com/media/13cMYrbpeJsX8Q/giphy.gif",
    "https://media.giphy.com/media/MVnnLh5WhGBhe/giphy.gif",
    "https://media.giphy.com/media/12XGECQYa80YAo/giphy.gif",
    "https://media.giphy.com/media/XEg7SK9fiXAhiKBYZt/giphy.gif",
    "https://media.giphy.com/media/n9fUozyTUAKIw/giphy.gif",
    "https://media.giphy.com/media/L7F3PakLagm9W/giphy.gif",
    "https://media.giphy.com/media/CAlBTS57uDXoY/giphy.gif",
    "https://media.giphy.com/media/HZpCCbcWc0a3u/giphy.gif",
    "https://media.giphy.com/media/Fa2vR8hle8s9y/giphy.gif",
]

backup_keys = ['spicy', 'explosions', 'hot food', 'simmer spice']

def get_search_keys():
    try:
        keys = os.environ['GIPHY_TERMS'].split(',')
    except:
        return backup_keys
    return keys

def get_giphy_results():
    results = []
    if os.environ.get('FEATURE_FLAG_GIF_RANDOMIZER', 'true') == 'true':
        return backup_gifs
    try:
        giphy = Giphy()
        for key in get_search_keys():
            results.extend([x.media_url for x in giphy.search(key)])
    except:
        results = backup_gifs
    shuffle(results)
    return results
