APP_PY:



import cv2
import face_recognition
import numpy as np
import os
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
import serial
import time

# Load the trained model
model_path = r'Mymodel.h5'
model = load_model(model_path)

# Configure the serial port (adjust parameters as necessary)
ser = serial.Serial('COM4', 9600, timeout=1)  # Windows example, change for Linux/Unix

# Load known faces and their names
known_faces_dir = "known_faces"
known_encodings = []
known_names = ['gopi', 'guru', 'kavin']

# Load each image in the known_faces directory
for filename in os.listdir(known_faces_dir):
    image_path = os.path.join(known_faces_dir, filename)
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]  # Get face encoding
    known_encodings.append(encoding)
    known_names.append(os.path.splitext(filename)[0])  # Use filename as name

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    
    # Convert frame to RGB (face_recognition requires RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare detected face with known faces
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_names[best_match_index]
            # Send the recognized person's name via UART
            print('authorize')
            ser.write(b'a')  # Send name as byte string
            # time.sleep(3)
        else:
            ser.write(b'b')  # Send 'Unknown' if no match
            print('UN authorized')
            # time.sleep(3)

        # Draw a rectangle and label on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # ser.write(b'c')
    print('no one here')
    # Display the result
    cv2.imshow("Face Recognition", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources before exiting
video_capture.release()
ser.close()  # Close the serial port
cv2.destroyAllWindows()
