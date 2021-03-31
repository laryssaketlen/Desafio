# -- coding: utf-8 --
import cv2

img = cv2.imread('Syngenta.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cont = 0

altura, largura = img.shape[0], img.shape[1]

for i in range(altura):
    for j in range(largura):
        if (img[i, j] == [96, 192, 0]).all():
            cont += 1

print("O número de pixels verdes é " + str(cont))
