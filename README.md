# Welcome to the Scraping Dealer Rater

This project scrapes the first five pages of DealerRater.com and chooses the top three reviews by a criterion.

It could be done with machine learning, but it would need a much larger number of reviews.

The criterion used was to count the MY_KEY words (list of keywords) found in each review. The review that contains the highest number of keywords is the first place in hanking, the second with the highest number of words is the second place and the third place is the third largest with keywords.

For example:

MY_KEYS = ['good', 'beauty', 'fast']

1º - I like the car. It's 'good', 'beauty' and fast.

2º - I like the car. It's 'good' and 'beauty'.

3º - I like the car. It's 'good' and 'fast'.