# Welcome to the Scraping Dealer Rater

This project scrapes the first five pages of DealerRater.com and chooses the top three reviews by a criterion.

The criterion used was to count the `COMPLIMENTS` words found in each review. The review that contains the highest number of keywords is ranked first, so on and so forth until the third review. If there is a tie, the first review found comes first in the classification.

For example:

`COMPLIMENTS` = [**good**, **beautiful**, **fast**]

1º - I like the car. It's **good**, **beautiful** and **fast**.

2º - I like the car. It's **good** and **fast**.

3º - I like the car. It's **fast**.


`COMPLIMENTS` is a list of keywords. New words can be inserted on the list through the code.

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

The scraping returns the three most “overly positive” endorsements. Each review contains the map:
```
Username: user0
Review: the body of review

Ratings:
CUSTOMER SERVICE 5,
QUALITY OF WORK 5,
FRIENDLINESS 5,
PRICING 5,
OVERALL EXPERIENCE 5,
RECOMMEND DEALER	"YES"    

```

## Tests

Run the code to execute the tests:
```
$ python -m pytest dealer_rater_scrape
```

