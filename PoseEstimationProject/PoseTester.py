import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
ptime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img,(lmList[14][1],lmList[14][2]), 15, (0,0, 255), cv2.FILLED)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("VideoStream", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break