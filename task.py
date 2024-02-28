import cv2


def coordinate(x,y):
    with open('coordinates.txt', 'a') as file:
        file.write(f"Координаты: x={x} ; y={y}\n")


cap = cv2.VideoCapture(0)
label = cv2.imread('ref-point.jpg')
illusory = cv2.ORB_create()
keypoints, descrp = illusory.detectAndCompute(label, None)
match_bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
while True:
    ret, frame = cap.read()
    keypoint_fr, descrp_fr = illusory.detectAndCompute(frame, None)
    matches = match_bf.match(descrp, descrp_fr)
    x, y = keypoint_fr[0].pt
    coordinate(x, y)
    img_match = cv2.drawMatches(label, keypoints, frame, keypoint_fr, matches, None, flags=cv2.DrawMatchesFlags_DEFAULT)
    cv2.imshow('Match', img_match)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
