# 11 metacharacteres in regular expression 
import requests
import pypdf
import io
import re

url="https://erpproject.blr1.digitaloceanspaces.com/uat/motor_datasheet/20250402164742_1743592662_20250106194250_1736172770_4103_202501060322090.pdf"
response = requests.get(url)

if response.status_code == 200:
    pdf_file = io.BytesIO(response.content)
    reader = pypdf.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        x = re.search("IP Address",text)
        print(x.group())
