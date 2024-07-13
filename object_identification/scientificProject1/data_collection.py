import os
import cv2
import time
import uuid

Image_Path = "collectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
video_files = {
    'Hello': 'videos/hello.mp4',
    'Yes': 'videos/yes.mp4',
    'No': 'videos/no.mp4',
    'Thanks': 'videos/thanks.mp4',
    'IloveYou': 'videos/iloveyou.mp4',
    'Please': 'videos/please.mp4'
}

number_of_images = 5

for label in labels:
    image_path = os.path.join(Image_Path, label)
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    video_path = video_files[label]
    cap = cv2.VideoCapture(video_path)
    print(f'Capturing {label}')
    time.sleep(3)

    frame_count = 0
    while cap.isOpened() and frame_count < number_of_images:
        ret, frame = cap.read()
        if not ret:
            break

        imagename = os.path.join(Image_Path, label, label + '.' + '{}.jpg'.format(str(uuid.uuid4())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()