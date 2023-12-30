import smtplib as s
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import os

EMAIL= os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

obj=s.SMTP('SMTP.GMAIL.COM',587)

obj.ehlo()
obj.starttls()
obj.login(EMAIL,PASSWORD)

subject ='Python Email Project'
body= 'This is python email sending project for you. Hi from Email server'

message ='subject:{}\n\n{}'.format(subject,body)

listadd=['noumanarshad2003@gmail.com','noumanarshad159266@gmail.com']

obj.sendmail('noumanarshad@gmail.com',listadd,message)
print('Email sended')

obj.quit()