import pytest
from flask import json

sample_data = {
    "url": "https://www.energyworx.com/",
    "shortcode": "c83df7"
}


@pytest.fixture
def client(request):
    import urlshortener
    return urlshortener.app.test_client()


def test_shorten_withoutcode(client):
    data = {
        "url": "https://www.energyworx.com/",
    }
    rv = client.post('/shorten', data=json.dumps(data),
                     content_type='application/json')
    assert rv.status_code == 201


def test_shorten_urlnotpresent(client):
    data = {
        "shortcode": "c83df7"
    }
    response = client.post('/shorten', data=json.dumps(data),
                           content_type='application/json')
    assert b'Url not present' in response.data


def test_shorten(client):
    data = {
        "url": "https://www.energyworx.com/",
        "shortcode": "c83df7"
    }
    rv = client.post('/shorten', data=json.dumps(data),
                     content_type='application/json')
    assert rv.status_code == 201


def test_shorten_alreadyinuse(client):
    data = {
        "url": "https://www.energyworx.com/",
        "shortcode": "c83df7"
    }
    response = client.post('/shorten', data=json.dumps(data),
                           content_type='application/json')

    assert b'c83df7' in response.data


def test_shortcode_notfound(client):
    response = client.get('/c83df8')
    assert b'Shortcode not found' in response.data


def test_stats(client):
    response = client.get('/c83df7/stats')
    assert response.status_code == 200
