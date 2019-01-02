"""
Scraping AAB apartments

Created 2/1/2019

@Author Dennis Jensen

"""

import scrapy
from send_a_mail.send_a_mail import SendAMail

class AABBoliger(scrapy.Spider):
    """
    This spider crawls AABBoliger and sends a mail for Anna and I to apply for it.
    """

    name = "ABBBoliger"
    allowed_domains = ['http://www.aab.dk']

    # The actual url to scrape
    start_urls = ['http://www.aab.dk/da/MainMenu/Boligsoegende/Saadan-soeger-du-bolig/Ledige-boliger-lige-nu']

    def parse(self, response):

        # Wrapping all the content i want to scrape
        content = " ".join(response.xpath('//div[@class="content_TextBlock"][2]//text()').extract())
        link = 'http://www.aab.dk/da/MainMenu/Boligsoegende/Saadan-soeger-du-bolig/Ledige-boliger-lige-nu'
        message = '\nThere is an available apartment in AAB site. Here is the link for the website: {0}. ' \
                  'There is no waiting que, so be quick <3 <3'.format(link)
        not_avai = "Vi har i øjeblikket ingen ledige boliger til leje uden opnotering på ventelisten."


        if not_avai in content:
            pass
        else:
            print("There is an apartment")
            SendAMail().send_email(from_addr='getaplace.kbh@gmail.com',
                                 to_addr=['ngh1adj95@hotmail.com', 'anna.c.rodriguez@hotmail.com'],
                                 cc_addr_list=[],
                                 subject='Available apartment from AAB!',
                                 message=message,
                                 login='getaplace.kbh@gmail.com',
                                 password='Uvr23bhw')