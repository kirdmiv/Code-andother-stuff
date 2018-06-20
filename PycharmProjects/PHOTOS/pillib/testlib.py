def grey():
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            mid = (r + g + b) // 3
            draw.point((i, j), (mid, mid, mid))


def negativ():
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            draw.point((i, j), (255 - r, 255 - g, 255 - b))


def skepta():
    r_c = int(input('r_c:'))
    g_c = int(input('g_c:'))
    b_c = int(input('b_c:'))
    depth = int(input('depth:'))
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            mid = (r + g + b) // 3
            r = min(mid + r_c * depth, 255)
            g = min(mid + g_c * depth, 255)
            b = min(mid + b_c * depth, 255)
            draw.point((i, j), (r, g, b))


def fact():
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            r = min(max(pix[i, j][0] + rand, 0), 255)
            g = min(max(pix[i, j][1] + rand, 0), 255)
            b = min(max(pix[i, j][2] + rand, 0), 255)
            draw.point((i, j), (r, g, b))


def brightness():
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            r = min(max(pix[i, j][0] + factor, 0), 255)
            g = min(max(pix[i, j][1] + factor, 0), 255)
            b = min(max(pix[i, j][2] + factor, 0), 255)
            draw.point((i, j), (r, g, b))


def black_white():
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            sum = r + g + b
            if sum > (((255 + factor) // 2) * 3):
                r, g, b = 255, 255, 255
            else:
                r, g, b = 0, 0, 0
            draw.point((i, j), (r, g, b))


def check():
    m = int(input("mod:"))
    if m == 0:
        grey()
    elif m == 1:
        negativ()
    elif m == 2:
        skepta()
    elif m == 3:
        brightness()
    elif m == 4:
        fact()
    elif m == 5:
        black_white()


import random
from PIL import Image, ImageDraw

img = Image.open("testpic.jpg")

pix = img.load()
width = img.size[0]  # Определяем ширину.
height = img.size[1]  # Определяем высоту.
image = Image.new("RGB", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image)
#check()
fact()
del draw
image.save("newim.jpg", "JPEG")
