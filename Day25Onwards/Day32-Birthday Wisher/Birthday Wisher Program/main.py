import datetime as dt
import pandas
import smtplib
import random

now = dt.datetime.now()
day = now.day
month = now.month
today = (day, month)

my_email = "<YourMail@gmail.com>"
my_password="<your password>"

dataFrame= pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month,row.day):row for (index,row) in dataFrame.iterrows()}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # person_name = birthday_dict[today].name
    person_name = birthday_dict[today]["name"]
    person_mail = birthday_dict[today].email
    print(person_name,person_mail)
    with open(file_path,"r") as letter_pad:
        content = letter_pad.read()
        content = content.replace("[NAME]",person_name)
        print(content)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="<Receiver@gmail.com>",
            msg=f"Subject:Happy Birthday\n\n{content}"
        )




