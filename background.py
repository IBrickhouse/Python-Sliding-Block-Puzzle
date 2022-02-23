from RedditReader import Subreddit
from PIL import Image
import requests

# gets the url from reddit. This uses r/twicemedia
image = Subreddit("Twicemedia")
image.get_random()
image_url = image.url
#url.show()
#print(image_url)

# grabs the image and shows it
im = Image.open(requests.get(image_url, stream=True).raw)
#im.show()

#saves image to project directory
im.save("images/twicebg.jpg")