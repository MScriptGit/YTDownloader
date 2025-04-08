from pytubefix import Search

def YTSearch(userInput):
    listTitle = []
    listDuration = []
    listURL = []

    results = Search(userInput)
        
    for video in results.videos:
        listTitle.append(f'{video.title}')
        listDuration.append(f'Duration: {video.length} sec')
        listURL.append(f'URL: {video.watch_url}')
        
    return listTitle, listDuration, listURL