import os
from pypdf import PdfWriter, PdfReader

def crop_files(input, output):
    files = os.listdir(input)
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        # name = os.path.splitext(file_name)[0]
        if file_extension == ".pdf":
            try:
                inp_path = os.path.join(input, file_name)
                exp_path = f"{output}/{file_name}"
                print(inp_path, exp_path)
                with open(inp_path, "rb") as in_f:
                    pdfinput = PdfReader(in_f)
                    pdfoutput = PdfWriter()

                    numPages = len(list (pdfinput.pages))
                    print(numPages)

                    for i in range(numPages):
                        page = pdfinput.pages[i]
                        print(page.mediabox.upper_left, page.mediabox.upper_right)
                        page.trimbox.lower_left = (0, 0)
                        page.trimbox.upper_right = (0, 0)
                        page.cropbox.lower_left = (80, 150)
                        page.cropbox.upper_right = (525, 725)
                        pdfoutput.add_page(page)

                with open(exp_path, "wb") as out_f:
                    pdfoutput.write(out_f)

            except Exception as e:
                print(exp_path)
                print(e)

crop_files("input", "output")    