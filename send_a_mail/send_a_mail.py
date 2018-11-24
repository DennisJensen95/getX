# This script will send a mail

import smtplib

class SendAMail():

    def send_email(self, login, password, message, to_addr, subject="There is a new apartment we applied for <3", cc_addr_list='' ,from_addr='getaplace.kbh@gmail.com'):
        header = 'From: {0}'.format(from_addr)
        header += '\nTo: {0}'.format(to_addr)
        header += '\nCc: {0}'.format(' ,'.join(cc_addr_list))
        header += '\nSubject: {0}\n'.format(subject)

        message = header + message

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)
        problems = server.sendmail(from_addr, to_addr, message)
        server.quit()
