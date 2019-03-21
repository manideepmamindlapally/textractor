from PIL import Image
from backend.get_text import textrecog

image_url = "http://www.golbazaar.com/wp-content/uploads/2018/07/Mens-Opulent-Printed-T-Shirts-Vol-2-white-Printed-words-single.jpg"

mode = "Handwritten"

image, text = textrecog(image_url, mode)

print(text)
image.save("./../a.png")