import cv2
import imutils
import numpy as np
img = cv2.imread("/home/edward/star.jpg")
img2 = img
#blurred = cv2.GaussianBlur(img, (51, 51), 30)
#thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY)[1]
edges=cv2.Canny(img,50,100)
cntrs=cv2.findContours(edges.copy(),cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE)
cntrs = cntrs[0] if imutils.is_cv2() else cntrs[1]

for c in cntrs:
    m = cv2.moments(c)
    if m["m00"] == 0:
        cx = int(m["m10"]/.0001)
        cy = int(m["m10"]/.0001)
    else:
        cx = int(m["m10"]/m["m00"])
        cy = int(m["m01"]/m["m00"])
    cv2.drawContours(img, [c], -1, (0,255,0),1)
    #cv2.circle(img2,(cx,cy), 1, (255,255,255), -5)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

