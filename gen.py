import typing as t
from random import random, randrange

import cv2

img = cv2.imread("./mountain.jpg")

TILE_SIZE = 50
TILE_NUM_W = (img.shape[0] + TILE_SIZE - 1) // TILE_SIZE
TILE_NUM_H = (img.shape[1] + TILE_SIZE - 1) // TILE_SIZE

pixels: list[tuple[int, int, str]] = []
for h in range(TILE_NUM_H) :
    for w in range(TILE_NUM_W):
        num = randrange(0, 10**10)
        fname = f"./tiles/mountain-{num}.jpg"
        wend = min((w + 1) * TILE_SIZE, img.shape[0])
        hend = min((h + 1) * TILE_SIZE, img.shape[1])
        cv2.imwrite(fname, img[h * TILE_SIZE:hend, w * TILE_SIZE:wend])
        pixels.append((w, h, fname))

pixels.sort(key=lambda _: random())

for w, h, fname in pixels:
    print(f"""<img class="tile" style="left: {w * TILE_SIZE}px; top: {h * TILE_SIZE}px" src="{fname}"/>""")
