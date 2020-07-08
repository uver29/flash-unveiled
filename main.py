# Run with Python version 2
import os
import sys

# Custom Module Import
sys.path.insert(0, 'modules/')
import imageFileHandler
import pdfFileHandler

# Multiple Files Reception from the Arguments
if len(sys.argv) < 2:
    print ("Enter the Disk Image file\n")
    sys.exit()

# Report Folder Creation
directory = "report"
if not os.path.exists(directory):
    os.makedirs(directory)

# Argument Fetching
dd_image_name = sys.argv[1]
with open(dd_image_name, 'rb') as dd_image:

    to_continue = 1
    while to_continue:
        dd_image_contents = dd_image.read(10000000)

        imageFileHandler.file_extraction(dd_image_contents)
        pdfFileHandler.file_extraction(dd_image_contents)
        
        to_continue = input("1 to continue, 0 to exit ")
