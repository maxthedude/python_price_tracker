import requests
from bs4 import BeautifulSoup
import smtplib
import re

URL = "https://www.amazon.de/TurnRaise-Ladeger%C3%A4t-Aluminium-Voltmeter-Knopfleiste/dp/B01N6C2GCP?pf_rd_p=1d845bea-8a37-4701-8792-ce8d67e64a10&pd_rd_wg=x49ab&pf_rd_r=H42G4WE32KNY7G17ZP67&ref_=pd_gw_cr_simh&pd_rd_w=ari0P&pd_rd_r=42151dc9-7b51-407f-b0a3-9ee3d527092e"

#Customize the User-Agent for your client
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

def extract_nbr(input_str):
    if input_str is None or input_str == '':
        return 0

    out_number = ''
   # for ele in input_str:
    #    if ele.isdigit():
    #        out_number += ele
    out_number = re.findall(r"[-+]?\d*\.\d+|\d+", input_str)
    print(out_number)
    return float(out_number[0])    

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    convertedPrice = extract_nbr(price);

   # if(convertedPrice < 10):
    #    send_mail()

    print(price)
    print(convertedPrice)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 500)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('','')

    subject = 'Niedriger Preis jetzt'
    body = 'Check the Link: '

    message = {"Subject: {subject}\n\n{body}"}

    server.sendmail('from','to',message)

    print('EMail send')
    server.quit()



check_price()
