import scrapy
import csv

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/tolyatti/category/svet"]

    def open_spider(self, spider):
        self.file = open('output.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['name', 'price', 'url'])  # Пишите заголовки в CSV

    def close_spider(self, spider):
        self.file.close()

    def parse(self, response):
        svets = response.css('div.LlPhw')
        for svet in svets:
            name = svet.css('div.lsooF span::text').get()
            price = svet.css('div.q5Uds span::text').get()
            url = svet.css('a').attrib['href']
            self.writer.writerow([name, price, url])
            yield {
                'name': name,
                'price': price,
                'url': url
            }
#Прописываем открытие нового файла, задаём ему название и форматирование
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    pass