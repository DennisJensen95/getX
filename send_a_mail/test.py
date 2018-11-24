
from send_a_mail import SendAMail

send_mail = SendAMail()

# send_mail.send_email(from_addr= 'getaplace.kbh@gmail.com',
#                      to_addr= ['anna.c.rodriguez@hotmail.com'],
#                      cc_addr_list=[],
#                      subject='Apartment',
#                      message='Vi skal have en ny lejlighed',
#                      login='getaplace.kbh@gmail.com',
#                      password='Uvr23bhw')

send_mail.send_email(from_addr= 'getaplace.kbh@gmail.com',
                     to_addr= ['ngh1adj95@hotmail.com'],
                     cc_addr_list=[],
                     subject='Ny lejlighed ledig, Yay <3',
                     message='Test message',
                     login='getaplace.kbh@gmail.com',
                     password='Uvr23bhw')
