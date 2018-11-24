## Execute script for looking for apartments

# Parse new information from csv file
import os
import pandas as pd
from pandas.errors import EmptyDataError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from parse_csv_files.get_new_apartments import GetNewApartments

# Initialize
GetNewApartments = GetNewApartments('findbolig.csv', 'appliedApartments.csv')

os.chdir('./get_a_place_kbh')
if os.path.exists('findbolig.csv'):
    os.remove('findbolig.csv')

process = CrawlerProcess(get_project_settings())

process.crawl('findbolig')
process.start()

# Parse data
got_data, new_apartments_empty = GetNewApartments.get_data()

if new_apartments_empty:
    pass
else:
    emails = list(['ngh1adj95@hotmail.com', 'anna.c.rodriguez@hotmail.com'])
    email_username = 'getaplace.kbh@gmail.com'
    email_password = 'Uvr23bhw'
    findbolig_username = 'DennisJensen95'
    findbolig_password = 'Uvr23bhw'

    any_new = GetNewApartments.compare_if_any_new_apartments()
    print(any_new)
    if any_new:
        GetNewApartments.apply_for_new_apartments(findbolig_username, findbolig_password, email_username, email_password, emails)
    else:
        print("There is no new apartments to apply for.")
GetNewApartments.close_driver()











