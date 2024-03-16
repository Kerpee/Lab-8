import cv2
import numpy as np
THRESHOLD = 0.6
cap = cv2.VideoCapture(0)
ref = cv2.imread('ref-point.jpg', 0)
fly = cv2.imread('fly64.png', 0)
fly = cv2.resize(fly, (64, 64))
h, w = ref.shape
fly_h, fly_w = fly.shape
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_frame, ref, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= THRESHOLD)
    for pt in zip(*loc[::-1]):
        center_x, center_y = pt[0] + w // 2, pt[1] + h // 2  # Определяем центр метки на кадре
        top_left_x, top_left_y = center_x - fly_w // 2, center_y - fly_h // 2  # Находим левый угол для вставки мухи
        frame[top_left_y:top_left_y + fly_h, top_left_x:top_left_x + fly_w, 0] = fly  # Вставляем в кадр муху
    cv2.imshow('Fly', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
