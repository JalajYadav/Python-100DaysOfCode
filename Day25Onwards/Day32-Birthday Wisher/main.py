# -----------Monday Motivation Code-------------------#
# import smtplib
# import datetime as dt
# import random
#
# My_email = "<YourMail@gmail.com>"
# My_password = "<your password>"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 2:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#         connection.starttls()
#         connection.login(My_email, My_password)
#         connection.sendmail(
#             from_addr=My_email,
#             to_addrs="<Receiver@gmail.com>",
#             msg=f"Subject:Motivation\n\n{quote}")

# ---------------SMTPlibrary module practice----------------------#
# import smtplib
# my_email = "<YourMail@gmail.com>"
# password="<your password>"
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="<Receiver@gmail.com>",
#         msg="Subject:Hello\n\nThis is the body of the mail.")

# ---------------datetime module practice----------------------#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week=now.weekday()
