from testujeme_software import TestujemeSoftware
import re

ts = TestujemeSoftware()

def test_check_website():
    assert ts.check_website('https://testujeme.software/') == True

def test_get_website_title():
    assert re.match(ts.get_website_title('https://testujeme.software/'), 'Testujeme software')

def test_reverse_string():
    assert ts.reverse_string('Hello world') == 'dlrow olleH'

def test_generate_number():
    assert ts.generate_number() == 5