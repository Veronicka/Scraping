import pytest


@pytest.fixture
def fake_list_reviews():
    return [
        {
            "username": "- user01",
            "title": '"user01"',
            "text": "test test test",
            "ratings": {
                "Customer Service": 5,
                "Quality of Work": 5,
                "Friendliness": 5,
                "Pricing": 5,
                "Overall Experience": 5,
                "Recommend Dealer": "\r\nYes\r\n",
            },
        },
        {
            "username": "- user02",
            "title": '"user02"',
            "text": "test test test",
            "ratings": {
                "Customer Service": 5,
                "Quality of Work": 5,
                "Friendliness": 5,
                "Pricing": 5,
                "Overall Experience": 0,
                "Recommend Dealer": "\r\nYes\r\n",
            },
        },
        {
            "username": "- user03",
            "title": '"user03"',
            "text": "test test test",
            "ratings": {
                "Customer Service": 5,
                "Quality of Work": 4,
                "Friendliness": 5,
                "Pricing": 3,
                "Overall Experience": 5,
                "Recommend Dealer": "\r\nYes\r\n",
            },
        },
    ]


@pytest.fixture
def fake_five_stars_reviews():
    return [
        {
            "username": "- user01",
            "title": '"user01"',
            "text": "I think the car is good.",
            "ratings": {
                "Customer Service": 5,
                "Quality of Work": 5,
                "Friendliness": 5,
                "Pricing": 5,
                "Overall Experience": 5,
                "Recommend Dealer": "\r\nYes\r\n",
            },
        },
        {
            "username": "- user02",
            "title": '"user02"',
            "text": "It's the best car I've ever had, super fast and very good.",
            "ratings": {
                "Customer Service": 5,
                "Quality of Work": 5,
                "Friendliness": 5,
                "Pricing": 5,
                "Overall Experience": 5,
                "Recommend Dealer": "\r\nYes\r\n",
            },
        },
        {
            "username": "- user03",
            "title": '"user03"',
            "text": (
                "I'm very happy with the purchase! The car is very nice and "
                "beautiful, it is simply the best car I have ever had. The sellers "
                "were attentive and friendly."
            ),
            "ratings": {
                "Customer Service": 5,
                "Quality of Work": 5,
                "Friendliness": 5,
                "Pricing": 5,
                "Overall Experience": 5,
                "Recommend Dealer": "\r\nYes\r\n",
            },
        },
    ]


@pytest.fixture
def fake_reviews_with_compliments():
    return [
        (
            {
                "username": "- user01",
                "title": '"user01"',
                "text": "I think the car is good.",
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            1,
        ),
        (
            {
                "username": "- user02",
                "title": '"user02"',
                "text": "It's the best car I've ever had, super fast and very good.",
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            2,
        ),
        (
            {
                "username": "- user03",
                "title": '"user03"',
                "text": (
                    "I'm very happy with the purchase! The car is very nice and "
                    "beautiful, it is simply the best car I have ever had. The sellers "
                    "were attentive and friendly."
                ),
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            4,
        ),
        (
            {
                "username": "- user04",
                "title": '"user04"',
                "text": (
                    "The car is really good, I am satisfied with my purchase. "
                    "Everything is perfect."
                ),
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            3,
        ),
    ]


@pytest.fixture
def fake_reviews_with_compliments_tied():
    return [
        (
            {
                "username": "- user01",
                "title": '"user01"',
                "text": (
                    "I'm very happy with the purchase! The car is very nice and "
                    "beautiful, it is simply the best car I have ever had. The sellers "
                    "were attentive and friendly."
                ),
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            4,
        ),
        (
            {
                "username": "- user02",
                "title": '"user02"',
                "text": "It's the best car I've ever had, super fast and very good.",
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            2,
        ),
        (
            {
                "username": "- user03",
                "title": '"user03"',
                "text": (
                    "I'm very happy with the purchase! The car is very nice and "
                    "beautiful, it is simply the best car I have ever had. The sellers "
                    "were attentive and friendly."
                ),
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            4,
        ),
        (
            {
                "username": "- user04",
                "title": '"user04"',
                "text": "I think the car is good.",
                "ratings": {
                    "Customer Service": 5,
                    "Quality of Work": 5,
                    "Friendliness": 5,
                    "Pricing": 5,
                    "Overall Experience": 5,
                    "Recommend Dealer": "\r\nYes\r\n",
                },
            },
            1,
        ),
    ]


@pytest.fixture
def fake_tokenized_words():
    return ["The", "car", "is", "the", "best"]


@pytest.fixture
def fake_stopped_words():
    return ["car", "beautiful", "best", "good", "fast", "cool", "blue"]
