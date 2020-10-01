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
    reviews_list_by_page = scraper.request_url()

    reviews = (items for pages in reviews_list_by_page for items in pages)
    recommended_reviews = processor.remove_not_recommended_reviews(reviews)
    processed_reviews = processor.preprocess_nlp(recommended_reviews)
    top_reviews = processor.sort_top_three_reviews(processed_reviews)
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