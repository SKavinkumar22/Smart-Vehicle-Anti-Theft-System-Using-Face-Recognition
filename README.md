# Smart-Vehicle-Anti-Theft-System-Using-Face-Recognition
An AI-powered vehicle anti-theft system that detects unauthorized drivers using face recognition and alerts the vehicle owner via message in real time.
# 🚗 AI-Based Vehicle Anti-Theft System Using Face Recognition

An **AI-powered smart vehicle security system** that prevents car theft by identifying **unauthorized drivers using face recognition** and **alerting the vehicle owner in real time** through messages, along with hardware-level access control.



## 🔍 Problem Statement
Vehicle theft is a major security concern. Traditional key-based systems can be easily bypassed.  
This project introduces an **intelligent AI-based authentication system** that allows only **authorized users** to operate the vehicle and **alerts the owner immediately** if a theft attempt is detected.



## 💡 Solution Overview
This system uses a **camera + deep learning model** to recognize the driver's face.  
If the detected face does **not match authorized users**, the system:
- Blocks vehicle access
- Sends an alert message to the vehicle owner
- Triggers hardware response via Arduino



## ⚙️ System Workflow

Camera → Face Detection → Face Recognition (CNN)
↓
Authorized?
YES → Vehicle Access ON
NO → Alert Owner + Access Blocked

yaml
Copy code



## 🗂 Project Folder Structure

AI-Based-Vehicle-Anti-Theft-System-Using-Face-Recognition/
│
├── README.md
├── requirements.txt
│
├── models/
│ └── Mymodel.h5
│
├── dataset/
│ ├── kavin/
│ ├── gurunath/
│ └── gobi/
│
├── create_dataset/
│ └── create_dataset.py
│
├── flask_app/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│
├── standalone_app/
│ └── app_py_serial.py
│
├── hardware/
│ ├── arduino_code.ino
│ └── circuit_diagram.png
│
└── screenshots/
├── authorized.png
├── unauthorized.png
└── alert_sent.png

yaml
Copy code



## 🧠 Key Modules Explained

### 1️⃣ Dataset Creation
Captures real-time face images using webcam and stores them for training.

📁 `create_dataset/create_dataset.py`



### 2️⃣ Face Recognition Model
- CNN-based deep learning model
- Trained on authorized driver faces
- Confidence threshold used to reject unknown faces

📁 `models/Mymodel.h5`
OUTPUT SCREE SHOT:
<img width="372" height="314" alt="image" src="https://github.com/user-attachments/assets/581636d7-6826-4780-9af8-8cd0c212f687" />



### 3️⃣ Real-Time Monitoring (Flask App)
- Live camera feed
- Face detection and recognition
- Displays person name and confidence score

📁 `flask_app/app.py`



### 4️⃣ Vehicle Hardware Control & Alert System
- Communicates with Arduino via UART
- Sends:
  - `'a'` → Authorized driver → Vehicle enabled
  - `'b'` → Unauthorized driver → Alert + Vehicle disabled

📁 `standalone_app/app_py_serial.py`



## 🔔 Alert Mechanism
When an unauthorized face is detected:
- System sends a signal to the hardware
- Alert message is sent to the vehicle owner
- Vehicle access is blocked



## 🧰 Technologies Used

| Category | Tools |
|--------|------|
| Programming | Python |
| AI / ML | TensorFlow, Keras |
| Computer Vision | OpenCV, dlib, face_recognition |
| Web | Flask |
| Hardware | Arduino, UART |
| Communication | Serial (COM Port) |



## 🔌 Hardware Components
- Arduino UNO
- Webcam
- Relay / Motor Driver / Buzzer
- Power Supply
- Vehicle Lock Simulation

---

## ▶️ How to Run the Project

### Install Dependencies

pip install -r requirements.txt
Run Flask App
bash
Copy code
python flask_app/app.py
Run Hardware Integration
bash
Copy code
python standalone_app/app_py_serial.py
📸 Results
Authorized user → Vehicle access granted

Unauthorized user → Owner alerted + access denied

Real-time recognition with high accuracy

🎯 Applications
Smart Vehicle Anti-Theft System

Fleet Security

Personal Car Protection

Automotive Embedded Systems

🚀 Future Enhancements
GPS location tracking

Mobile app alerts

Cloud logging

IR night vision camera

Edge AI deployment (Raspberry Pi / Jetson Nano)

👨‍💻 Author
Kavin Kumar
🎓 BE – Electronics & Communication Engineering
🤖 AI | Embedded Systems | Computer Vision
🇮🇳 India














