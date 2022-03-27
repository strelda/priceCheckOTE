### web scrapping option
# from lxml import html, etree
# import requests

# html_source = "https://www.ote-cr.cz/en/short-term-markets/electricity/intra-day-market?date=2022-03-26"
# xpath = '//*[@id="content-core"]/div/div[2]/div[2]/div/table[1]/tbody/tr[19]/td[1]'
# page = requests.get(html_source)
# tree = html.fromstring(page.content)  
# price = tree.xpath(xpath)
# print(price[0].attrib)
# print(price[0].text)


### global setting
price_warning_level = 100 #at what price the email will be sent, EUR/MWh
receiver_email = "strelecek.jan@seznam.cz" 


### load page and data
from datetime import date
import datetime


today = date.today()
# tomorrow = today + datetime.timedelta(days=1)

# htmlTomorrow="https://www.ote-cr.cz/en/short-term-markets/electricity/day-ahead-market?date="+today.strftime('%Y_%m_%d')
html = "https://www.ote-cr.cz/en/short-term-markets/electricity/intra-day-market?date="+today.strftime('%Y-%m-%d')


###send email
import ssl, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(price):

    port = 465  # For SSL
    context = ssl.create_default_context()

    smtp_server    = "smtp.seznam.cz"
    sender_email   = "oteinfo@seznam.cz"
    password_email = "warn-me-please"
    text        = """\
    <html>
        <body>
            <h4>Automatický skript zaznamenal zvýšenou cenu energií.<h4>
            <h1>Aktuální cena: """ + str('%.2f'%price) + """ Kč/kWh <h1>
            <h2><a href=""" + str(html) + """>Zdroj OTE</a> <h2>
        </body>
    </html>
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = "potenciálně vysoké ceny energií"
    message["From"] = sender_email
    message["To"] = receiver_email

    messagehtml = MIMEText(text, "html")
    message.attach(messagehtml)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
        server.login(sender_email, password_email)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )



### load from xls file
import xlrd
from forex_python.converter import CurrencyRates #for conversion from EUR to CZK

c = CurrencyRates()

filename = today.strftime('%d_%m_%Y') +"_EN.xls"
hour = datetime.datetime.now().hour

file = xlrd.open_workbook(filename)
sh = file.sheet_by_index(0)
price_now = sh.cell_value(rowx=5+hour, colx=2)

if(price_now > price_warning_level):
    sendMail(c.convert('EUR',"CZK",price_now)/1000) #converts EUR/MWh to CZK/kWh



### plot




### simple mail format, goes to spam
# import ssl, smtplib

# def sendMail(price):
#     port = 465  # For SSL
#     context = ssl.create_default_context()

#     smtp_server    = "smtp.seznam.cz"
#     sender_email   = "oteinfo@seznam.cz"
#     password_email = "warn-me-please"
#     message        = """\
#     <html>
#         <body>
#             <h1>Cena: {price} Kc <h1><br>
#             <h2><a href={html}>Zdroj OTE</a> <h2>
#         </body>
#     </html>
#     """

#     #message is not RFC 5322 complian -> např. gmail to blokuje 

#     with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
#         server.login(sender_email, password_email)
#         server.sendmail( sender_email, receiver_email, message.format(price=str(price), html=html))

