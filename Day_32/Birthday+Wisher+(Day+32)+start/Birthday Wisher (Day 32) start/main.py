import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:

    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )















# import smtplib
#
# my_email = "mawaddanaser0@gmail.com"
# password = "ntgw fcen ieei zzhp"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="youmnanasser732@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email"
#                         )
#

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# date_of_birth = dt.datetime(day=16, month=4, year=2000)
# print(date_of_birth)