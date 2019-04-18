from jsonweb.encode import to_object


@to_object()
class Address:
    def __init__(self, id, country, post_code, city, street, house_number, lat=None, lng=None, *args, **kwargs):
        self.id = id
        self.country = country
        self.street = street
        self.post_code = post_code
        self.city = city
        self.house_number = house_number
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return self.country + "," + self.post_code + " " + self.city + "," + self.street + " " + self.house_number

    def __hash__(self):
        return hash((self.country, self.street, self.post_code, self.city, self.house_number))

    def __eq__(self, other):
        return self.country == other.country \
               and self.street == other.street \
               and self.post_code == other.post_code \
               and self.city == other.city \
               and self.house_number == other.house_number
