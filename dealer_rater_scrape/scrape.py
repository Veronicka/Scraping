import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def scraping_response(response):
    list_reviews = []
    html = BeautifulSoup(response.text, "html.parser")
    for review in html.select(".review-entry"):
        for review_wrapper in review.select(".review-wrapper"):
            title = review_wrapper.h3
            username = review_wrapper.span
            text = review_wrapper.select_one(".review-content")

            review_dict = {}
            review_dict["username"] = username.text
            review_dict["title"] = title.text
            review_dict["text"] = text.text
            review_dict["services"] = {}

            for rating in review_wrapper.select(".review-ratings-all"):
                for tr in rating.select(".tr"):
                    name_service = tr.select_one(".lt-grey.small-text.td")
                    qtd_star = tr.select_one(".rating-static-indv")
                    if qtd_star:
                        qtd_star = int(qtd_star.attrs["class"][1][-2])
                    else:
                        qtd_star = tr.select_one(".td.small-text.boldest").text.replace(
                            " ", ""
                        )
                    review_dict["services"][name_service.text] = qtd_star
            list_reviews.append(review_dict)
    return list_reviews


def request_url(url, pages=5):
    logger.info("Getting url data ...")

    list_reviews = []
    total = 0
    session = requests.Session()
    for page in reversed(range(pages)):
        response = session.get(f"{url}/page{page+1}")
        reviews = scraping_response(response)
        list_reviews.append(reviews)
        size_reviews = len(reviews)
        logger.info("Page %d - %d reviews found", page + 1, size_reviews)
        total += size_reviews
    logger.info("Total %d reviews found", total)
    return list_reviews