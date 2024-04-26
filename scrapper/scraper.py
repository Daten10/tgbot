import asyncio
import httpx
from parsel import Selector


class Scrapper:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        print('PAGE: ', url)
        return response.text

    def get_link(self, page: str):
        html = Selector(page)
        link = html.css(".title a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, link))
        return full_links

    async def get_links(self):
        tasks = []
        async with httpx.AsyncClient() as client:
            for i in range(1, 11):
                url = f'{self.MAIN_URL}?page={i}'
                task = asyncio.create_task(self.get_page(url, client))
                tasks.append(task)

            results = await asyncio.gather(*tasks)
            all_links = []
            for result in results:
                links = self.get_link(result)
                all_links.extend(links)

        for i, link in enumerate(all_links, start=1):
            print(f"{i}. {link}")

        return all_links[:3]


if __name__ == '__main__':
    scrap = Scrapper()
    asyncio.run(scrap.get_links())
    # print(scrap.get_link())
