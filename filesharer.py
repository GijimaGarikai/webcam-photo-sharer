from filestack import Client


class FileShare:

    def __init__(self, file_name, api_key="A3rLFB5HcQP67fSPDHxR7z"):
        self.file_name = file_name
        self.api_key = api_key

    def url(self):
        client = Client(self.api_key)
        pdf_file = self.file_name
        pdf_file = client.upload(filepath=pdf_file)

        return pdf_file.url
