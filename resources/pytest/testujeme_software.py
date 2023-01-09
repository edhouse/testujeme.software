import requests
import random
from bs4 import BeautifulSoup

class TestujemeSoftware:

    @staticmethod
    def check_website(url: str) -> bool:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def get_website_title(url: str,) -> str:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response, features='html.parser')
            return soup.title.string
        except Exception as ex:
            return ''

    @staticmethod
    def reverse_string(x):
        return x[::-1]

    @staticmethod
    def generate_number():
        return random.randint(0,9)