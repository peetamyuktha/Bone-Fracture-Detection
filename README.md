# Bone Fracture Detection Using Deep Learning

## Table of Contents
- [Introduction](#introduction)
- [Project Scope](#project-scope)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Testing](#testing)
- [Contributors](#contributors)
- [Future Scope](#future-scope)

## Introduction
The **Bone Fracture Detection System** is a deep learning-based solution designed to assist healthcare professionals in identifying bone fractures through medical imaging. By leveraging Convolutional Neural Networks (CNNs) and object detection models like YOLO, the system aims to enhance diagnostic accuracy and speed.

## Project Scope
This project focuses on automating the detection and classification of bone fractures in X-ray and CT scan images, providing an efficient tool for radiologists to improve diagnostic processes.

## Features
- Automatic detection and classification of bone fractures.
- Real-time processing of medical images.
- Integration with clinical workflows for seamless use.
- User-friendly interface for both doctors and patients.
- High accuracy rates achieved through deep learning models (CNN, YOLO).

## Architecture
The system architecture consists of:
- **Input Data Acquisition**: Medical images from X-ray machines.
- **Preprocessing**: Image quality enhancement using Canny edge detection.
- **Model Processing**: Deep learning models analyze images for fracture detection.
- **Detection and Classification**: Fractures are localized and classified using trained models.

## Technologies Used
- **Programming Language**: Python (3.7)
- **Frameworks/Libraries**: PyTorch, Django, OpenCV, Matplotlib, NumPy
- **Database**: MySQL
- **Deep Learning Models**: Convolutional Neural Networks (CNN), YOLO
- **Operating System**: Windows 8 or above

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Bone-Fracture-Detection.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the MySQL database and update the connection details in the project files.

## Usage
1. Run the Django server:
   ```bash
   python manage.py runserver
   ```
2. Access the application through your web browser at `http://127.0.0.1:8000/index.html`.
3. Use the interface to upload X-ray images for fracture detection.

## Results
The system provides high accuracy for fracture detection:
- **CNN and YOLO models** achieved detection rates up to **94%**.
- Improved diagnostic speed and reliability compared to traditional methods.

## Testing
### Types of Testing Implemented:
- **Unit Testing**: Ensures individual components work as expected.
- **Integration Testing**: Checks the interaction between different modules.
- **Functional Testing**: Validates the system against defined requirements.
- **System Testing**: Ensures the complete system functions correctly.
- **Black Box Testing**: Verifies output correctness without knowledge of internal code structure.

## Contributors
- **P. Yuktha** (217R1A05P6)
- **B. Deeksha** (217R1A05L7)
- **P. Raghava** (217R1A05P8)

Under the guidance of **Dr. Raj Kumar Patra**.

## Future Scope
Potential future enhancements include:
- Detection of micro-fractures and other bone conditions.
- Integration with MRI and 3D CT scans for complex case handling.
- Predictive analytics for fracture risk assessment based on patient history.
