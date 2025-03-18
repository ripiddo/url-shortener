import hashlib
import re
import time

import flask
from sqlalchemy import func
from werkzeug.exceptions import abort

from urlshortener.common import database


def generate_short_code(length: int):
    myhash = hashlib.sha1()
    myhash.update(str(time.time()).encode('utf-8'))
    short_code = myhash.hexdigest()[:length]

    return short_code


def get_url_stats(shortcode):
    query_url = database.query(shortcode)
    return query_url


def get_url(shortcode):
    query_url = database.query(shortcode)
    return query_url


def set_url_stats(query_url):
    query_url.redirect_count += 1
    query_url.last_redirect = func.now()
    database.update_url(query_url)
    return query_url


def shorten_long_url(long_url, shortcode, query_url):
    if shortcode is None:
        shortcode = generate_short_code(6)
        database.add_url_to_db(long_url, shortcode)

    elif len(shortcode) != 6 or re.match("^[a-zA-Z0-9]*$", shortcode) is None:
        flask.abort(412, "The provided shortcode is invalid")
    else:
        database.add_url_to_db(long_url, shortcode)
    return shortcode
