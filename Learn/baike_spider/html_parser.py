from bs4 import BeautifulSoup

class HtmlParser(object):
    
    def _get_new_urls(self, page_url, soup):
        
        links = soup.find_all('a', href=re.compiler(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = 

    def _get_new_datas(self, page_url, soup):
        pass



    def paser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
        
        soup = BeautifulSoup( markup = html_cont, parse_only =' html.paser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
