import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

URL_DEALER_RATER = (
    "https://www.dealerrater.com/dealer/"
    "McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685"
)

PAGES = 5


def request_url():
    logger.info("Getting url data ...")

    list_reviews = []
    total = 0
    session = requests.Session()
    for page in reversed(range(PAGES)):
        response = session.get(f"{URL_DEALER_RATER}/page{page+1}")
        reviews = scraping_response(response)
        list_reviews.append(reviews)

        logger.info("Page %d - %d reviews found", page + 1, len(reviews))
        total += len(reviews)
    logger.info("Total %d reviews found", total)
    return list_reviews


def scraping_response(response):
    reviews = []
    scraped_reviews = BeautifulSoup(response.text, "html.parser")
    reviews_entries = scraped_reviews.select(".review-entry")
    for entry in reviews_entries:
        for review_wrapper in entry.select(".review-wrapper"):
            review = build_review(review_wrapper)
            reviews.append(review)
    return reviews


def get_review_ratings(review_wrapper):
    review_ratings = {}
    for ratings in review_wrapper.select(".review-ratings-all"):
        for rating in ratings.select(".tr"):
            name_rating = rating.select_one(".lt-grey.small-text.td")
            number_stars = rating.select_one(".rating-static-indv")
            if number_stars:
                number_stars = int(number_stars.attrs["class"][1][-2])
            else:
                number_stars = rating.select_one(".td.small-text.boldest").text.replace(
                    " ", ""
                )
            review_ratings[name_rating.text] = number_stars
    return review_ratings


def build_review(review_wrapper):
    review = {}
    title = review_wrapper.h3
    username = review_wrapper.span
    text = review_wrapper.select_one(".review-content")

    review["username"] = username.text
    review["title"] = title.text
    review["text"] = text.text
    review["ratings"] = get_review_ratings(review_wrapper)
    return review
