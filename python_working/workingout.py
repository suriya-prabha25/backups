import requests
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image, ImageEnhance
import re

url2 = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
response = requests.get(url2)

if response.status_code == 200:
    pdf_content = response.content
    images = convert_from_bytes(pdf_content, dpi=400)

    approval_page = ""
    full_text = []

    for i, image in enumerate(images):
        # Preprocess image
        gray = image.convert("L")
        enhancer = ImageEnhance.Contrast(gray)
        enhanced_image = enhancer.enhance(2.0)

        # OCR
        text = pytesseract.image_to_string(enhanced_image, config='--oem 3 --psm 6')
        full_text.append(text)

        # Case-insensitive search for 'APPROVAL' in full_text list
approval_index = next(
    (i for i, text in enumerate(full_text) if 'APPROVAL' in text),
    None
)

if approval_index is not None:
    approval_page = approval_index + 1  # Convert to human-readable page number
    print(f"'APPROVAL' found on page {approval_page}")
else:
    print("'APPROVAL' not found in any page")
