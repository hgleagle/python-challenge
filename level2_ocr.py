#!/usr/bin/env python3
"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""
from urllib import request
import re


def solution1():
    s = []
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    with request.urlopen(url) as f:
        html = f.read().decode()
        data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
        for c in data:
            if c.isalpha():
                s.append(c)
    print("".join(s))


# print low frequency character
def solution2():
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    with request.urlopen(url) as f:
        html = f.read().decode()
        s = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
        s = ''.join(s.split('\n'))
    occurences = {}
    for c in s:
        occurences[c] = occurences.get(c, 0) + 1
    avg_oc = len(s) // len(occurences)
    print("".join([c for c in s if occurences[c] < avg_oc]))


if __name__ == "__main__":
    solution1()
    solution2()
