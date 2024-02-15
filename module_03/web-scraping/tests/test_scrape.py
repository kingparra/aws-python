import pytest
import requests
import bs4
import textwrap

import web_scraping.scrape as scrape


def test_fetch_202():
    """Does the http transaction return a 200 series response?"""
    URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " +
                             "AppleWebKit/537.36 (KHTML, like Gecko) " +
                             "Chrome/104.0.0.0 " +
                             "Safari/537.36"}
    assert requests.get(URL, headers=HEADERS).status_code == 200
