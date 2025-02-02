from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#--------------STEP 1------------------------------------------
PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"

html_page = requests.get(PRACTICE_URL).text
html_object = BeautifulSoup(html_page, "html.parser")

price = html_object.find(class_="a-offscreen").getText()
price_as_float = float(price.removeprefix("$"))
#print(price_as_float)

#--------------STEP 2------------------------------------------
BUY_PRICE = 100
product_title = html_object.find(id="productTitle").getText(strip=True)
#print(product_title)
YOUR_EMIAL = "mawaddanaser0@gmail.com"
YOUR_PASSWORD = "mawada123123"
subject = "Amazon Price Alert!"
body = f"{product_title} \n {price} \n {PRACTICE_URL}"
print(body)

message = MIMEMultipart()
message["from"] = YOUR_EMIAL
message["to"] = YOUR_EMIAL
message["subject"] = subject

message.attach(MIMEText(body, "plain"))

if price_as_float < BUY_PRICE:
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(YOUR_EMIAL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMIAL, YOUR_EMIAL, message.as_string())
        print("Emial send Successfully!")   
    except Exception as e:
        print(f"Failed to send Email: {e}")