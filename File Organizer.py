#Code Written By Yogesh Kalmodiya

import os
import shutil

import pathlib

fileFormat = {

    "Picture": [".jpeg", ".jpg", ".png"],

    "video": [".avi", ".mkv", ".flv", ".mp4", ".webm"],

    "Document": [".txt", ".pdf", ".doc", ".docx", ".xls"],

    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar"]

}

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

print(fileFormats)
print(fileTypes)

for file in os.scandir():
    fileName = pathlib.Path(file)
    fileFormatType = fileName.suffix.lower()

    src = str(fileName)
    dest = "Other"
    if fileFormatType == "":
        print(f" {src} Has not File Format")
    else:
        for formats in fileFormats:
            if fileFormatType in formats:
                Folder = fileTypes[fileFormats.index(formats)]
                print(Folder)
                if os.path.isdir(Folder) == False:
                    os.mkdir(Folder)
                    dest = Folder
            else:
                if os.path.isdir("Other") == False:
                    os.mkdir("Other")

        print(src, "moved to ", dest, " ! ")
        shutil.move(src, dest)

    print("File organizer Started")
    input("\n Press enter to Exit")


