from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# STEP 1: Fetch the product details
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", 
  }
#PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
html_page = requests.get(URL, headers=HEADERS).text
html_object = BeautifulSoup(html_page, "html.parser")
print(html_object.prettify())

price = html_object.find(class_="a-offscreen").getText()
price_as_float = float(price.removeprefix("$"))

BUY_PRICE = 100
product_title = html_object.find(id="productTitle").getText(strip=True)

# STEP 2: Send email if price drops
if price_as_float < BUY_PRICE:
    message = f"{product_title} is on sale for {price}!"
    try:
        with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
            connection.starttls()
            connection.login(os.environ["YOUR_EMAIL"], os.environ["YOUR_PASSWORD"])
            connection.sendmail(
                from_addr=os.environ["YOUR_EMAIL"],
                to_addrs=os.environ["YOUR_EMAIL"],
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )
        print("Email sent Successfully!")   
    except Exception as e:
        print(f"Failed to send Email: {e}")
