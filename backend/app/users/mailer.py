import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Template

from ..settings import EMAIL_ADDRESS, EMAIL_PASSWORD

current_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_path, "template.html"), encoding="utf8") as file:
    html = file.read()


def send_mail(link, to_address):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_address
    msg["Subject"] = "Email Title"

    template = Template(html)
    body = template.render(link=link)

    msg.attach(MIMEText(body, "html"))

    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, to_address, text)
    server.quit()
