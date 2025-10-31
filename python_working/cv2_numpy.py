import requests
import cv2
import numpy as np
from pdf2image import convert_from_bytes
import pytesseract
import re

url = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
response = requests.get(url)

if response.status_code == 200:
    pdf_content = response.content
    images = convert_from_bytes(pdf_content, dpi=400)

    full_text = ""

    for i, image in enumerate(images):
        # Convert PIL image to OpenCV format (numpy array)
        open_cv_image = np.array(image)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

        # Convert to grayscale
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to make text more clear
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Optionally resize for better OCR accuracy
        resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # OCR with whitelist
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/:'
        text = pytesseract.image_to_string(resized, config=custom_config)

        full_text += text

        print(full_text)

else:
    print(f"❌ Failed to download PDF. Status code: {response.status_code}")