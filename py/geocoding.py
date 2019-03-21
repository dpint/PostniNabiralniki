import requests
import json
import time

url_prefix = "https://nominatim.openstreetmap.org/search?q="
res_format = "format=json"


def api_call(obj):
    url = url_prefix + obj.hisna_st + obj.dodatek + "+" + obj.ulica + ",+" + obj.naselje + "&" + res_format
    response = requests.get(url)
    return response.content


def get_latlon(obj):
    content = api_call(obj)
    loaded = json.loads(content)

    obj.lat = loaded[0]["lat"]
    obj.long = loaded[0]["lon"]


def add_latlon(objects):
    for o in objects:
        get_latlon(o)
        time.sleep(1)
    return objects
