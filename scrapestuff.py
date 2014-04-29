import cookielib
import mechanize
import os
#import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
from os.path import basename
from os.path import splitext
from urlparse import urlsplit
# prog = re.compile(pattern)

#http://www.cim.mcgill.ca/~langer/251.html
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
    get_files(f.get('href'))

  #soup.body.p.b finds the first bold item inside a paragraph tag inside a body  

def get_files(url):
  #print url.split('/')
  urllib.urlretrieve(url, url.split('/')[-1].split('#')[0].split('?')[0])

  # print get_filename_parts_from_url(url)
  #urllib.urlretrieve(url, get_filename_parts_from_url(url))
  # page = urllib2.urlopen(url)
  # page.info()['Content-Disposition']
  # soup = BeautifulSoup(page)
  # print soup.prettify()

def get_filename_parts_from_url(url):
    fullname = url.split('/')[-1].split('#')[0].split('?')[0]
    t = list(os.path.splitext(fullname))
    if t[1]:
        t[1] = t[1][1:]
    return t

def configure_url(url):
  if (not (url.startswith('http://') or url.startswith('https://'))):
    print "Cannot find http or https protocol, adding http"
    url = 'http://' + url
  return url


if  __name__ == '__main__':
  prompt()

#soup = BeautifulSoup(open(page));
