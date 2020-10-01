import logging.config

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"}
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "standard",
            }
        },
        "loggers": {
            "": {"handlers": ["default"], "level": "INFO", "propagate": True},
        },
    }
)

MY_KEYS = [
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
]

URL_DEALER_RATER = (
    "https://www.dealerrater.com/dealer/"
    "McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685"
)
