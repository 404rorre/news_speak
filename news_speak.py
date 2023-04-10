# Import needed modules
"""
requests: A popular library for making HTTP requests, allowing you to send and 
receive data from websites, APIs, and other web services.

bs4: Short for Beautiful Soup 4, a library used for parsing HTML and XML 
documents, making it easier to navigate and extract information from web pages.
"""
import requests
import bs4
import sys

# from inspect import *

# Import functions from the local package mptkg
from mptpkg import voice_to_text
from mptpkg import print_say


# Define the news_teaser() function
def news_teaser():
    """Scraps the news from "Tagesschau" and returns them as prompt."""
    # Obtain the source code from the "tagesschau" news website
    res = requests.get("https://www.tagesschau.de/")
    res.raise_for_status()

    # Use beautiful soup to parse the code
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Get the div tags that contain titles and teasers
    div_tags_top = soup.find_all(
        "div", class_="teaser teaser--top-aufmacher teaser--top"
    )
    div_tags = soup.find_all("div", class_="teaser teaser--top")

    # Index different news
    news_index = 1

    # For top article (different div tag as other main teasers)
    for div_tag in div_tags_top:
        span_short_title = div_tag.find("span", class_="teaser__topline").text
        span_long_title = div_tag.find("span", class_="teaser__headline").text
        span_teaser_text = div_tag.find("p", class_="teaser__shorttext").text
        news = f"{span_short_title}\n {span_long_title}\n {span_teaser_text}"
        print_say(news, "de_DE")

    # Go to each div_tag to retrieve the title and teasers
    for div_tag in div_tags:
        news_index += 1

        # Print the news index to seperate different news
        print(f"Nachricht {news_index}")

        # Retrieve and print the h2 tag that contains the title
        # ".text" is used to only get the text content of the span
        # seems not to be importent when inside <p> or <hx> elements
        span_short_title = div_tag.find("span", class_="teaser__topline").text
        span_long_title = div_tag.find("span", class_="teaser__headline").text
        span_teaser_text = div_tag.find("p", class_="teaser__shorttext").text
        news = f"{span_short_title}\n {span_long_title}\n {span_teaser_text}"
        print_say(news, "de_DE")

        if news_index > 10:
            break


# Print and ask you if you like to hear the news summary
question = "Möchtest du die Zusammenfassung der aktuellen Taggesschau hören?"
print_say(question, "de_DE")
# Capture voice Command
inp = voice_to_text().lower()
# If you answer "yes", activate the newscast
if "yes" in inp:
    news_teaser()
# Otherwise, exit the script
else:
    sys.exit()
