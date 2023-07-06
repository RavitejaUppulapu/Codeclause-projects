import pyshorteners
import requests


def shorten_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return shortened_url


def expand_url(shortened_url):
    response = requests.head(shortened_url, allow_redirects=True)
    return response.url


url = input("Enter URL: ")
shortened_url = shorten_url(url)
print("Shortened URL:", shortened_url)

expanded_url = expand_url(shortened_url)
print("Expanded URL:", expanded_url)
