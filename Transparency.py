import numpy as np
import cv2

path = input("Input image path ... (ex: ./image.jpg) : ")
bgr_img = cv2.imread(path, 1)
bgra_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra_img)
h, w, c = bgra_img.shape
for i in range(w):
    for j in range(h):
        a[j, i] = 200

for i in range(w):
    for j in range(h):
        if (b[j, i] == 0 and g[j, i] == 0 and r[j, i] == 0):
            a[j, i] = 0
            b[j, i] = 255
            g[j, i] = 255
            r[j, i] = 255
output = cv2.merge([b, g, r, a])
cv2.imwrite("./output.png", output)
cv2.waitKey(0)
