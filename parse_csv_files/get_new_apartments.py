# This class is for parsing the csv files and returning new apartments to apply for

import time
import pandas as pd
from apply_findbolig.findbolig_apply import FindBoligApply
from send_a_mail.send_a_mail import SendAMail

class GetNewApartments():

    def __init__(self, new_data, appliedApartments):
        self.filename_new_data = new_data
        self.filename_applied_data = appliedApartments
        self.new_data = None
        self.applied_data = None
        self.new_apartments = []
        self.new_apartments_data = pd.DataFrame()
        self.email = SendAMail()

        self.apply = None

    def get_data(self):
        got_data = False
        empty_data = False
        try:
            self.new_data = pd.read_csv(self.filename_new_data)
            self.applied_data = pd.read_csv(self.filename_applied_data)
            got_data = True
            if self.new_data.empty:
                empty_data = True
            # print(self.new_data)
            # print(self.applied_data)
        except:
            print("One of the files were corrupted or empty.")

        return got_data, empty_data

    def compare_if_any_new_apartments(self):
        """
        Comparing all the new data to old applied data, and if any new you can apply them
        :return:
        """
        new_apartments = True
        # Check if any new apartments
        self.new_apartments = set(self.new_data['link']) - set(self.applied_data['link'])

        # Index the application list in the new_data and extract only new apartments
        for new_apartment in self.new_apartments:
            new_apartment = self.new_data.loc[self.new_data['link'] == new_apartment]
            new_apartment = new_apartment.loc(axis=1)['adress', 'area', 'rent', 'aconto', 'link', 'time']
            self.new_apartments_data = self.new_apartments_data.append(new_apartment, ignore_index=True)

        # print(self.new_apartments_data)
        if self.new_apartments_data.empty:
            print("No new apartments")
            new_apartments = False

        return new_apartments




    def apply_for_new_apartments(self, username, password, email_username, email_password, emails):
        """
        The profile used to login to and applying with, and the emails to send mails too
        """
        # Start a webdriver when initiating
        self.apply = FindBoligApply()
        # login_success = True
        login_success = self.apply.login_findbolig(username, password)
        if login_success and not self.new_apartments_data.empty:
            for index, row in self.new_apartments_data.iterrows():
                self.apply.click_apply(row['link'])
                time.sleep(5)
                message = "A new apartment has been applied. Rent is {0} surplus rent is {1} \n" \
                       "The adress is {2} ond here is the link for it {3}".format(str(row['rent']), str(row['aconto']),
                                                                           str(row['adress']), str(row['link']))
                if len(emails) == 1:
                    try:
                        self.email.send_email(email_username, email_password, message, emails)
                        print('Sent email to: {0}'.format(emails))
                    except:
                        message = "The email could not be send properly, check that the agent has applied."
                        self.email.send_email(email_username, email_password, message, emails)
                        print(message)
                else:
                    for email in emails:
                        try:
                            self.email.send_email(email_username, email_password, message, str(email))
                            print('Sent email to: {0}'.format(email))
                        except:
                            message = "The email could not be send properly, check that the agent has applied."
                            self.email.send_email(email_username, email_password, message, emails)
                            print(message)



            with open(self.filename_applied_data, 'a') as f:
                self.new_apartments_data.to_csv(f, header=False)

    def close_driver(self):
        if self.apply != None:
            self.apply.close








