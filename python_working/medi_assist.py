import requests
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image, ImageEnhance
import re

url = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
response = requests.get(url)

if response.status_code == 200:
    pdf_content = response.content
    images = convert_from_bytes(pdf_content, dpi=400)

    full_text = ""

    for i, image in enumerate(images):
        gray_scale = image.convert("L")
        enhancer = ImageEnhance.Contrast(gray_scale)
        enhanced_image = enhancer.enhance(2.0)

        # OCR with custom config
        text = pytesseract.image_to_string(enhanced_image, config='--oem 3 --psm 6')
        full_text += text
        # print(full_text)
        pattern1 = re.findall(r'(BILL\sNO)\s.(.\w.*)',full_text)     #Bill No
        pattern2 = re.findall(r'Cashless.*.\w*\s.(\d+)',full_text)   #CCN
        pattern3 = re.findall(r'Medi.*\s(\d+)',full_text)            #MAID NO
        pattern4 = re.findall(r'Name\s(\w*\s\w{5}\s.)',full_text)    #Patient Name
        pattern5 = re.findall(r'IP\sNo.\s.\s(\w*)',full_text)        #IP No
        pattern6 = re.findall(r'(UHID\s.\s)(.\w*)',full_text)        #UHID
        pattern7 = re.findall(r'(D.O.A.\s:.)(.+)',full_text)         #D.O.A
        pattern8 = re.findall(r'(D.O.D.\s:.)(.+)',full_text)         #D.O.D    same as Bill Date

        pattern9 = re.findall(r'(CLAIM.\w*.:)(.\d+)',full_text)      #CLAIM NO
        pattern10 = re.findall(r'(INS\s.\w*\s:.)(.\w*\s.\w*.\W.\w*\s\w*)',full_text)        #INS NAME
        pattern11 = re.findall(r'authorize\s.\w*.(\d+)',full_text)      #Authorized Amount
        pattern12 = re.findall(r'Day.\d.\W(\d+.\d*.\d*)\W.\s',full_text)        #Bill Received Date
        pattern13 = re.findall(r'bill\s.\w*.\w*.(\d+)',full_text)       #Gross Bill Amount
        pattern14 = re.findall(r'1.(Med\w*\s\w*)',full_text)        #Hospital Name
        pattern15 = re.findall(r'Holder.(.\w*.of\s\w*.\w*.\w*.\w*)',full_text)      #Corporate Name
        pattern16 = re.findall(r'(United\s.\w*.\w*.Co.\s\w*)',full_text)        #Insurance Company Name
        pattern17 = re.findall(r'insured\s\W.\w*\W.(\d+)',full_text)        #Cash Received same as NM/NP and Total

        output = {}
        if pattern1:
            # print(pattern1)
            output[pattern1[0][0]] = pattern1[0][1]
            # result = output.append(f"Bill No : {pattern1}")
            # print(output)
