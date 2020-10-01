# Welcome to the Scraping Dealer Rater

This project scrapes the first five pages of DealerRater.com and chooses the top three reviews by a criterion.

It could be done with machine learning, but it would need a much larger number of reviews.

The criterion used was to count the `MY_KEY` words (list of keywords) found in each review. The review that contains the highest number of keywords is the first place in hanking, the second with the highest number of words is the second place and the third place is the third largest with keywords.

For example:

`MY_KEYS` = [**good**, **beauty**, **fast**]

1º - I like the car. It's **good**, **beauty** and **fast**.

2º - I like the car. It's ***good** and **fast**.

3º - I like the car. It's **fast**.


`MY_KEYS` is a list of keywords, this list can be attached or create a new one.

### Installation

Install the pipfile https://github.com/pypa/pipenv
```
$ sudo apt update
$ sudo apt install pipenv
```

Install project dependencies:
```
$ pipenv install
```

### Usage

With the dependencies installed, you can start using the project.

Start the virtual env created by pipenv.
```
$ pipenv shell
```

Using:
```
$ python -m dealer_rater_scrape
Usage: __main__.py [OPTIONS] COMMAND [ARGS]...

  A Dealer For the People. Identifies the top three most overly excited
  reviews for a McKaig Chevrolet Buick

Options:
  --help  Show this message and exit.

Commands:
  download-nltk-packages
  init-scraping
```

If is the first time you're executing, you need to install nltk package:
```
$ python -m dealer_rater_scrape download-nltk-packages
```

Running scraping:
```
$ python -m dealer_rater_scrape init-scraping
```

The result is the three most “overly positive” endorsements. Each review contains the dictionary:
 - **username**: username review person
 - **text**: review
 - **services**: dictionary services name and stars

## Tests

Run the code to execute the tests:
```
$ python -m pytest dealer_rater_scrape
```

