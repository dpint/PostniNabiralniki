# CLI Usage:
# python3 parser.py <current PDF filepath> <old generated JSON filepath> <new generated JSON filepath>

import json as json
import io as io
from pdf import Pdf
import geocoder
from datetime import datetime
from jsonweb.encode import dumper
from address import Address
import sys


def write_to_file(output_path, data):
    with io.open(output_path, "w", encoding="utf-8") as f:
        f.write(data)


def get_json_from_file(file_path):
    with open(file_path) as f:
        return json.load(f)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.stderr.write('Argument count is invalid!\n')
        exit(1)

    current_pdf_file_path = sys.argv[1]
    old_generated_JSON_file_path = sys.argv[2]
    new_generated_JSON_file_path = sys.argv[3]

    new_pdf = Pdf(current_pdf_file_path)
    old_json = get_json_from_file(old_generated_JSON_file_path)

    # Exit if PDF file is the same as the last time.
    new_pdf_hash = new_pdf.get_pdf_hash()
    old_pdf_hash = old_json["referenced_pdf_hash"]

    if new_pdf_hash == old_pdf_hash:
        print("PDF file hasn't changed since the last time. Exiting.")
        exit()

    new_addresses = new_pdf.get_addresses()
    old_addresses = {Address(**address) for address in old_json["addresses"]}

    # Google Geocoding calls are pretty expensive, so we don't really want to query every address every time.
    addresses_to_be_removed = old_addresses - new_addresses
    addresses_to_be_added = new_addresses - old_addresses

    new_addresses = old_addresses - addresses_to_be_removed
    json_data = {"generation_time": str(datetime.now()), "referenced_pdf_hash": new_pdf_hash}
    for address in addresses_to_be_added:
        address_latlng = geocoder.google(address).latlng
        if address_latlng is not None:
            sys.stderr.write("Geocoder returned empty result for address: " + str(address) + "\n")
            continue
        address.lat = address_latlng[0]
        address.lng = address_latlng[1]

        new_addresses.add(address)
    json_data["addresses"] = list(new_addresses)

    write_to_file(new_generated_JSON_file_path, dumper(json_data))
    print("Removed: ", len(addresses_to_be_removed),
          "Added: ", len(addresses_to_be_added),
          "Number of addresses: ", len(new_addresses))