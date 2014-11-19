"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, jsonify, request, stream_with_context, Response, make_response
import urllib2
import logging
from Download import Download
from GoogleSearchResultParser import GoogleSearchResultParser
from google.appengine.api import urlfetch

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    jsonDict = {}
    jsonDict['title'] = 'hehe'
    jsonDict['escapedUrl'] = 'http://csrgxtu.com'

    url = "http://www.google.com/search?q=csrgxtu"
    d = Download(url)
    if d.doRequest():
      return "can't do request"
    else:
      g = GoogleSearchResultParser(d.getSOURCE())
      return jsonify(g.getJson())

@app.route('/search', methods=['GET'])
def search():
  Google_Search_URL = 'https://www.google.com/search?'
  # parse url params and build query url
  q = request.args.get('q', '')
  hl = request.args.get('hl', '')
  start = request.args.get('start', '')

  if not q:
    return jsonify({})
  else:
    Google_Search_URL = Google_Search_URL + '&q=' + q

  if not hl:
    pass
  else:
    Google_Search_URL = Google_Search_URL + 'hl=' + hl

  if not start:
    pass
  else:
    Google_Search_URL = Google_Search_URL + '&start=' + start

  d = Download(Google_Search_URL)
  if d.doRequest():
    return jsonify({})
  else:
    g = GoogleSearchResultParser(d.getSOURCE())
    return jsonify(g.getJson())

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
