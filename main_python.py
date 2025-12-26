#MAIN_PYTHON:





import cv2
import numpy as np
from flask import Flask, render_template, Response, request
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
import dlib

app = Flask(__name__)

# Load the trained model
model_path = r'Mymodel.h5'
model = load_model(model_path)

# Define the class labels
class_labels = ['Gurunath', 'Kavin kumar','gobi']
confidence_threshold = 0.8  # Adjust as needed

# OpenCV video capture object (global)
camera = None

@app.route('/')
def index():
    """Renders the main page with the start/stop buttons and video feed."""
    return render_template('index.html')

def generate_frames():
    """Generates video frames from the webcam for the video feed."""
    global camera
    camera = cv2.VideoCapture(0)  # Initialize camera
    hog_face_detector = dlib.get_frontal_face_detector()  # Initialize face detector
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Resize the frame for better processing
            frame = cv2.resize(frame, (600, 400))

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = hog_face_detector(gray, 1)

            for face in faces:
                x, y, w, h = (face.left(), face.top(), face.width(), face.height())
                cropped_image = frame[y:y+h, x:x+w]
                resized_image = cv2.resize(cropped_image, (75, 75))
                img = img_to_array(resized_image)
                img = np.expand_dims(img, axis=0) / 255.0  # Normalize

                # Predict the class
                prediction = model.predict(img)
                predicted_class_index = np.argmax(prediction, axis=1)[0]
                predicted_confidence = np.max(prediction)

                if predicted_confidence < confidence_threshold:
                    predicted_class = 'unknown'
                else:
                    predicted_class = class_labels[predicted_class_index]

                # Draw rectangle around the face and put the predicted label
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f'{predicted_class} ({predicted_confidence:.2f})', 
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame as a response to the video feed request
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Route to stream the video feed."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    """Releases the camera when the stop button is clicked."""
    global camera
    if camera is not None:
        camera.release()  # Release the camera resource
        camera = None
    return "Camera Stopped", 200

if __name__ == "__main__":
    app.run(debug=True)





