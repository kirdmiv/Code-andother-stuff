import random
from PIL import Image, ImageDraw

img1 = Image.open("otl1.jpg")
img2 = Image.open("otl2.jpg")


pix1 = img1.load()
pix2 = img2.load()
width = img1.size[0]  # Определяем ширину.
height = img1.size[1]  # Определяем высоту.
image = Image.new("RGB", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image)

for i in range(width):
    for j in range(height):
        r1 = pix1[i, j][0]
        g1 = pix1[i, j][1]
        b1 = pix1[i, j][2]
        r2 = pix2[i, j][0]
        g2 = pix2[i, j][1]
        b2 = pix2[i, j][2]
        mid1 = (r1 + g1 + b1) // 3
        if abs(r1 - r2) < 50 and abs(g1 - g2) < 50 and abs(b1 - b2) < 50:
            draw.point((i, j), (mid1, mid1, mid1))
        else:
            draw.point((i, j), (255, 0, 0))

del draw
image.save("newimage.jpg", "JPEG")
