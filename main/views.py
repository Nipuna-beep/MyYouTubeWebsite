import requests
from django.shortcuts import render

def home(request):
    # API තොරතුරු
    api_key = 'AIzaSyDZls_lGEmX2vWnOmXyZ5J-jZeOBdL3tds'
    channel_id = 'UC2tgc8NDdsj1ewSPfW8WoyQ' # Nipuna AI Studio ID
    
    # YouTube API එකට Request එකක් යැවීම
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=3&type=video'
    
    videos = []
    try:
        response = requests.get(url)
        data = response.json()
        if 'items' in data:
            for item in data['items']:
                videos.append({
                    'title': item['snippet']['title'],
                    'thumbnail': item['snippet']['thumbnails']['high']['url'],
                    'video_id': item['id']['videoId']
                })
    except Exception as e:
        print(f"Error: {e}")

    return render(request, 'home.html', {'videos': videos})