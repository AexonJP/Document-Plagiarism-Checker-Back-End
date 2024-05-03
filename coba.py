# Import the required modules\
try:
    import docx2txt
    from pdf2docx import Converter
    import glob
except:
    import os
    os.system('pip install pdf2docx')
    os.system('pip install docx2txt')

def convert_pdf(pdf_file):
    
    
    # Keeping the PDF's location in a separate variable
    # pdf_file = "C:/Users/ADMIN/Desktop/serverNode/Delfan Rynaldo Laden - 1915016069.pdf"
    
    # Maintaining the Document's path in a separate variable
    docx_file = (pdf_file[:-4]+'.docx')
    
    # Using the built-in function, convert the PDF file to a document file by saving it in a variable.
    cv = Converter(pdf_file)
    
    # Storing the Document in the variable's initialised path
    cv.convert(docx_file)
    
    # Conversion closure through the function close()
    cv.close()

def convert_docx(docx_file):
    

    directory = glob.glob(docx_file)

    for file_name in directory:
        with open(file_name, 'rb') as infile:
            with open(file_name[:-5]+'.txt', 'w', encoding='utf-8') as outfile:
                doc = docx2txt.process(infile)
                outfile.write(doc)
    print("=========")
    print("All done!")

def pdf_to_text(pdf_file):
    hasil = []
    convert_pdf(pdf_file)
    docx_file = (pdf_file[:-4]+'.docx')
    convert_docx(docx_file)
    # okeh = False
    with open(docx_file[:-5]+'.txt', mode='r', encoding="utf-8") as f:
        # print((f.read()).replace('\t',''))
        opl = f.readlines()
        # if(i)
        for i in opl :
            if(len(i) > 20):
                if("...." not in i):
                    i= i.replace('\t','')
                    hasil.append(i)
    return hasil
        # print(f"ada sebanyak {len(opl)}")

def preprocessing(file_pdf):
    oke = pdf_to_text(file_pdf)
    # print(len(oke))
    ole = ""
    for i in oke:
        # print(i)
        ole = ole + i +" "

    with open(f"{file_pdf[:-4]} - preprocessing.txt", "w", encoding="utf-8") as f:
        f.write(ole.replace("  ", ""))
    
    return file_pdf[:-4] +' - preprocessing.txt'



# file_pdf = r"C:\Users\ADMIN\Desktop\serverNode\Proposal_Skripsi_abdullah.pdf"

# preprocessing(file_pdf)