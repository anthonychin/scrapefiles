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
  f = urllib2.urlopen(url)
  print f.read()

def configure_url(url):
  if (not (url.startswith('http://') or url.startswith('https://'))):
    print "Cannot find http or https protocol, adding http"
    url = 'http://' + url
  return url


if  __name__ == '__main__':
  prompt()

#soup = BeautifulSoup(open(page));
