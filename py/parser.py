import json as json
import io as io
from pdf_downloader import PdfDownloader
from pdf import Pdf
import geocoder
from md5checker import checkmd5

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

    new_pdf_hash = checkmd5.make_hash(pdf_file.name)
    old_pdf_hash = previous_json["referenced_pdf_hash"]

    if new_pdf_hash == old_pdf_hash:
        print("PDF file hasn't changed since the last time. Exiting.")
        exit()

    pdf = Pdf(pdf_file.name)
    addresses = pdf.get_addresses()
    addresses_with_latlon = [[address, geocoder.google(address).latlng] for address in addresses]
    json = list_to_json(addresses_with_latlon)
    write_to_file(OUTPUT_FILENAME, json)
