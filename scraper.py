import requests
from bs4 import BeautifulSoup
import smtplib
import time

from re import sub
from decimal import Decimal

URL="https://www.amazon.in/dp/B07HHHMWQG/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=TG9F4HHR42RAC0AB6JVM&pf_rd_t=101&pf_rd_p=428cd22f-b362-46d4-aa3b-7b2c8ea18e0c&pf_rd_i=21405369031"

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup =BeautifulSoup(page.content,'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = Decimal(sub(r'[^\d.]', '', price))
	 

	if(converted_price < 1.700):
		send_mail()

	print(converted_price)
	print(title.strip())


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('ananthuajay5@gmail.com','unnzztycenvwcrev')

	subject = 'Price fell down'
	body ='Check the amazon link https://www.amazon.in/dp/B07HHHMWQG/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=TG9F4HHR42RAC0AB6JVM&pf_rd_t=101&pf_rd_p=428cd22f-b362-46d4-aa3b-7b2c8ea18e0c&pf_rd_i=21405369031'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'ananthuajay5@gmail.com',
		msg
	)
	print('HEY EMAIL IS SENT!!')

	server.quit()


while(True):
	check_price()
	time.sleep(60*60)