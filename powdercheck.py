#!/usr/bin/env python

# This program is used to check primarily for Hodgdon H110 and Hodgdon Varget gunpowder from
# http://www.powdervalleyinc.com

# Version 1.0
# Project started on 12/22/15
# First version finished 12/23/15 - No support for email or text

# Version 1.1
# Added support for text through va*********@gmail.com -- finished 12/28/15
# TODO: text to multiple people, figure out why text shows a period at the end

# Version 1.2
# Added support for multiple people(brackets around msg_to) -- finished 12/29/15
# Period at the end of texts seems to be normal

# Link for grab - http://www.powdervalleyinc.com/hodgdon.shtml

#Libraries for email/text
import smtplib
from email.MIMEText import MIMEText

#Libraries for parsing data
from bs4 import BeautifulSoup
import requests
import re


# For support, consult http://www.scottcking.com/?p=146
# The headers and msg_body section is scottcking's code
def email():
	msg_from = ''        # who the message is 'from'
	#    msg_subject = ''           # message subject -- if i ever want to email this alert
	msg_to = ['', '', '']    # phone to text/email
	msg_text = '''Varget is in stock!<br><br>Go to http://powdervalleyinc.com now to order.''' # alert message, will never change -- variable is needed for headers/formatting
 
	# If intent is SMS/text, remove/comment the header subject line
	# If intent is e-mail, add/uncomment the header subject line
 
	headers = ['From: {}'.format(msg_from),
               #'Subject: {}'.format(msg_subject),
               'To: {}'.format(msg_to),
               'MIME-Version: 1.0',
               'Content-Type: text/html']
 
	msg_body = '\r\n'.join(headers) + '\r\n\r\n' + msg_text

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login('', '') #'username','password' note: password in plaintext is very dangerous
	session.sendmail(msg_from, msg_to, msg_body)
	session.quit()


def main():
	#imports HTML and adds it to soup
	r = requests.get('http://www.powdervalleyinc.com/hodgdon.shtml')
	soup = BeautifulSoup(r.content)
	
	powder = []
	stock = []
	
	# Finds Varget, strips HTML tags
	for i in soup('td',text=re.compile('VARGET')):
		powder.append(i.text)
		stock.append(i.next_sibling.next.text)

# For a second powder...

#	for i in soup('td',text=re.compile('H110 -')):
#		powder.append(i.text)
#		stock.append(i.next_sibling.next.text)

	i=0
	count = 0
	
	# Iterates list and prints what is in stock
	while i < len(powder):
		if (stock[i] == 'Yes'):
			print powder[i] + ' >In Stock<'
			# Adds count if powder is in stock. Used for email()
			count += 1
		else:
			print powder[i] + ' >Out of Stock<'
		i+=1

	# If stock is found, email is called
	if count >= 1:
		email()

if __name__ == '__main__':
	main()
