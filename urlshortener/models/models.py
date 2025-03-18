from sqlalchemy import text, func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT

from urlshortener import db


class URL(db.Model):
    url_id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(200), nullable=False)
    short_code = db.Column(db.String(6), index=True, unique=True)
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    last_redirect = db.Column(TIMESTAMP, nullable=True)
    redirect_count = db.Column(db.Integer, default=0)

    def __init__(self, url_id, long_url, short_code, last_redirect, redirect_count):
        self.url_id = url_id
        self.long_url = long_url
        self.short_code = short_code
        self.last_redirect = last_redirect
        self.redirect_count = redirect_count

    def stats_to_json(self):
        return dict(created_at=self.created_at, last_redirect=self.last_redirect, redirect_count=self.redirect_count)

    def shortcode_to_json(self):
        return dict(short_code=self.short_code)
