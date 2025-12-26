#CREATE_DATASET:




import cv2
import dlib
import imutils
import os

# Initialize dlib's HOG-based face detector
hog_face_detector = dlib.get_frontal_face_detector()

# Open a connection to the webcam (usually camera index 0)
video_capture = cv2.VideoCapture(0)

# Create the directory to save images if it doesn't exist
save_dir = 'gobi'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Initialize a counter for the images
image_counter = 0
max_images = 200

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    # Resize the frame for better processing
    frame = imutils.resize(frame, width=600)
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = hog_face_detector(gray, 1)
    
    # Process each face detected
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        
        # Draw rectangle around the face
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Crop the region around the face with some padding
        cropped_image = frame[max(y-50, 0):y+h+50, max(x-50, 0):x+w+50]
        
        # Resize the cropped image to passport size (413x531 pixels)
        passport_size_image = cv2.resize(cropped_image, (413, 531))
        
        # Save the passport-size image
        image_path = os.path.join(save_dir, f'gobi{image_counter+1}.jpg')
        cv2.imwrite(image_path, passport_size_image)
        
        # Display the passport-size image in a separate window (optional)
        cv2.imshow('Passport Size Photo', passport_size_image)
        
        # Increment the counter
        image_counter += 1

        # Check if we have saved enough images
        if image_counter >= max_images:
            break

    # Break the loop when 'q' is pressed or when the maximum number of images is reached
    if cv2.waitKey(1) & 0xFF == ord('q') or image_counter >= max_images:
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
