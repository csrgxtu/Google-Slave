# Author: Archer Reilly
# Date: 19/Nov/2014
# File: Utility.py
# Desc: some helper functions that will be used in main programe
#
# Produced By CSRGXTU
from google.appengine.api import urlfetch
import logging
from Download import Download
from GoogleSearchResultParser import GoogleSearchResultParser

# Google_Web_Search_Helper
# handles web search
#
# @param q (string)
# @param hl (string)
# @param start (string)
# @return json dict contains the search result or empty dict
def Google_Web_Search_Helper(q, hl='en', start=0):
  Google_Web_Search_URL = 'https://www.google.com/search?'

  if not q:
    return {}
  else:
    Google_Web_Search_URL = Google_Web_Search_URL + 'q=' + q

  Google_Web_Search_URL = Google_Web_Search_URL + '&hl=' + hl
  Google_Web_Search_URL = Google_Web_Search_URL + '&start=' + start

  d = Download(Google_Web_Search_URL)
  if d.doRequest():
    return {}
  else:
    g = GoogleSearchResultParser(d.getSOURCE())
    return g.getJson()
  """
  result = urlfetch.fetch(url=Google_Web_Search_URL)
  logging.info(type(result))
  g = GoogleSearchResultParser(result.content)
  return g.getJson()
  """
