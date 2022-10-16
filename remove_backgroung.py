from rembg import remove 
from PIL import Image
input_path = 'security.png'
output_path = 'output.png'
input = Image.open(r"D:\Python codes\Remove_Background\image.jpg")
output = remove(input)
output.save(output_path)