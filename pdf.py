import PyPDF2
import sys


# with open("./dummy.pdf", "rb") as file:  # rb is read in binary
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)  # 1
#     # print(reader.getPage(0))
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("tilt.pdf", "wb") as new_file:
#         writer.write(new_file)


# Merging PDFs
# inputs = sys.argv[1:]


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()

#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write("super.pdf")


# pdf_combiner(inputs)


# Watermarking PDFs

# read the input file
# read the wtrmrk file
with open("./super.pdf", "rb") as super_file, open("./wtr.pdf", "rb") as watermark:

    read_super = PyPDF2.PdfFileReader(super_file)
    read_wtr = PyPDF2.PdfFileReader(watermark)
    watermark_page = read_wtr.getPage(0)

    out_writer = PyPDF2.PdfFileWriter()

    # for each page in the input file, mergePage the wtrmark page
    for idx in range(read_super.numPages):
        cur_page = read_super.getPage(idx)
        cur_page.mergePage(watermark_page)
        out_writer.addPage(cur_page)
    with open("./watermarked_super.pdf", "wb") as merged_file:
        out_writer.write(merged_file)
