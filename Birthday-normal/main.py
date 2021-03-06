# #################### Normal Starting Project ######################
import random
import smtplib
from datetime import datetime

import pandas

today = datetime.now()
today_tuple = (today.month, today.day)
name = "[NAME]"
my_email = "your_email"
password = "your_password"

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(name, birthday_person["name"])

        #if you use gmail.com (smtp.gmail.com)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )

    print(birthday_person["email"])
