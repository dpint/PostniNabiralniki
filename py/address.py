
class Address:
    def __init__(self, id, country, post_code, city, street, house_number):
        self.id = id
        self.country = country
        self.street = street
        self.post_code = post_code
        self.city = city
        self.house_number = house_number

        self.fix_data()

    # Ugly hack, but MapBox Geocoder can't geocode address otherwise...
    def fix_data(self):
        self.city = self.city.replace("/Lendva", "")

    def __str__(self):
        return self.country + "," + self.post_code + " " + self.city + "," + self.street + " " + self.house_number
