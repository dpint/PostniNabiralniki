from requests import get
import tempfile


class PdfDownloader:

    DOWNLOAD_URL = "https://www.posta.si/zasebno-site/Documents/Seznami/Seznam%20po%C5%A1tnih%20nabiralnikov.pdf"

    @staticmethod
    def download():
        r = get(PdfDownloader.DOWNLOAD_URL)
        pdf_file = tempfile.NamedTemporaryFile(delete=False)
        pdf_file.write(r.content)
        return pdf_file
