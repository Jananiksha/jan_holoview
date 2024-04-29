import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon = 0.8,maxHands=2)
cam = cv2.VideoCapture(0)
while True:
    success, img = cam.read()
    hands, img = detector.findHands(img)
    #print(len(hands))
    #hand-dict_(lmlist-bbox-center-type)
    if hands:
        #hand1
        hand1 = hands[0]
        lmList = hand1["lmList"]#list of 21 landmarks
        bbox1 = hand1["bbox"]#bounding box info x,y,w,h
        centerPoint1 = hand1["center"]#center of the hand cx,cy
        handType1 = hand1["type"]#hand type,left or right
        
        #print(lmList,len(lmList))
        #print(bbox1)
        #print(centerPoint1)
        cv2.circle(img=img,center=centerPoint1,radius=10,color =(0,255,255))
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList[8][:2] , lmList[12][:2], img)
        
        if (len(hands)==2):
            hand2 = hands[1]
            lmList2 = hand2["lmList"]#list of 21 landmarks
            bbox2 = hand2["bbox"]#bounding box info x,y,w,h
            centerPoint2 = hand2["center"]#center of the hand cx,c
            handType2 = hand2["type"]#hand type,left or right
            #print(lmList,len(lmList))
            #print(bbox1)
            # print(centerPoint1)
            cv2.circle(img=img,center=centerPoint2,radius=10,color =(0,255,255))
            fingers2 = detector.fingersUp(hand2)
            #print(fingers1,fingers2)#to show wheather the finger is up or down
            #length, info , img = detector.findDistance(lmList[8][:2],lmList2[8][:2],img)
            length, info, img = detector.findDistance(centerPoint1,centerPoint2, img)
            print(length)
            if length > 150:
                pyautogui.scroll(100)
            else:
                pyautogui.scroll(-100)
            
    cv2.imshow("Image",img)
    cv2.waitKey(1)
