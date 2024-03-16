import cv2
import numpy as np
THRESHOLD = 0.6
with open("coordinates.txt", "w") as f:  # Обновляем файл
    f.write("Координаты метки\n")


def coord(x, y):  # Запись координат
    with open("coordinates.txt", "a") as file:
        file.write(f'Координаты x:{x}; Координаты y:{y}\n')


cap = cv2.VideoCapture(0)
template = cv2.imread('ref-point.jpg', 0)
h, w = template.shape
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= THRESHOLD)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        coord(pt[0], pt[1])  # Перёдаем координаты в функцию
    cv2.imshow('Task3', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
