# 🛡️ Safe Zone - Wearable Tracking System for Alzheimer's Patients

Safe Zone is a smart wearable project designed to improve the safety and independence of individuals suffering from Alzheimer’s disease. It provides real-time GPS tracking, geofencing alerts, and SOS functionalities — all integrated into a tamper-resistant smartwatch. This project was developed as part of the *Joy of Engineering* course at **BML Munjal University**.



## 📌 Problem Statement

Patients with Alzheimer’s often suffer from memory loss, disorientation, and wandering, placing them at significant risk. Existing solutions are either too expensive, easy to remove, or require constant connectivity. **Safe Zone** addresses these gaps by offering an affordable, wearable, and secure device that ensures constant tracking and caregiver alerting.

---

## 🔧 Features

- 📍 **Real-Time GPS Tracking**  
- 🚧 **Geofencing with Auto Alerts**  
- 🆘 **SOS Emergency Button**  
- 🔒 **Tamper-Resistant Smart Lock**  
- 📡 **Cloud & Offline Data Storage**  
- 💻 **Responsive Web Interface for Caregivers**  

---

## 🧰 Tech Stack

### 📟 Hardware
- Arduino Uno
- A7672S GPS Module
- SIM800L GSM Module
- OLED Display
- Buzzer
- Custom Locking Mechanism

   <figure>
  <img src="https://github.com/charan-608/SAFE-ZONE/blob/main/DOCUMENTATION/CIRCUIT_DIAGRAM.png?raw=true" alt="Circuit Diagram" width="450"/>
  <figcaption><strong></strong> Circuit Diagram</figcaption>
</figure>





### 🌐 Software
- Arduino IDE (Embedded C)
- Firebase (for real-time location storage)
- HTML, CSS, JavaScript (Frontend)
- Leaflet.js (Map Integration)
- Node.js/Express (Backend APIs)

---

## 🖥️ Website Features

- 🏠 **Landing & Sign-In Page**
- 📊 **Live Location Dashboard**
- 🗺️ **Geofencing Interface**
- 🚓 **Nearby Police Stations & Hospitals**
- 📱 **Mobile Responsive Design**

> Check out the documentation folder for in depth details
<figure>
  <img src="https://github.com/charan-608/SAFE-ZONE/blob/main/DOCUMENTATION/Working%20images.jpg?raw=true" alt="Demo Screenshot" width="450"/>
  <figcaption><strong></strong> SafeZone Project Working Image</figcaption>
</figure>



---

## ⚙️ Workflow Overview

1. **Data Collection**: Location captured by the GPS module.
2. **Transmission**: Sent via GSM to Firebase/cloud.
3. **Storage & API**: Data processed and served to the frontend.
4. **Frontend Display**: Location visualized on a live map.
 <figure>
  <img src="https://github.com/charan-608/SAFE-ZONE/blob/main/DOCUMENTATION/FLOW_DIAGRAM.png?raw=true" alt="Flow Diagram" width="450"/>
  <figcaption><strong></strong> Flow Chart</figcaption>
</figure>


