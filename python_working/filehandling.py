# myfile = open("newfile3.txt","x")
# with open("newfile.txt","w") as file:
#     file.write("Hello,i successfully created a new file.\n")
#     file.write("Hello i am a new and first content of this file.\n")

# # print("File created and written successfully!")
# contentappend = open("newfile.txt","a")
# contentappend.write("This is a appended message")
# contentappend.close()

# file = open("newfile.txt","r")
# for line in file:
#     print(line.strip())
# # content = file.read()
# # print(content)
# file.close()

# file = open("newfile.txt","rb")    #reading a file in binary format
# content = file.read()
# print(content)
# file.close()

# file = open("newfile.txt","r")    #reading specific parts of a file
# content = file.read(15)     #reading the first N Bytes
# print(content)
# file.close()

# with open("example.bin","rb") as file:
#     binary_data = file.read()       #reading a binary file entirely
#     print(binary_data)

# with open("large_file.bin","rb") as file:
#     while chunk := file.read(1024):     #reading a binary file in chunks
#         print(chunk)                    #for large files,reading in chunks is more memory-efficient.

# import requests

# url = "https://erpproject.blr1.digitaloceanspaces.com/uat/motor_datasheet/20250402164742_1743592662_20250106194250_1736172770_4103_202501060322090.pdf"

# response = requests.get(url)

# if response.status_code == 200:
#     with open("downloaded_file.pdf", "") as file:
#         file.write(response.content)  # Save the file locally

#     print("File downloaded successfully!")
# else:
#     print("Failed to download the file. HTTP Status Code:", response.status_code)

# import requests
# import pypdf  # Updated import
# import io

# # URL of the PDF
# url = "https://erpproject.blr1.digitaloceanspaces.com/uat/motor_datasheet/20250402164742_1743592662_20250106194250_1736172770_4103_202501060322090.pdf"

# response = requests.get(url)

# if response.status_code == 200:
#     pdf_file = io.BytesIO(response.content)  # Convert response to a file-like object
#     reader = pypdf.PdfReader(pdf_file)  # Use pypdf instead of PyPDF2

#     for page in reader.pages:
#         print(page.extract_text())  # Extract text from each page
# else:
#     print("Failed to download the PDF")


import requests
import pypdf
import io

# Step 1: Download the PDF from URL
url = "https://erpproject.blr1.digitaloceanspaces.com/uat/motor_datasheet/20250402164742_1743592662_20250106194250_1736172770_4103_202501060322090.pdf"
response = requests.get(url)

if response.status_code == 200:
    # Step 2: Convert to a file-like object
    pdf_file = io.BytesIO(response.content)
    reader = pypdf.PdfReader(pdf_file)
    print("AS",pdf_file)
    # Step 3: Extract text from all pages
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + "\n"
    #print(text)
    # Step 4: Search for a specific word (e.g., "Policy Number")
    search_word = "Name of Insured"
    extracted_text = None

    for line in text.split("\n"):
        if search_word in line:
            extracted_text = line.split(search_word)[-1].strip()  # Extract text after the keyword
            break  # Stop after finding the first match

    # Step 5: Display the extracted text
    if extracted_text:
        print(f"Name of Insured: {extracted_text}")
    else:
        print(f"'{search_word}' not found in the PDF")

else:
    print("Failed to download the PDF")