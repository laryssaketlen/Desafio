from PIL import Image

img = Image.open('Syngenta.bmp')
cores = img.convert('RGB').getcolors()
verdes = cores[1][0]

print("O número de pixels verdes é " + str(verdes))
