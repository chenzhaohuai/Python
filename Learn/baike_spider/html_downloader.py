import requests

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = requests.get(url)

        if response.encoding != 200:
            return None
        else:
            return response.text