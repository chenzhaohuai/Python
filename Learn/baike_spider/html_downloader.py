import requests
from IPython.display import display

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}
        response = requests.get(url=url, headers=headers, timeout=10)
        response.encoding = 'UTF-8'

        if response.status_code != 200:
            return None
        else:
            return response.text



# if __name__ == "__main__":
#     root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
#     down = HtmlDownloader()
#     display(down.download(root_url))