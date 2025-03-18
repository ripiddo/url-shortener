import re

from urlshortener.common.service import generate_short_code, shorten_long_url


def test_shortcode():
        assert len(generate_short_code(6)) ==6
        assert re.match("^[a-zA-Z0-9]*$", generate_short_code(6)) is not None

def test_shorten_long_url():

    data = {
    "url": "https://www.energy.com/",
    "shortcode": "c83df7"
    }
    assert shorten_long_url('https://www.energy.com/', 'c83df7', query_url=None)

