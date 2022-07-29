import csv
import re
import yagmail
from email.mime.text import MIMEText

# Obtain details from user
msg = MIMEText(input('Please enter your message: '))
msg['Subject'] = input('Please enter your subject: ')
sender = input('Please enter your email address: ')
msg['From'] = sender
password = input('Please enter your password: ')

# Start connection to server
server = yagmail.SMTP(sender, password)

# Obtain the CSV file location
email_data = csv.reader(open(input("Please enter the location of the CSV file: "), 'r'))

# Send emails
email_pattern = re.compile("^.+@.+\..+$")
for row in email_data:
    if email_pattern.search(row[0]):
        del msg['To']
        msg['To'] = row[0]
        print (row[0] + '\t Valid Address')
        try:
            server.send([row[0]], msg['Subject'], msg.as_string())
        except yagmail.YagAddressError:
            print("An error occurred.")
    else:
        print(row[0] + '\t Invalid Address')
