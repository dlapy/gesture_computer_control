import mediapipe as mp
import cv2 
from typing import NamedTuple
import pyautogui as pag


class Coordinates(NamedTuple):
    for_x: int
    for_y: int

class Screen_resolution(NamedTuple):
    resolution_x: int
    resolution_y: int


def resolution() -> Screen_resolution:
    """Size you screen"""

    widthScreen, heightScreen = pag.size()
    return widthScreen, heightScreen


def get_coordinates(cap,hands) -> Coordinates:
    """Return coordinates finger"""

    while True:
        _, img = cap.read()
        result = hands.process(cv2.resize(cv2.flip(img, 1), resolution()))
        #result = hands.process(img)
        if result.multi_hand_landmarks:

            for id, lm in enumerate( result.multi_hand_landmarks[0].landmark):
                h,w = resolution()
                #print(h,w)
                cx,cy = int(lm.x * w), int(lm.y * h)
                #cv2.circle(img, (cx,cy), 3, (255, 0, 255))
                if id==8:
                    return Coordinates(**{"for_x": cx, "for_y":cy })
        #cv2.imshow("Hand treaking", img)
        cv2.waitKey(1)
