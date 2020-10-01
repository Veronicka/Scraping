import click
import nltk
import itertools

from . import log_settings
from . import scraper
from . import processor


@click.group()
def cli():
    """A Dealer For the People.
    Identifies the top three most overly excited reviews for a McKaig Chevrolet Buick"""
    pass


@cli.command()
def download_nltk_packages():
    nltk.download("stopwords")
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")


@cli.command()
def init_scraping():
    reviews_by_page = scraper.request_url()
    top_reviews = processor.process_reviews(reviews_by_page)
    show_top_reviews(top_reviews)


def show_top_reviews(top_reviews):
    count = itertools.count(start=1)
    for review, _ in top_reviews:
        click.secho("\n***** REVIEW %d *****\n" % next(count))
        click.secho("Username: %s" % review["username"], fg="green")
        click.secho("Review: %s" % review["text"], fg="green")
        click.secho("\nRatings:", fg="green")
        for service, stars in review["ratings"].items():
            click.secho("%s  %s" % (service, stars), fg="green")


if __name__ == "__main__":
    cli()