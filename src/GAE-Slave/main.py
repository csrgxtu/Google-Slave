# Import the Flask Framework
from google.appengine.api.app_identity import get_application_id
from flask import Flask, jsonify, request, stream_with_context, Response, make_response
from urllib import quote
import logging
from Utility import Google_Web_Search_Helper

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def msg():
  appname = get_application_id()
  return 'Google Slaver [' + appname + '] started and running'

@app.route('/search', methods=['GET'])
def search():
  # parse url params and build query url
  q = quote(unicode(request.args.get('q', '')).encode('utf-8'))
  hl = request.args.get('hl', '')
  start = request.args.get('start', '')

  return jsonify(Google_Web_Search_Helper(q, hl, start))

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
