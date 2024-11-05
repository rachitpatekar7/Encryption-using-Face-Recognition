import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os

def encrypt_message(message, key):
    num_columns = len(key)
    num_rows = int(np.ceil(len(message) / num_columns))
    num_blanks = (num_columns * num_rows) - len(message)
    encrypted_message = [''] * num_columns

    column = 0
    row = 0

    for symbol in message:
        encrypted_message[column] += symbol
        column += 1

        if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - num_blanks):
            column = 0
            row += 1
    
    return ''.join(encrypted_message)

def recognize_face():
    cap = cv2.VideoCapture(0)
    recognized_user = "Unknown"

    while recognized_user == "Unknown":
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                recognized_user = classNames[matchIndex]
                print(f"Welcome, {recognized_user}!")
                break

        cv2.putText(img, "Looking for known faces...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Detection', img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

    return recognized_user

def send_message_and_save():
    
    sender = recognize_face()
    receiver = input("Enter receiver's name: ")
    message = input("Enter message: ")
    message = f"Message from {sender} to {receiver} on {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')} : {message}"
    encrypted_message = encrypt_message(message, receiver)
    file_name = f"Message_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(file_name, 'w') as file:
        file.write(encrypted_message)
    print(f"Message encrypted and saved to {file_name}")

path = 'Training_images'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

encodeListKnown = []
for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeListKnown.append(encode)


send_message_and_save()
