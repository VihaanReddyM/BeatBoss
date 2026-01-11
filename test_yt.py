from googleapiclient.discovery import build
import re

API_KEY = "AIzaSyCUKgydyr5_Zb-WE4Djt-gCK7wygZ9cIcM"
url = "https://music.youtube.com/playlist?list=RDCLAK5uy_k6PkYWus1Mt-aKrbb0Ne8SkA2BgAk1Yy4"

# Extract playlist ID
pid = re.search(r'list=([^&]+)', url).group(1)
print(f"Playlist ID: {pid}")

# Build YouTube client
yt = build('youtube', 'v3', developerKey=API_KEY)

try:
    # Get playlist items
    req = yt.playlistItems().list(part='snippet', playlistId=pid, maxResults=10)
    resp = req.execute()
    
    items = resp.get('items', [])
    print(f"\nFound {len(items)} items:")
    
    for i, item in enumerate(items, 1):
        title = item['snippet']['title']
        print(f"{i}. {title}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
