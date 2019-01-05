## Execute script for looking for apartments

# Parse new information from csv file
import os
import time
import pandas as pd
from send_a_mail.send_a_mail import SendAMail
from pandas.errors import EmptyDataError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from parse_csv_files.get_new_apartments import GetNewApartments

try:
    if '/home/dennis' in os.getcwd():
        os.chdir('./Desktop/getX/get_a_place_kbh')
    else:
        os.chdir('./get_a_place_kbh')


    if os.path.exists('findbolig.csv'):
        os.remove('findbolig.csv')

    process = get_project_settings()
    process.crawl('findbolig_test')
    process.start()

    time.sleep(5)

    # Initialize
    GetNewApartments = GetNewApartments('findbolig.csv', 'appliedApartments.csv')

    # Parse data
    got_data, new_apartments_empty = GetNewApartments.get_data()

    if new_apartments_empty:
        pass
    else:
        emails = list(['ngh1adj95@hotmail.com', 'anna.c.rodriguez@hotmail.com'])
        email_username = 'getaplace.kbh@gmail.com'
        email_password = 'Uvr23bhw'
        findbolig_username_dennis = 'DennisJensen95'
        findbolig_password_dennis = 'Uvr23bhw'
        findbolig_username_anna = 'Anna Rodriguez'
        findbolig_password_anna = 'stella1707'

        any_new = GetNewApartments.compare_if_any_new_apartments()
        print(any_new)
        if any_new:
            GetNewApartments.apply_for_new_apartments(findbolig_username_anna, findbolig_password_anna, email_username, email_password, emails)
        else:
            print("There is no new apartments to apply for.")

    GetNewApartments.close_driver()
except:
    SendAMail = SendAMail()
    SendAMail.send_email(from_addr='getaplace.kbh@gmail.com',
                         to_addr=['ngh1adj95@hotmail.com'],
                         cc_addr_list=[],
                         subject='Shit',
                         message='Shits not working, fix it.',
                         login='getaplace.kbh@gmail.com',
                         password='Uvr23bhw')
    os.chdir("./../")
    print("Shits not working, killing everything")
    os.system('./kill_sel_drivers')











