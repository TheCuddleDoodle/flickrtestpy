import requests


FLICKR_PUBLIC = os.environ["FLICKR_PUBLIC"]
FLICKR_SECRET = os.environ["FLICKR_SECRET"]

#send a request to popular.photos
def get_popular_photos():
    url = "https://api.flickr.com/services/rest/"
    params = {
        "method": "flickr.photos.getPopular",
        "api_key": FLICKR_PUBLIC,

        "user_id": "195564741@N05",
   

    }
    response = requests.get(url, params=params)
    return response.content

# curl -X GET "https://api.flickr.com/services/rest/" -d "method=flickr.photos.getPopular&api_key=29e7860acd226d16e7397650ba0d7d1e&user_id=195564741@N05&format=json&nojsoncallback=1"

images = get_popular_photos()
print(images)
