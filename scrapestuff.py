import cookielib
import mechanize
import os
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
from os.path import basename
from os.path import splitext
from urlparse import urlsplit

#http://www.cim.mcgill.ca/~langer/251.html
def prompt():
  user_url = raw_input("Enter url to scrape: ").lower()
  url = configure_url(user_url)
  # print url
  page = urllib2.urlopen(url).read()
  soup = BeautifulSoup(page)
  # print soup.prettify() #made the html nice
  folder_name = raw_input("Enter folder name to copy file: ")
  create_folder(folder_name)
  # urllib.urlretrieve(url, os.path.join(folder_name, filename))
  for f in soup.find_all('a'):
    get_files(f.get('href'), folder_name)
  print 'Success, files have been saved'
  #soup.body.p.b finds the first bold item inside a paragraph tag inside a body  

def get_files(url, folder_name):
  print url
  filename = url.split('/')[-1]
  if filename:
    fullfilename = os.path.join(folder_name, filename)
    urllib.urlretrieve(url, fullfilename)
  # print fullfilename
  # print fullfilename
  # if (os.path.exists('./comp251langer')):
  #   print 'this exist'
  # else:
  #   print 'this doesnt'
  #urllib.urlretrieve(url, url.split('/')[-1].split('#')[0].split('?')[0])

  # print get_filename_parts_from_url(url)
  #urllib.urlretrieve(url, get_filename_parts_from_url(url))
  # page = urllib2.urlopen(url)
  # page.info()['Content-Disposition']
  # soup = BeautifulSoup(page)
  # print soup.prettify()


def create_folder(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)
  print folder

def configure_url(url):
  if not (url.startswith('http://') or url.startswith('https://')):
    print "Cannot find http or https protocol, adding http"
    url = 'http://' + url
  return url


if  __name__ == '__main__':
  prompt()

#soup = BeautifulSoup(open(page));
