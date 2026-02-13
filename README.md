🚗 AI-Powered Automatic License Plate Recognition (ALPR)

An end-to-end Automatic License Plate Recognition (ALPR) system built using OpenCV, Tesseract OCR, and Streamlit.
This application detects vehicle license plates from images and extracts the plate number using Optical Character Recognition (OCR).

📌 Project Overview

- This project uses Computer Vision techniques to:

- Detect vehicle license plates

- Extract text using OCR

- Display results through a Streamlit web interface

- Provide an easy-to-use browser-based experience


🛠️ Tech Stack

- Python 3.13

- OpenCV – Image processing & contour detection

- Tesseract OCR – Text extraction

- Pytesseract – Python wrapper for Tesseract

- Streamlit – Web app interface

- NumPy


⚙️ How It Works

- Upload vehicle image

- Convert image to grayscale

- Apply bilateral filtering (noise reduction)

- Perform edge detection using Canny

- Detect contours

- Identify 4-point contour (license plate)

- Crop plate region

- Extract text using Tesseract OCR

- Display detected license number


📷 Application Demo

- Upload an image and the system:

- Detects the license plate

- Draws bounding box

- Extracts and displays plate text


🧠 Future Improvements

- Deep Learning based plate detection (YOLO)

- Real-time video processing

- Cloud deployment

- Multi-language OCR support

- Improved preprocessing for higher accuracy


🎯 Use Cases

- Traffic monitoring systems

- Smart parking systems

- Toll booth automation

- Security surveillance

- Law enforcement systems



Imutils

Pillow
