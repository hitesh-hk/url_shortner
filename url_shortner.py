from urllib.request import urlopen
from urllib.parse import urlencode
import contextlib
import argparse

def make_url_short(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8 ')

parser = argparse.ArgumentParser(description = "Url needs to be parsed")
parser.add_argument('url',help='url needed to be shortened')
args = parser.parse_args()
inp_url = args.url
shorten_url = make_url_short(inp_url)
print(shorten_url)
