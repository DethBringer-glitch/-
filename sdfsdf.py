import requests
from bs4 import BeautifulSoup
class Weather:
    def __init__(self, link="https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"):
        self.link = link
        r = requests.get(self.link).text
        self.soup = BeautifulSoup(r, 'html.parser')
        print(self.soup)
    def first_pars(self):
        data = self.soup.fill_all('div',{'class': 'RuLinks'})
        print(data)
if __name__ == '__main__':
    w = Weather()
    w.first_pars()
