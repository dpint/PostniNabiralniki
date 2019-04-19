from address import Address
import camelot


class Pdf:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def get_addresses(self):
        tables = camelot.read_pdf(self.pdf_path, pages="all")

        addresses = set()
        for table in tables:
            df = table.df
            for index, row in df.iloc[3:].iterrows():
                address = Address(row[0], "Slovenia", row[1], row[3], row[4],
                                  str(row[5]) + ("" if str(row[6]) == "nan" else str(row[6])))
                addresses.add(address)

        return addresses