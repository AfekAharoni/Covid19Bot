import requests
from bs4 import BeautifulSoup
import datetime


def get_data(url):
    """ This function import the data from the covid19's site
    :param url: url of the covid19 details' site
    :return: covid19_data
    :rtype: list
    """
    html_content = requests.get(url).content
    soup = BeautifulSoup(html_content, "html.parser")
    covid19_data = []
    daily_man_sick = soup.find_all('p', class_="stat-total")
    covid19_data.append(daily_man_sick[0].get_text())  # Index 0
    daily_infection_coefficient = soup.find_all('p', class_="stat-total")
    covid19_data.append(daily_infection_coefficient[1].get_text())  # Index 1
    daily_man_vaccine = soup.find_all('p', class_="stat-total")
    covid19_data.append(daily_man_vaccine[2].get_text())  # Index 2
    daily_man_total_vaccine = soup.find_all("strong")
    covid19_data.append(daily_man_total_vaccine[2].get_text())  # Index 3
    date = datetime.datetime.now().strftime("%x")
    covid19_data.append(date)  # Index 4
    return covid19_data

#print(get_data("https://corona.mako.co.il/"))

