import torch

import cv2, time
import numpy as np
from yolov6.core.inferer import Inferer
from imutils.video import VideoStream

from speak import Speak
from telegram_utils import send_telegram
from section_selection import draw_polygon

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

model = Inferer('./weights/yolov6n_base.pt', 0, './coco.yaml', 640, False)
video = VideoStream(src='rtsp://admin:@192.168.1.86/user=admin_password=_channel=1_stream=1.sdp').start()
detect = False
points = []
t1 = time.time()
speak = Speak()

while True:
    frame = draw_polygon(cv2.rotate(video.read(), cv2.cv2.ROTATE_90_CLOCKWISE), points)
    
    if detect:
        frame, state = model.infer(frame, points)
        t2 = time.time()
        if state and (t2-t1)>10:
            speak.speak_thread("Intrusion Warning")
            cv2.imwrite('output.jpg',frame)
            send_telegram('output.jpg')
            t1 = t2

    key = cv2.waitKey(30)
    if key == ord('q'):
        points.append(points[0])
        detect = True

    cv2.imshow("Intrusion Warning", frame)
    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)
# When everything done, release the capture
video.stop()
cv2.destroyAllWindows()

