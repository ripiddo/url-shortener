from urlshortener.models.models import URL


def test_new_url():

    url = URL(url_id=1, long_url="htts://www.energyworx.com", short_code="ab12cd34", redirect_count=3,
              last_redirect="2021-03-02 23:02:25")
    assert url.url_id == 1
    assert url.long_url == "htts://www.energyworx.com"
    assert url.short_code == "ab12cd34"
    assert url.redirect_count == 3
    assert url.last_redirect == "2021-03-02 23:02:25"
