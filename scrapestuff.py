import cookielib
import mechanize
import os
#import re
import sys
import urllib2
from bs4 import BeautifulSoup
from os.path import basename
from urlparse import urlsplit
# prog = re.compile(pattern)


def prompt():
  print "hello world"
  user_url = raw_input("Enter url: ").lower()
  #result = re.match(pattern, url)
  #print result
  url = configure_url(user_url)
  print url
  page = urllib2.urlopen(url).read()
  soup = BeautifulSoup(page)
  print soup.prettify() #made the html nice

  for f in soup.find_all('a'):
    print f.get('href')

  #soup.body.p.b finds the first bold item inside a paragraph tag inside a body  

def configure_url(url):
  if (not (url.startswith('http://') or url.startswith('https://'))):
    print "Cannot find http or https protocol, adding http"
    url = 'http://' + url
  return url


if  __name__ == '__main__':
  prompt()

#soup = BeautifulSoup(open(page));
