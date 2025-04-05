import PyPDF2

file_path = r'C:\Users\raksi\OneDrive\Desktop\PRINCPLE OF PROGRAMMING LANGUAGE.pdf'

with open(file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()

    print(text)
