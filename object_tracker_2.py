import numpy as np
import cv2

cap = cv2.VideoCapture("videos/Ball_horz.mp4")
ret = True
frameNo = 0;
while(ret):
    print frameNo
    ret ,frame = cap.read()
    if frameNo==110: #this is the start frame
        c = 957
        r = 1301
        h = 132
        w = 123
        track_window = (c,r,w,h)
        roi = frame[r:r+h, c:c+w]
        hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

        # # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )


    if (frameNo > 110) and (frameNo < 165):
        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

            # apply meanshift to get the new location
            retval, track_window = cv2.meanShift(dst, track_window, term_crit)
            # Draw it on image
            x,y,w,h = track_window
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
            cv2.imshow('img2',frame)
	    print x+w/2,y+h/2
            k = cv2.waitKey(60) & 0xff
            if k == 27:
		break

    if (frameNo <=110) or (frameNo >=165):
	print "None"

    frameNo+=1
cv2.destroyAllWindows()
cap.release()
