import click
import nltk

from . import scrape
from . import process
from . import settings


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
def scraping():
    reviews_list_by_page = scrape.request_url(settings.URL_DEALER_RATER, pages=5)

    reviews = (items for pages in reviews_list_by_page for items in pages)
    reviews = process.remove_low_stars_and_not_recommended(reviews)
    reviews = process.preprocess_nlp(reviews)
    reviews = process.sort_reviews(reviews)

    for review, _ in reviews:
        click.secho("Username: %s" % review["username"], fg="green")
        click.secho("Review: %s" % review["text"], fg="green")
        for service, stars in review["services"].items():
            click.secho("%s stars %s" % (service, stars), fg="green")


if __name__ == "__main__":
    cli()