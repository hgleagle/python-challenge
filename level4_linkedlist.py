#!/usr/bin/env python3

from urllib import request
from urllib.parse import urlparse, urljoin
import re


if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    with request.urlopen(url) as f:
        html = f.read().decode()
        data = re.findall('a href="(.*?)">', html, 0)[0]
        next_url = urljoin(url, data)
        olddata = data.split('=')[-1]
        uri = next_url.replace(olddata, "%s")

    pattern = re.compile("and the next nothing is (\d+)")
    while True:
        print(next_url)
        with request.urlopen(next_url) as f:
            html = f.read().decode()
            m = pattern.search(html)
            if m is None:
                break
            num = m.group(1)
            print("going to %s", num)
            # if m.group(1) == str(16044):
                # num = int(m.group(1)) // 2
            next_url = uri % num

