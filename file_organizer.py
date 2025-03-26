import os
import shutil
import shutil as sh
path = r"FOLDER LOCATION/"

print(os.listdir(path))
file_name = os.listdir(path)
#setting folder names

folder_names = ["png_files","image_files","pdf_files","shortcut_files","documents_files","zip_files","mlt_files"]

#creating temporary values

count = 0

#counting the total numbers of files

for folder in folder_names:
    count +=1
print(count)

#creating folders and moving the files according to the extensions


for i in range(0,count):
    if not os.path.exists(path + folder_names[i]):
        os.makedirs(path + folder_names[i])

#moving the files according to the extensions

for file in file_name:
    if ".pdf" in file and not os.path.exists(path + f"{folder_names[2]}/" + file):
        shutil.move(path + file,path + f"{folder_names[2]}/" )
    elif ".jpg" in file or ".jpeg" in  file and not os.path.exists(path + f"{folder_names[1]}/" + file):
        shutil.move(path + file,path + f"{folder_names[1]}/" )
    elif ".png" in file and not os.path.exists(path + f"{folder_names[0]}/" + file):
        shutil.move(path + file,path + f"{folder_names[0]}/" )
    elif ".link" in file and not os.path.exists(path + f"{folder_names[3]}/" + file):
        shutil.move(path + file,path + f"{folder_names[3]}/" )
    elif ".zip" in file and not os.path.exists(path + f"{folder_names[5]}/" + file):
        shutil.move(path + file,path + f"{folder_names[5]}/" )
    elif ".mlt" in file and not os.path.exists(path + f"{folder_names[6]}/" + file):
        shutil.move(path + file,path + f"{folder_names[6]}/" )
    elif ".docx" in file and not os.path.exists(path + f"{folder_names[4]}/" + file):
        shutil.move(path + file,path + f"{folder_names[4]}/" )






