import barcode
from PIL import Image
from barcode.writer import ImageWriter
ean = barcode.get('ean13', '123456789011', writer=ImageWriter())
filename = ean.save('sample')

Image.open(filename).show()