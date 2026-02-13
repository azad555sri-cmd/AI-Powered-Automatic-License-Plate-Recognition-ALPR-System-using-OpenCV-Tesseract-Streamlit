import streamlit as st
import cv2
import numpy as np
import imutils
import pytesseract
from PIL import Image

# Set Tesseract path (CHANGE if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("🚗 License Plate Detection & OCR")

uploaded_file = st.file_uploader("Upload a vehicle image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV format
    image = Image.open(uploaded_file)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_column_width=True)

    # Resize
    image = imutils.resize(image, width=600)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise reduction
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Edge detection
    edged = cv2.Canny(gray, 30, 200)

    # Find contours
    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

    screenCnt = None

    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is not None:
        # Draw contour
        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)

        # Crop detected plate
        x, y, w, h = cv2.boundingRect(screenCnt)
        plate = gray[y:y+h, x:x+w]

        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Detected License Plate", use_column_width=True)
        st.image(plate, caption="Cropped Plate", use_column_width=True)

        # OCR
        text = pytesseract.image_to_string(plate, config='--psm 8')

        st.success(f"Detected Text: {text.strip()}")

    else:
        st.error("No License Plate Detected")
