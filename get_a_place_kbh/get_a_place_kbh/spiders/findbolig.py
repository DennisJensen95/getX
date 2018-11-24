## Scraper for findbolig

import scrapy
import datetime


class findbolig(scrapy.Spider):
    name = 'findbolig'
    allowed_domains = ['www.findbolig.nu']
    # The actual url
    start_urls = ['https://www.findbolig.nu/ledigeboliger/liste.aspx?where=K%C3%B8benhavn%20K%2C%20K%C3%B8benhavn%20N%202200%2C%20K%C3%B8benhavn%20%C3%98%2C%20K%C3%B8benhavn%20NV%202400%2C%20Frederiksberg%2C%20&rentmax=10000&roomsmin=2&showrented=1&showyouth=1&showlimitedperiod=1&showunlimitedperiod=1&showOpenDay=0&focus=ctl00_placeholdersidebar_0_txt_RoomsMin']
    # Test url københavn Ø, N, NV, K, Frederiksberg uden søge kriterier
    # start_urls = ['https://www.findbolig.nu/ledigeboliger/liste.aspx?where=Frederiksberg%2C%20K%C3%B8benhavn%20K%2C%20K%C3%B8benhavn%20N%202200%2C%20K%C3%B8benhavn%20NV%202400%2C%20K%C3%B8benhavn%20%C3%98%202100%2C%20&roomsmin=2&showrented=1&showyouth=1&showlimitedperiod=1&showunlimitedperiod=1&showOpenDay=0&pagesize=100']

    def parse(self, response):

        # Wrapping all the content i want to scrape
        ads = response.xpath('//table[@class="gridTable"]//tr[position() > 1]')
        i = 0
        for ad in ads:
            response.meta['adress'] = ad.xpath('.//a[@class="advertLink"]/b/text()').extract_first()
            response.meta['area'] = ad.xpath('.//a[@class="advertLink"]/text()').extract_first()
            response.meta['rent'] = ad.xpath('.//td[contains(text(), "kr")]/text()').extract()[0]
            response.meta['aconto'] = ad.xpath('.//td[contains(text(), "kr")]/text()').extract()[1]
            response.meta['link'] = response.urljoin(ad.xpath('.//td[@class="imgCol"]/a[@class="advertLink"]/@href').extract_first())
            response.meta['time'] = datetime.datetime.now().strftime("%d-%m-%y")
            print("Num: {0}".format(i))
            i += 1

            yield response.meta