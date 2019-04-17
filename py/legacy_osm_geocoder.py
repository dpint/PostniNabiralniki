import requests
import json
import time
from urllib import parse


class Geocoder:
    URL_PREFIX = "https://nominatim.openstreetmap.org/search?"
    RESPONSE_FORMAT = "json"

    def __init__(self, address):
        self.address = address

    def get_latlon(self):
        # Usage policies dictate 1 request per second at maximum
        time.sleep(1)

        content = self._call_api()
        parsed_json = json.loads(content)

        print(self._get_url())
        print(content)

        lat = parsed_json[0]["lat"]
        lon = parsed_json[0]["lon"]

        return lat, lon

    def _call_api(self):
        return requests.get(self._get_url()).content

    def _get_url(self):
        return Geocoder.URL_PREFIX + parse.urlencode({'q': self.address.country + "," + self.address.post_code + " "
                                                           + self.address.city + "," +self.address.house_number + " "
                                                           + street,
                                                      'format': Geocoder.RESPONSE_FORMAT
                                                      })
