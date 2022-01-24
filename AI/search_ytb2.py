from youtube_search import YoutubeSearch
import webbrowser

while True:
    results = YoutubeSearch('paper short love', max_results=10).to_dict()
    if results:
        break
url = 'https://www.youtube.com' + results[0]['url_suffix']
webbrowser.open(url)