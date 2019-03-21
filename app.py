from PIL import Image
from backend.get_text import textrecog

image_url = "https://i.ytimg.com/vi/Mh9-NlRGA7g/maxresdefault.jpg"

mode = "Handwritten"

image, text = textrecog(image_url, mode)

print(text)
image.show()