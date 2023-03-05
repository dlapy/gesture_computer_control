from capture import get_coordinates
import mediapipe as mp
import cv2 
import pyautogui as pag


capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
hands_1 = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_tracking_confidence=0.5, min_detection_confidence=0.5)


def mous_control():
    coordinates = get_coordinates(capture,hands_1)
    pag.moveTo(coordinates)

