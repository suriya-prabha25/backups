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

    search_text = "REQUEST FOR CASHLESS HOSPITALISATION"
    found_page = None

    for page_no, text in enumerate(images):
        # Optional: preprocess image (convert to grayscale and enhance)
        gray = text.convert("L")
        enhancer = ImageEnhance.Contrast(gray)
        enhanced_image = enhancer.enhance(2.0)

        # OCR with custom config
        
        text = pytesseract.image_to_string(enhanced_image, config='--oem 3 --psm 6')

        if search_text in text:
            found_page = page_no
            break  # Stops at the first match
    if found_page:
        print(f"'{search_text}' found on page {found_page}")
    else:
        print(f"'{search_text}' not found in any page.")
