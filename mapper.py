#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import re

urls = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}')
romanNumerals = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

for line in sys.stdin:
    line = re.sub(r'[\d_]', '', line)
    if re.search(urls, line):
        line = re.sub(urls, '', line)
    line = line.strip()
    words = line.split()
    for word in words:
        word = re.sub('\-\-+', '', word)
        word = re.sub(r'[^\w-]', '', word)
        if re.search(romanNumerals, word) and word != "I":
            word = re.sub(romanNumerals, '', word)
        word = word.lower()
        if (word != '') and (len(word) > 1 or word == 'a' or word == 'i'):
            print('%s\t%s' % (word, 1))
