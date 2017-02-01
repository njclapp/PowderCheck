import smtplib
from email.MIMEText import MIMEText

msg = ('Varget is in stock!')

msg_from = ''         # who the message is 'from'
	#    msg_subject = ''           # message subject -- if i ever want to email this alert
msg_to = ['', '']    # phone to text -- figure out how to text multiple users later
msg_text = "Varget is on sale!" # alert message, will never change -- variable is needed for headers/formatting
 

headers = ['From: {}'.format(msg_from),
           'To: {}'.format(msg_to),
	   'Content-Type: text/html'
]
msg_body = '\r\n'.join(headers) + '\r\n\r\n' + msg_text

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login('', '') #'username', 'password' note: password in plaintext is very dangerous
session.sendmail(msg_from, msg_to, msg_body)
session.quit()
