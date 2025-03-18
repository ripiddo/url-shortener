import flask
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import abort

from urlshortener import db, app
from urlshortener.models.models import URL


def add_url_to_db(long_url, shortcode):
    new_url = URL(url_id=None, long_url=long_url, short_code=shortcode, last_redirect=None, redirect_count=None)
    try:
        db.session.add(new_url)
        db.session.commit()

    except SQLAlchemyError as e:
        error = str(e)
        app.logger.debug(error)
        db.session.rollback()
        if "Duplicate entry" in error:
            flask.abort(409, "Shortcode already in use")

    return shortcode


def query(shortcode):
    return URL.query.filter_by(short_code=shortcode).first()


def update_url(query_url):
    try:
        query_url
        db.session.commit()

    except SQLAlchemyError as e:
        error = str(e)
        app.logger.debug(error)
        db.session.rollback()
    return query_url
