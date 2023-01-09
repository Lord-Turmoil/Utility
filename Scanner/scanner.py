import os
from time import sleep
from fpdf import FPDF

ret = str

def search_images(path):
    """
    Search all images, just directory.
    """

    image_list = []
    print("Searching...")
    for img in os.listdir(path):
        if (img[-3:] == "jpg") or (img[-3:] == "png"):
            image_list.append(img)
    if len(image_list) != 0:
        print("Search Complete!")
        print("Images to convert:")
        image_list.sort()
        for image in image_list:
            print(f"\t {image}")
    else:
        print("No image!")

    return image_list


def create_pdf():
    pdf = FPDF()
    pdf.set_creator("Tony's Studio")
    pdf.set_auto_page_break(False)

    return pdf


def convert_pdf(path, filename, image_list):
    """
    Convert all images to PDF.
    """

    if len(image_list) == 0:
        return

    print("Converting...")

    pdf = create_pdf()
    for img_dir in image_list:
        pdf.add_page()
        pdf.image(os.path.join(path, img_dir), x = 0, y = 10, w = 210)
    pdf.output(os.path.join(path, filename), "F")
    pdf.close()
    print("Conversion Complete!\n")


while True:
    print("------------- Copyright(C) Tony's Studio -------------")
    print("----------------- Image to PDF 1.1.0 -----------------")
    print("-------------- Only support jpg and png --------------")

    # Read source folder.
    path = input("Please enter the source folder(\"q\" to quit): ").strip()
    if path == "q":
        break

    # Read file name.
    filename = input("Please enter the target filename(\"q\" to quit): ").strip()
    if filename == "q":
        break
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    # Search and convert.
    convert_pdf(path, filename, search_images(path))
        
    ret = input("Continue? (Y/N) ").lower()
    if ret[0] != 'y':
        break
    os.system("cls")

print("Thanks for your using!")
sleep(0.8)