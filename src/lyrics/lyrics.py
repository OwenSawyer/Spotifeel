import requests
from bs4 import BeautifulSoup


def export_lyrics(artist, song):
    token = 'abc'
    song_url = search(token, artist, song)
    if song_url:
        song_lyrics = lyric_scraper(song_url)


def search(token, artist, song):
    headers = {"Authorization": "Bearer " + token}
    search_url = 'http://api.genius.com/search'
    search_data = {'q': song + " " + artist}
    search_results = requests.get(search_url, params=search_data, headers=headers).json()

    for match in search_results["response"]["hits"]:
        if artist == match["result"]["primary_artist"]["name"]:
            return match["result"]["url"]


def lyric_scraper(url):
    source = requests.get(url).text
    source_soup = BeautifulSoup(source, "html.parser")
    lyrics = source_soup.find("lyrics")
    return lyrics.get_text().strip().replace('\n', ' ')


