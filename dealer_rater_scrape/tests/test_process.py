from dealer_rater_scrape import process


def test_remove_low_stars_and_not_recommended(fake_list_reviews):
    reviews = process.remove_low_stars_and_not_recommended(fake_list_reviews)
    assert len(reviews) == 1
    assert list(reviews[0].keys()) == ["username", "title", "text", "services"]
    assert reviews[0]["services"]["Customer Service"] == 5
    assert reviews[0]["services"]["Quality of Work"] == 5
    assert reviews[0]["services"]["Friendliness"] == 5
    assert reviews[0]["services"]["Pricing"] == 5
    assert reviews[0]["services"]["Overall Experience"] == 5
    assert "Yes" in reviews[0]["services"]["Recommend Dealer"]


def test_preprocess_nlp(fake_five_stars_reviews):
    reviews = process.preprocess_nlp(fake_five_stars_reviews)
    assert list(reviews[0][0].keys()) == ["username", "title", "text", "services"]
    assert reviews[0][1] == 1
    assert reviews[1][1] == 3
    assert reviews[2][1] == 4


def test_sort_reviews(fake_reviews_with_adjectives):
    reviews = process.sort_reviews(fake_reviews_with_adjectives)
    assert reviews[0][0]["username"] == "- user03"
    assert reviews[1][0]["username"] == "- user04"
    assert reviews[2][0]["username"] == "- user02"
