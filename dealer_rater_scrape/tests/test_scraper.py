import json
import pytest
import requests
import codecs
from mock import patch, Mock
from dealer_rater_scrape import scraper


def test_scraping_response(requests_mock):
    with codecs.open("./dealer_rater_scrape/tests/response_mock.html") as html:
        requests_mock.get(
            "http://test.com",
            text=html.read(),
        )

    response = requests.get("http://test.com")
    result = scraper.scraping_response(response)

    assert len(result) == 10
    assert type(result) == list
    assert list(result[0].keys()) == ["username", "title", "text", "ratings"]
    assert result[0]["username"] == "- Maria"
    assert result[1]["username"] == "- Joana"


@patch.object(requests.Session, "get")
def test_request_url(mock_get):
    with codecs.open("./dealer_rater_scrape/tests/response_mock.html") as html:
        mock_get.return_value.ok = True
        mock_get.return_value.text = html.read()

    result = scraper.request_url()

    assert len(result) == 5
    assert len(result[0]) == 10
    assert type(result) == list
    assert list(result[0][0].keys()) == ["username", "title", "text", "ratings"]
    assert result[0][0]["username"] == "- Maria"
    assert result[0][1]["username"] == "- Joana"
    assert result[0][-1]["username"] == "- Amanda"
