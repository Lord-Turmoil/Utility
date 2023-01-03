import os
from time import sleep
from fpdf import FPDF

ret = str

def search_images(path):
    ''' Search all images, just directory. '''

    imageList = []
    print("Searching...")
    for img in os.listdir(path):
        if (img[-3:] == "jpg") or (img[-3:] == "png"):
            imageList.append(img)
    if len(imageList) != 0:
        print("Search Complete!")
        print("Images to convert:")
        imageList.sort()
        for dir in imageList:
            print(f"\t {dir}")
    else:
        print("No image!")

    return imageList

def convert_pdf(path, filename, imageList):
    ''' Convert all images to PDF. '''

    print("Converting...")
    pdf = FPDF()
    pdf.set_creator("Tony's Studio")
    pdf.set_auto_page_break(False)
    for dir in imageList:
        pdf.add_page()
        pdf.image(os.path.join(path, dir), x = 0, y = 10, w = 210)
    pdf.output(os.path.join(path, filename), "F")
    pdf.close()
    print("Convertion Complete!\n")

while True:
    print("------------- Copyright(C) Tony's Studio -------------")
    print("----------------- Image to PDF 1.1.0 -----------------")
    print("-------------- Only support jpg and png --------------\n")

    # Read folder and filename.
    path = input("Please enter the source folder: ").strip()
    if path == "quit":
        break
    filename = input("Please enter the target filename: ").strip()
    if filename == "quit":
        break
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    
    # Search images
    imageList = search_images(path)
    if len(imageList) != 0:
        convert_pdf(path, filename, imageList)
        
    ret = input("Continue? (Y/N) ").lower()
    if ret[0] != 'y':
        break
    os.system("cls")

print("Thanks for your using!")
sleep(0.8)