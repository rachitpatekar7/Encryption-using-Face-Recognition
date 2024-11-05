import cv2
import numpy as np
import face_recognition
import os
import math

# Transposition Cipher functions
def decrypt_message(encrypted_message, key):
    num_columns = len(key)
    num_rows = math.ceil(len(encrypted_message) / num_columns)
    num_blanks = (num_columns * num_rows) - len(encrypted_message)

    decrypted_message = [''] * num_rows

    column = 0
    row = 0
    index = 0

    for symbol in encrypted_message:
        decrypted_message[row] += symbol
        index += 1

        if index >= len(encrypted_message):
            break

        row += 1

        if row == num_rows:
            row = 0
            column += 1

    return ''.join(decrypted_message).strip()

# Function to recognize face
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

# Function to receive and decrypt message from file
def receive_message_and_decrypt():
    receiver = recognize_face()
    file_name = input("Enter file name containing the encrypted message: ")

    with open(file_name, 'r') as file:
                content = file.read()
                decrypted_message = decrypt_message(content, receiver)
                decrypted_words = decrypted_message.split()
                if len(decrypted_words) >= 5 and decrypted_words[4] == receiver:
                    print(decrypted_message)
                else:
                    print("No messages for you in this file.")
        

# Example usage
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

receive_message_and_decrypt()
