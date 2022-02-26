# Import smtplib for the actual sending function
from email.message import EmailMessage
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

msg = EmailMessage()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'test'
msg['From'] = 'thisistaha@gmail.com'
msg['To'] = 'thisistaha@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail('thisistaha@gmail.com', ['thisistaha@gmail.com'], msg.as_string())
s.quit()