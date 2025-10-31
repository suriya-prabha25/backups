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

    # found_request_page = ""
    approval_page = ""
    patient_id_page = ""
    discharge_summary_page = ""
    credit_bill_page = ""
    hospital_page = ""
    # full_text = []

    for i, image in enumerate(images):
        # Preprocess image
        gray = image.convert("L")
        enhancer = ImageEnhance.Contrast(gray)
        enhanced_image = enhancer.enhance(2.0)

        # OCR
        text = pytesseract.image_to_string(enhanced_image, config='--oem 3 --psm 6')
        # print(i)
        # page_number = i + 1  # Convert to human-readable page
        # print(page_number)
        if approval_page == "" and 'APPROVAL' in text:
            approval_page = page_number

        if patient_id_page == "" and 'PERSONAL DETAILS' in text:
            print("inside2")
            patient_id_page = page_number

        if discharge_summary_page == "" and 'DISCHARGE SUMMARY' in text:
            print("inside3")
            discharge_summary_page = page_number

        if credit_bill_page == "" and 'CREDIT BILL' in text:
            print("inside4")
            credit_bill_page = page_number


        if hospital_page == "" and 'CASHLESS HOSPITALISATION FOR HEALTH INSURANCE POLICY' in text:
            print("inside5")
            if hospital_page is not None:
                hospital_page = page_number


    # Print all
    # if found_request_page:
    #     print(f"'REQUEST FOR CASHLESS HOSPITALISATION' found on page {found_request_page}")
    # else:
    #     print(f"'REQUEST FOR CASHLESS HOSPITALISATION' not found in any page.")

    print("Approval Letter        :", approval_page or "Not found")
    print("Patient ID             :", patient_id_page or "Not found")
    print("Discharge Summary      :", discharge_summary_page or "Not found")
    print("Credit Bill            :", credit_bill_page or "Not found")
    print("Hospital Page          :", hospital_page or "Not found")

    
    #     full_text += text + "\n"
    # print("Approval Letter Page from 1 to 3:", full_text)
        # for texts in enumerate(text):
            # print(texts)
            # complete_text += texts
            # if texts == 'Medi Assist REQUEST FOR CASHLESS HOSPITALISATION':
                # print(complete_text)
