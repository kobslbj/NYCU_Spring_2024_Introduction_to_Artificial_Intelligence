import cv2
import numpy as np

video_capture = cv2.VideoCapture('video.mp4')

# 背景消除
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break  

    frame_resized = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)

    fgmask = fgbg.apply(frame_resized)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    extracted_objects = cv2.bitwise_and(frame_resized, frame_resized, mask=fgmask)
    stacked_frames = np.hstack((frame_resized, cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR), extracted_objects))

    cv2.imshow('video', stacked_frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
