import requests
from bs4 import BeautifulSoup
try:

    url = str(input("url -> "))

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        textPage = soup.select('p')
        for items in textPage:
            print(items.text)
    else:
        print('error')
except SyntaxError:
    print('Ссилка не дійсна')
