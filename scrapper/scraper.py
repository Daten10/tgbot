import httpx
from parsel import Selector


class Scrapper:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        self.page = response.text

    def get_link(self):
        html = Selector(self.page)
        link = html.css(".title a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, link))
        # full_links2 = str(full_links)
        # full_links2.split()
        return full_links[:3]


if __name__ == '__main__':
    scrap = Scrapper()
    scrap.get_page()
    scrap.get_link()
    # print(scrap.get_link())
