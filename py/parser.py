import json as json
import io as io
from pdf_downloader import PdfDownloader
from pdf import Pdf
import geocoder
from md5checker import checkmd5
from datetime import datetime
from jsonweb.encode import dumper
from address import Address

OUTPUT_FILENAME = "postni_nabiralniki.json"


def list_to_json(list):
    return json.dumps(list, default=lambda i: i.__dict__, indent=4, ensure_ascii=False)


def write_to_file(output_path, data):
    with io.open(output_path, "w", encoding="utf-8") as f:
        f.write(data)


def get_last_generated_data():
    with open(OUTPUT_FILENAME) as f:
        return json.load(f)


if __name__ == '__main__':
    pdf_file = PdfDownloader.download()
    previous_json = get_last_generated_data()

    # Exit if PDF file is the same as the last time.
    new_pdf_hash = checkmd5.make_hash(pdf_file.name)
    old_pdf_hash = previous_json["referenced_pdf_hash"]

    if new_pdf_hash == old_pdf_hash:
        print("PDF file hasn't changed since the last time. Exiting.")
        exit()

    pdf = Pdf(pdf_file.name)
    new_addresses = pdf.get_addresses()
    old_addresses = {Address(**address) for address in previous_json["addresses"]}

    # Google Geocoding calls are pretty expensive, so we don't really want to query every address every time.
    addresses_to_be_removed = old_addresses - new_addresses
    addresses_to_be_added = new_addresses - old_addresses

    new_addresses = old_addresses - addresses_to_be_removed
    json_data = {"generation_time": str(datetime.now()), "referenced_pdf_hash": new_pdf_hash}
    for address in addresses_to_be_added:
        address_latlng = geocoder.google(address).latlng
        if address_latlng is None:
            print(address)
            continue
        address.lat = address_latlng[0]
        address.lng = address_latlng[1]

        new_addresses.add(address)
    json_data["addresses"] = list(new_addresses)

    write_to_file(OUTPUT_FILENAME, dumper(json_data))
    print("Removed: ", len(addresses_to_be_removed),
          "Added: ", len(addresses_to_be_added),
          "Number of addresses: ", len(new_addresses))