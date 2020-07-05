import pytesseract as tess
#if tesseract wasn't found out
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

image = Image.open("C:/Users/Mehedi Hassan Galib/Desktop/Python/qqq.jpg")
image = image.convert('L')  #if the image is too much noisy and unable to be converted into text, then we will make the image grey, and try it.
image.save('qqqq.jpg')
text = tess.image_to_string(Image.open('qq.jpg'))
print(text)
