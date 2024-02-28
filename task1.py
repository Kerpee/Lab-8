import cv2
image = cv2.imread('variant-2.png')
blurred_image = cv2.GaussianBlur(image, (7, 7), 6)
cv2.imwrite('output.jpg',  blurred_image)
