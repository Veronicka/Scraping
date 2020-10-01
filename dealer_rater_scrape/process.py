import random
import logging
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

from . import settings

logger = logging.getLogger(__name__)

STOP_WORDS = list(set(stopwords.words("english")))


def remove_low_stars_and_not_recommended(list_reviews):
    logger.info("Removing low stars and not recommended reviews ...")
    reviews_stars = []
    for review in list_reviews:
        if "Yes" not in review["services"]["Recommend Dealer"]:
            continue

        all_stars = True
        for service, stars in review["services"].items():
            if isinstance(stars, int) and stars < 5:
                all_stars = False
                break
        if all_stars:
            reviews_stars.append(review)
    return reviews_stars


def preprocess_nlp(list_reviews):
    logger.info("Tokenizing, removing stop words and counting adjectives ...")
    reviews = []
    for review in list_reviews:
        tokenized = word_tokenize(re.sub(r"[^(a-zA-Z)\s]", "", review["text"]))
        stopped = [w for w in tokenized if not w in STOP_WORDS]
        words = [word for word in settings.MY_KEYS if word in stopped]
        reviews.append((review, len(words)))
    return reviews


def sort_reviews(reviews):
    reviews.sort(reverse=True, key=lambda a: a[1])
    return reviews[:3]