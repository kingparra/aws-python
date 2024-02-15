#!/usr/bin/python3
import requests
import os
from bs4 import BeautifulSoup


def get_page(url):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " +
                             "AppleWebKit/537.36 (KHTML, like Gecko) " +
                             "Chrome/104.0.0.0 Safari/537.36"}
    return requests.get(url, headers=headers)


def find_titles(page):
    soup = BeautifulSoup(page.content, "html.parser")
    titles = soup.find_all(
            'div',
            {'class': 'ipc-title ipc-title--base ' +
                      'ipc-title--title ipc-title-link-no-icon ' +
                      'ipc-title--on-textPrimary sc-be6f1408-9 ' +
                      'srahg cli-title'}
        )
    return titles


def format_title(title_element):
    return title_element.a.text.split(".")[1].strip()


def filter_links_for_review(links):
    for link in links:
        if link.text == "User reviews":
            review_link = link['href']
    return review_link


def main():
    page = get_page("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    if page.status_code != 200:
        print("Unable to find URL")
    else:
        titles = find_titles(page)
        base_url = "https://www.imdb.com"
        for title in titles[:10]:
            movie_title = format_title(title)

            os.makedirs("Reviews", exist_ok=True)
            with open(f"Reviews/{movie_title}", "w") as f:
                movie_page = get_page(f"{base_url}{title.a['href']}")
                soup = BeautifulSoup(movie_page.content, "html.parser")

                ipc_link = soup.find_all(
                        'a',
                        {'class': 'ipc-link ipc-link--baseAlt' +
                                  ' ipc-link--inherit-color'}
                    )

                for r in ipc_link:
                    if r.text == "User reviews":
                        review_link = r['href']

                # Navigate to Movie title's review page
                all_reviews_page = requests.get(f"{base_url}{review_link}")
                soup = BeautifulSoup(all_reviews_page.content, "html.parser")
                reviews = soup.find_all('div', {'class': 'text show-more__control'})

                print(f'Recording reviews for {movie_title}...')
                for review in reviews:
                    f.write(review.text + "\n")
