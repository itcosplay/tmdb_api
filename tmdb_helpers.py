import json
import urllib.error
import urllib.parse
import urllib.request

from environs import Env


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)

    url = '%s?%s' % (url, urllib.parse.urlencode(params))
    print(url)
    response = urllib.request.urlopen(url).read().decode('utf-8')

    return json.loads(response)


def get_user_api_key():
    env = Env()
    env.read_env()

    TMDB_TOKEN = env('TMDB_TOKEN')

    try:
        make_tmdb_api_request(method='/movie/2', api_key = TMDB_TOKEN)
        return TMDB_TOKEN

    except urllib.error.HTTPError as err:
        if err.code == 401:
            return None
            
        else:
            raise

