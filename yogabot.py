import requests
from bs4 import BeautifulSoup
from settings import email, password

import time

def book_yoga_class():

    #start the session

    s = requests.Session()


    #log in

    login_data = {'email_address':email, 'password': password, 'log_in': 'Log+In'}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    r1 = s.post("https://myflye.flyefit.ie/login", data=login_data, headers=headers)
    r1.raise_for_status()


    #go to class page

    r2 = s.get("https://myflye.flyefit.ie/myflye/courses")
    r2.raise_for_status()
    soup = BeautifulSoup(r2.content, features="html.parser")


    #finding the class

    yoga_class = soup.find("div",string="YOGA")
    a_tag = yoga_class.find_parents("a")[0]
    link = a_tag.get("href")


    # Book the YOGA class

    book_data = {'action': 'book_now', 'book_now': 'Book Now'}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    yoga_book = s.post("https://myflye.flyefit.ie"+link, data=book_data, headers=headers)
    yoga_book.raise_for_status()


# book_yoga_class()

book_yoga_class()