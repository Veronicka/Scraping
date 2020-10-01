from dealer_rater_scrape import processor


def test_remove_low_stars_and_not_recommended(fake_list_reviews):
    reviews = processor.remove_not_recommended_reviews(fake_list_reviews)
    assert len(reviews) == 1
    assert list(reviews[0].keys()) == ["username", "title", "text", "ratings"]
    assert reviews[0]["ratings"]["Customer Service"] == 5
    assert reviews[0]["ratings"]["Quality of Work"] == 5
    assert reviews[0]["ratings"]["Friendliness"] == 5
    assert reviews[0]["ratings"]["Pricing"] == 5
    assert reviews[0]["ratings"]["Overall Experience"] == 5
    assert "Yes" in reviews[0]["ratings"]["Recommend Dealer"]


def test_preprocess_nlp(fake_five_stars_reviews):
    reviews = processor.preprocess_nlp(fake_five_stars_reviews)
    assert list(reviews[0][0].keys()) == ["username", "title", "text", "ratings"]
    assert reviews[0][1] == 1
    assert reviews[1][1] == 3
    assert reviews[2][1] == 5


def test_sort_reviews(fake_reviews_with_adjectives):
    reviews = processor.sort_top_three_reviews(fake_reviews_with_adjectives)
    assert reviews[0][0]["username"] == "- user03"
    assert reviews[1][0]["username"] == "- user04"
    assert reviews[2][0]["username"] == "- user02"


def test_remove_low_stars_ratings(fake_list_reviews):
    review_five_stars = fake_list_reviews[0]
    review_low_stars = fake_list_reviews[2]
    high_stars = processor.remove_low_stars_ratings(review_five_stars["ratings"])
    low_stars = processor.remove_low_stars_ratings(review_low_stars["ratings"])

    assert high_stars == True
    assert low_stars == False


def test_generate_token(fake_five_stars_reviews):
    first_review = fake_five_stars_reviews[0]
    second_review = fake_five_stars_reviews[1]
    first_tokenized = processor.generate_token(first_review)
    second_tokenized = processor.generate_token(second_review)

    assert first_tokenized == ["I", "think", "the", "car", "is", "good"]
    assert second_tokenized == [
        "Its",
        "the",
        "best",
        "car",
        "Ive",
        "ever",
        "had",
        "super",
        "fast",
        "and",
        "very",
        "good",
    ]


def test_remove_stop_words(fake_tokenized_words):
    stopped = processor.remove_stop_words(fake_tokenized_words)

    assert len(stopped) == 3
    assert stopped == ["The", "car", "best"]


def test_count_compliments(fake_stopped_words):
    compliments = processor.count_compliments(fake_stopped_words)

    assert len(fake_stopped_words) == 7
    assert compliments == 4