

---

# **Raspberry Pi DHT11 & Face Detection System**  

## **Overview**  
This Python script combines **DHT11 sensor data collection** and **face detection** using **OpenCV**. It continuously:  
1. Reads temperature and humidity from the **DHT11** sensor.  
2. Captures an image using **libcamera**.  
3. Detects faces in the captured image using **OpenCV's Haar Cascade classifier**.  

## **Hardware Requirements**  
- **Raspberry Pi (with GPIO access)**  
- **DHT11 Temperature & Humidity Sensor**  
- **Camera Module (Raspberry Pi Camera)**  

## **Software Requirements**  
Ensure the following are installed on your Raspberry Pi:  
- **Python 3**  
- **Adafruit DHT library**  
- **OpenCV (cv2)**  
- **libcamera** (for capturing images)  

### **Installation Steps**  
1. **Update & Upgrade Packages**  
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Required Python Libraries**  
   ```sh
   pip install adafruit-circuitpython-dht opencv-python
   ```

3. **Enable Camera & GPIO Access**  
   ```sh
   sudo raspi-config
   ```
   - Enable **Camera Interface**  
   - Enable **I2C and GPIO access**  

4. **Run the Script**  
   ```sh
   python3 face_dht.py
   ```

## **How It Works**  
1. **DHT11 Sensor Readings:**  
   - Reads **temperature** and **humidity** from the **DHT11 sensor** connected to GPIO17.  
   - Displays the readings in the console.  

2. **Face Detection:**  
   - Captures an image using the **libcamera-jpeg** command.  
   - Uses **OpenCV Haar Cascade classifier** to detect faces in the image.  
   - Prints the number of faces detected in the image.  

## **GPIO Connections (DHT11 to Raspberry Pi)**  
| DHT11 Pin | Raspberry Pi Pin |  
|-----------|-----------------|  
| VCC       | 3.3V (Pin 1)     |  
| Data      | GPIO17 (Pin 11)  |  
| GND       | GND (Pin 9)      |  

## **Future Enhancements**  
- Implement **real-time video face detection**.  
- Store **DHT11 readings in a database** for logging.  
- **Email alerts** when a face is detected.  

## **Author**  
**Shakti Dheerays S**  


---
