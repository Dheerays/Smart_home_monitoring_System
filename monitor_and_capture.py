import adafruit_dht
import board
import time
import subprocess
import cv2  # OpenCV for face recognition

dht_device = adafruit_dht.DHT11(board.D17)

# Load pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_image(filename):
    try:
        # Capture the image using libcamera-jpeg
        subprocess.run(['libcamera-jpeg', '-o', filename], check=True)
        print(f"Image captured and saved as {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")

def detect_faces(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print(f"Detected {len(faces)} face(s) in the image.")

try:
    while True:
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            print(f"Temp: {temperature_c} C   Humidity: {humidity}%")

            # Capture image
            capture_image('test.jpg')

            # Perform face detection
            detect_faces('test.jpg')

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(10)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Script interrupted by user")
