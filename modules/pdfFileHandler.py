import os
import re

# Global Variable COUNT - to keep track of files as they are found
count = 0
directory = "report/pdf/"


# Folder Creator For PDF Files
def directory_create():
    if not os.path.exists(directory):
        os.makedirs(directory)


# Create Image Files with the Data Given
def file_create(data):
    directory_create()
    filename = directory+"pdf"+str(count)+".pdf"
    pdf_file_created = open(filename, 'wb')
    pdf_file_created.write(data)
    pdf_file_created.close()


# Magic Numbers for Images
pdf_data = {"pdf": {"start":"25504446","end":"25454f460d"}}


# Extract Image Files
def file_extraction(data):
    for key,value in pdf_data.iteritems():
        print ("Searching for %s files..." % key)
        regex_string = r"("+re.escape(value["start"])+r".+?"+re.escape(value["end"])+r".+?"+re.escape(value["end"])+r")"
        pdfs_snatched = re.findall(regex_string, data.encode('hex'))
        if pdfs_snatched:
            for snatches in pdfs_snatched:
                global count
                count = count + 1
                try:
                    file_create(snatches.decode('hex'))
                except:
                    pass
