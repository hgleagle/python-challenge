#!/usr/bin/env python3

import re
from urllib import request


if __name__ == "__main__":
    with request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as f:
        html = f.read().decode()
        data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
        print("".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", data, re.DOTALL)))
