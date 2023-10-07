from parameters import *
import smtplib

my_email = EMAIL_ID
my_password = PASSWORD


class SendMail:

    def send_the_mail(self):
        subject = "New message from the blog"
        content = f"Name: {self.name}\nE-mail: {self.email}\nPhone: {self.phone}\nMessage: {self.message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:{subject}\n\n{content}")

    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
        self.send_the_mail()
