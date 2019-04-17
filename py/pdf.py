import pandas as pd
import tabula as tb
from address import Address
import tempfile


class Pdf:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def get_addresses(self):
        df = pd.read_csv(self.to_csv())

        addresses = []
        for index, row in df.iterrows():
            if pd.notnull(row[0]) and pd.notnull(row[1]) and pd.notnull(row[2]) \
                    and pd.notnull(row[3]) and pd.notnull(row[5]) and pd.notnull(row[7]):
                address = Address(row[0], "Slovenia", row[1], row[3], row[5],
                                  str(row[7]) + "" if str(row[8]) == "nan" else str(row[8]))
                addresses.append(address)
        return addresses

    def to_csv(self):
        csv_file = tempfile.NamedTemporaryFile(delete=False)
        tb.convert_into(self.pdf_path, csv_file.name, "csv", pages="all")
        return csv_file.name
