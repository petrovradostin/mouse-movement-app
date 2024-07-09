import os
import cv2
import time

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        if not os.path.exists('saved_pictures'):
            os.makedirs('saved_pictures')
        image_path = f'saved_pictures/{time.time()}.jpeg'
        cv2.imwrite(image_path, frame)
        cap.release()
        return image_path
    return None
