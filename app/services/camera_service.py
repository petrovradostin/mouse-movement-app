import os
import cv2
import time

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        saved_pictures_dir = os.path.join(os.getcwd(), 'saved_pictures')
        if not os.path.exists(saved_pictures_dir):
            os.makedirs(saved_pictures_dir)
        image_path = os.path.join(saved_pictures_dir, f'{time.time()}.jpeg')
        cv2.imwrite(image_path, frame)
        cap.release()
        return image_path
    return None
