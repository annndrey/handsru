#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re
import unicodedata
import unittest


#re1 = '\d*\s*\(*\d*\)*\s?\d{3}-\d{2}-?\d{2}'
#re2 = '8\s?\(?\d{3}\)?\s?\d{3}-\d{2}-?\d{2}'
re3 = '\d*\s*\(*\d*\)*\s+\d\d\d-\d{2}-?\d{2}'
re_phone = re.compile(re3)


def find_phones(URL):
    """ A simple function that takes \
    an URL, reads HTML, finds all matched numbers\ 
    and returns a list of normailsed phone numbers"""
    
    with urllib.request.urlopen(URL) as response:
        html = response.read()
        try:
            decoded = html.decode('utf-8')
        except UnicodeDecodeError:
            decoded = html.decode('cp1251')
        # print(decoded)
        normalised = unicodedata.normalize("NFKD", decoded)
        phones =re_phone.findall(normalised)
        phones = [p.replace("(", "").replace(")", "").replace("-", "").replace(" ", "") for p in phones]

        return phones



class Testing(unittest.TestCase):
    def test_hands_ru(self):
        url = 'https://hands.ru/company/about'
        self.assertEqual(find_phones(url), ['84951377767', ])

    def test_repetitors_info(self):
        url = 'https://repetitors.info'
        self.assertEqual(find_phones(url), ['84955405676', '88005555676'])

#URLS = [' https://hands.ru/company/about', 'https://repetitors.info']

#for u in URLS:
#    find_phones(u)
unittest.main()
