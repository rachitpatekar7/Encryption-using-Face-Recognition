# Face Recognition Messaging System

## Overview

This project implements a face recognition system that allows users to send encrypted messages to each other. It utilizes OpenCV and the face_recognition library to identify users based on their facial features. The messages are encrypted using a simple columnar transposition method before being saved to a text file.

## Features

- **Face Recognition**: The system captures video input and recognizes faces from a set of known individuals.
- **Encrypted Messaging**: Messages are encrypted before being saved, ensuring privacy.
- **User Interface**: The system displays a video feed while searching for known faces.

## Requirements

To run this project, you need the following libraries:

- Python 3.x
- OpenCV
- NumPy
- face_recognition
- datetime (part of the standard library)

You can install the necessary packages using pip:

```bash
pip install opencv-python numpy face_recognition
```

## Setup

1. **Prepare Training Images**:
   - Create a directory named `Training_images`.
   - Add images of the individuals you want to recognize. The file names should be the names of the individuals (e.g., `Alice.jpg`, `Bob.jpg`).

2. **Run the Code**:
   - Ensure your camera is connected.
   - Execute the script. The program will start capturing video and looking for known faces.

## Usage

1. The program will display the video feed and prompt the user to recognize a face.
2. Once a face is recognized, the user will be prompted to enter the receiver's name and the message.
3. The message will be encrypted and saved to a text file with a timestamp.

## Functionality

### `encrypt_message(message, key)`

Encrypts a message using a simple columnar transposition cipher based on a provided key.

- **Parameters**:
  - `message`: The message to be encrypted (string).
  - `key`: The key for encryption (string).
- **Returns**: The encrypted message (string).

### `recognize_face()`

Captures video from the webcam to recognize faces.

- **Returns**: The name of the recognized user (string).

### `send_message_and_save()`

Manages the process of recognizing a face, taking input for the message, and saving the encrypted message to a file.

## File Output

The encrypted messages are saved in the current directory with the format:
```
Message_YYYY-MM-DD_HH-MM-SS.txt
```

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
