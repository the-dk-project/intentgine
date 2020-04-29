import email, getpass, imaplib, os

user = 'donn.victory@intentgine.com'
pwd = 'intent2020'

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)