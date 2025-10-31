# import requests
# import pypdf
# import io
# import re
# import array
# import pytesseract
# from pdf2image import convert_from_bytes
# # from PIL import Image

# #step 1: Download the PDF from URL
# # url = "https://erpproject.blr1.digitaloceanspaces.com/uat/motor_datasheet/20250402164742_1743592662_20250106194250_1736172770_4103_202501060322090.pdf"
# url = "https://claim.blr1.digitaloceanspaces.com/live/cashless_claim/live/cashless_claim/1830/6819e9652f34f.pdf"
# url1 = "https://claim.blr1.digitaloceanspaces.com/live/cashless_claim/live/cashless_claim/1829/6819e9651688f.pdf"
# # url2 = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
# # https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf
# response = requests.get(url)
# response1 = requests.get(url1)
# # response2 = requests.get(url2)
# # print(response2)

# if response.status_code == 200:                               #perfect1
#     pdf_file = io.BytesIO(response.content)
#     reader = pypdf.PdfReader(pdf_file)
#     text = ""

#     for page in reader.pages:
#         text += page.extract_text() + "\n"
#         # print(text)
#         pattern = r"(Total\s*bill amount \(INR\))\s*(\d+)"
#         pattern1 = r"(Other\s*Deductions\(INR\)\*)\s*(\d+)"
#         pattern2 = r"(Copay\s*\(INR\))\s*(\d+)"
#         pattern3 = r"(Hospital\s*Discount\s*\(INR\))\s*(\d+)"
#         pattern6 = r"(Deductibles\s*\(INR\))\s*(\d+)"
#         pattern4 = r"(Total\s*Authorized\s*Amount\(INR\))\s*(\d+)"
#         # pattern5 = r"(^Amount\s*.*)\s(\d+)" the another correct one
#         pattern5 = r"(Amount\s*to\s*be\s*paid\s*by\s*Insured\s*\(INR\))\s*(\d+)"
#         value = re.findall(pattern, text)[0]
#         value1 =  re.findall(pattern1, text)[0]
#         value2 = re.findall(pattern2, text)[0]
#         value3 = re.findall(pattern3, text)[0]
#         value4 = re.findall(pattern4, text)[0]
#         value5 = re.findall(pattern5, text, re.MULTILINE)
#         value6 = re.findall(pattern6, text)[0]
#     # print(value)
#     # print(value1)                                              #end1
#     # print(value2)
# results = {}
# results[value[0]] = value[1]
# results[value1[0]] = value1[1]
# results[value2[0]] = value2[1]
# results[value3[0]] = value3[1]
# results[value6[0]] = value6[1]
# results[value4[0]] = value4[1]
# results[value5[0][0]] = value5[0][1]
# # print(results)
    
# if response1.status_code == 200:
#     pdf_file = io.BytesIO(response1.content)
#     reader = pypdf.PdfReader(pdf_file)
#     text1 = ""

#     for page in reader.pages:
#         text1 += page.extract_text() + "\n"
#         # print(text1)
#         re_pattern = r"(\(LESS.*)\s(\d+)"
#         new_text = r"(Net.*)\s(\d+)"
#         new_pattern = r"85958\s*(\d+)(.\w.*)"
#         new_pattern1 = r"(Total)\s*(\d+)"
#         find = re.findall(re_pattern, text1)
#         new_text_value = re.findall(new_text, text1)
#         new_text_pattern = re.findall(new_pattern, text1)
#         # print(new_text_pattern)
#         new_text_pattern1 = re.findall(new_pattern1, text1)
# output = {}
# output[find[0][0]] = find[0][1]
# output[find[1][0]] = find[1][1]
# output[find[2][0]] = find[2][1]
# output[find[3][0]] = find[3][1]
# output[new_text_value[0][0]] = new_text_value[0][1]
# output[new_text_pattern[0][1]] = new_text_pattern[0][0]
# output[new_text_pattern1[0][0]] = new_text_pattern1[0][1]
# # print(output)

# final_output = []

# copay_subtraction = int(value2[1]) - int(find[1][1])
# deduction_subtraction = int(value1[1]) - int(new_text_pattern[0][0])
# hospital_subtraction = int(value3[1]) - int(find[2][1])
# total_bill_amount = int(value[1])
# net_amount = int(new_text_value[0][1])
# tax_deducted = int(find[3][1])
# disclosed = total_bill_amount - (net_amount + tax_deducted)

# final_output.append(f"Copay : {copay_subtraction}")
# final_output.append(f"Other_deductions : {deduction_subtraction}")
# final_output.append(f"Hospital Discount : {hospital_subtraction}")
# final_output.append(f"Total Bill Amount : {total_bill_amount}")
# final_output.append(f"Net Amount Recommended For Payment : {net_amount}")
# final_output.append(f"Tax Deducted at Source : {tax_deducted}")
# final_output.append(f"Disclosed Amount: {disclosed}")

# # print(final_output)

# # if response2.status_code == 200:
# #     pdf_file = io.BytesIO(response2.content)
# #     reader = pypdf.PdfReader("C:/Users/User/Downloads/claim.pdf")
# #     # reader = pypdf.PdfReader(pdf_file)
# #     text2 = ""

# #     # for page in reader.pages:
# #     #     text2 += page.extract_text() + "\n"
# #     #     # print(text2)

# #     #     from pypdf import PdfReader

# #     # for i, page in enumerate(reader.pages):
# #     #     text = page.extract_text()
# #     #     # print(f"--- Page {i+1} ---")
# #     #     # print(text)
# #     for i, page in enumerate(reader.pages):
# #         text = page.extract_text()
# #         if text:
# #             text2 += f"\n--- Page {i+1} ---\n" + text
# #         else:
# #             text2 += f"\n--- Page {i+1} ---\n[No extractable text]"
# #     print(text2)

# from pdf2image import convert_from_bytes
# import requests
# import pytesseract
# from io import BytesIO

# url2 = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
# response = requests.get(url2)
# pdf_content  = response.content
# pdfstream = BytesIO(pdf_content)

# if response.status_code == 200:
#     pdfstream.seek(0)
#     images = convert_from_bytes(pdfstream.read(), dpi = 300)  # now this should work
#     for i, image in enumerate(images):
#         text = pytesseract.image_to_string(image)
#         print(f"\n--- Page {i+1} ---\n{text}")

# from pdf2image import convert_from_bytes
# import requests
# import pytesseract


# url2 = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
# response = requests.get(url2)

# if response.status_code == 200:
#     pdf_content = response.content
#     images = convert_from_bytes(pdf_content, dpi=400)  # Converts each PDF page to image
#     text2 = ""
#     for i, image in enumerate(images):
#         text = pytesseract.image_to_string(image)
#         text2 += text
#         print(f"\n--- Page {i+1} ---\n{text2}")
#     print(text2)
# else:
#     print(f"Failed to download PDF. Status code: {response.status_code}")

import requests
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image, ImageEnhance
import re

url2 = "https://claim.blr1.digitaloceanspaces.com/demo/cashless_claim/demo/cashless_claim/1233/687a28bbcacd6.pdf"
# https://claim.blr1.digitaloceanspaces.com/live/cashless_claim/live/cashless_claim/3771/687a261116cfe.pdf
response = requests.get(url2)

if response.status_code == 200:
    pdf_content = response.content
    images = convert_from_bytes(pdf_content, dpi=400)

    # full_text = ""

    for i, image in enumerate(images):
        # Optional: preprocess image (convert to grayscale and enhance)
        gray = image.convert("L")
        enhancer = ImageEnhance.Contrast(gray)
        enhanced_image = enhancer.enhance(2.0)

        # OCR with custom config
        text = pytesseract.image_to_string(enhanced_image, config='--oem 3 --psm 6')
        # full_text += text
        # print(full_text)
        print(f"\n--- Page {i+1} ---\n{text}")

    # Search for valid policy number using regex
    # matches = re.search(r'(BILL\sNO\s.)(.\w.*)', full_text)
    # matches1 = re.search(r'(IP\sNo.\s.)(.\d.{11})', full_text)
    # if matches or matches1:
    #     print(matches)
    #     print(matches1)
    # else:
    #     print("\n No valid policy number found.")
else:
    print(f"❌ Failed to download PDF. Status code: {response.status_code}")

