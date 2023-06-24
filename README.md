# Description  
The Auto Proctoring System is a project developed in Visual Studio Code that utilizes artificial intelligence techniques to monitor students during exams. The system leverages computer vision, audio analysis, and data visualization to detect head movements, analyze audio inputs, generate warnings for suspicious behavior, calculate cheat percentiles, and plot behavior graphs.

## Features
+ Head pose detection using the OpenCV library (cv2) to monitor students' head movements.
+ Real-time video processing with MediaPipe for accurate and efficient head pose estimation.
+ Audio analysis with speech recognition libraries (e.g., SpeechRecognition) to detect unusual sounds or conversations.
+ Text-to-speech conversion with pyttsx for providing audio feedback or warnings.
+ Data visualization using Matplotlib to plot behavior graphs and display the cheat percentile.
+ Integration of machine learning models for improved accuracy and behavior analysis.

## Usage
+ Run the main script: python main.py
+ Configure the desired parameters, such as threshold values or camera settings, in the configuration file (if applicable).
+ Start the exam or monitoring session.
+ Monitor the output and warnings in the console or user interface.
+ Analyze the behavior graph and cheat percentile to identify suspicious activities.
+ Customize or extend the system according to your needs.
