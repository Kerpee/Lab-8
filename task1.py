# -*- coding: utf-8 -*-
import cv2
image = cv2.imread('images/variant-2.png')
blur_image = cv2.GaussianBlur(image, (7, 7), 6) # Размытие по Гауссу
cv2.imwrite('elephant.jpg', blur_image)
