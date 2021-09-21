import os
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


script_dir = os.path.dirname(__file__)
html_file = os.path.join(script_dir, 'index.html')
# html_file = script_dir + '/index.html'

html = Template(Path(html_file).read_text())
email = EmailMessage()
email['from'] = 'Siddhant Kuntal'
email['to'] = ['siddhantkuntalalways@gmail.com','shraddha.patel79@gmail.com']
email['subject'] = 'Test SMTP!'


email.set_content(html.substitute({'name': "by Siddhant"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('siddhant.kuntal02@gmail.com', 'Ottoman_serbia1212')
    smtp.send_message(email)
    print('all good boss!')
