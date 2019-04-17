import json as json
import io as io
from geocoder import Geocoder
from pdf_downloader import PdfDownloader
from pdf import Pdf

OUTPUT_FILENAME = "postni_nabiralniki.json"


def list_to_json(list):
    return json.dumps(list, default=lambda i: i.__dict__, indent=4, ensure_ascii=False)


def write_to_file(output_path, data):
    with io.open(output_path, "w", encoding="utf-8") as f:
        f.write(unicode(data, "utf-8"))


if __name__ == '__main__':
    pdf_file = PdfDownloader.download()
    pdf = Pdf(pdf_file.name)
    addresses = pdf.get_addresses()
    addresses_with_latlon = [[address, Geocoder(address).get_latlon()] for address in addresses]
    json = list_to_json(addresses_with_latlon)
    write_to_file(OUTPUT_FILENAME, json)