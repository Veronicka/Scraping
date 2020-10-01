import random
import logging
import nltk
import re
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

logger = logging.getLogger(__name__)

# Stop Words are small words that can be ignored during language processing
# without changing the meaning of the sentence.
STOP_WORDS = list(set(stopwords.words("english")))

MINIMUM_STARS = 5

COMPLIMENTS = [
    "recommend",
    "smile",
    "honest",
    "satisfying",
    "satisfied",
    "polite",
    "helpful",
    "best",
    "friendly",
    "enjoyed",
    "great",
    "good",
    "nice",
    "perfect",
    "positive",
    "fantastic",
    "happy",
    "sure",
    "well",
    "professional",
    "highly",
    "genuinely",
    "fast",
    "beauty",
    "beautiful",
]


def remove_not_recommended_reviews(reviews):
    logger.info("Removing not recommended reviews ...")
    good_reviews = []
    for review in reviews:
        if "Yes" in review["ratings"]["Recommend Dealer"]:
            if remove_low_stars_ratings(review["ratings"]):
                good_reviews.append(review)
    return good_reviews


def remove_low_stars_ratings(ratings):
    logger.info("Removing low stars reviews ...")

    for service, stars in ratings.items():
        if isinstance(stars, int) and stars < MINIMUM_STARS:
            return False
    return True


def preprocess_nlp(list_reviews):
    logger.info("Preprocessing NLP ...")
    reviews = []
    for review in list_reviews:
        tokenized = generate_token(review)
        stopped = remove_stop_words(tokenized)
        number_of_compliments = count_compliments(stopped)
        reviews.append((review, number_of_compliments))
    return reviews


def generate_token(review):
    return word_tokenize(re.sub(r"[^(a-zA-Z)\s]", "", review["text"]))


def remove_stop_words(tokenized):
    return [w for w in tokenized if not w in STOP_WORDS]


def count_compliments(stopped):
    compliments = [word for word in COMPLIMENTS if word in stopped]
    return len(compliments)


def sort_top_three_reviews(reviews):
    reviews.sort(reverse=True, key=lambda a: a[1])
    return reviews[:3]