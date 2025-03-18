import logging

import flask
from flask import request, jsonify, abort

from urlshortener import app
from urlshortener.common import service

logging.basicConfig(level=logging.DEBUG)


@app.route('/shorten', methods=['POST'])
def shorten():
    content = request.get_json()
    long_url = content.get('url')

    if long_url is None:
        flask.abort(400, "Url not present")
    else:
        req_shortcode = content.get('shortcode')
        shortcode = service.shorten_long_url(long_url, req_shortcode, query_url=None)
        return jsonify(shortcode=shortcode), 201


@app.route('/<shortcode>', methods=['GET'])
def shortcode(shortcode):
    query_url = service.get_url(shortcode)
    if query_url is None:
        flask.abort(404, "Shortcode not found")
    else:
        query_url = service.set_url_stats(query_url)

    return jsonify(shortcode=shortcode), 302, {'Location': str(query_url.long_url)}


@app.route('/<shortcode>/stats', methods=['GET'])
def stats(shortcode):
    query_url = service.get_url_stats(shortcode)
    if query_url is None:
        flask.abort(404, "Shortcode not found")
    else:
        return query_url.stats_to_json()
