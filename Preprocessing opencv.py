import os
import glob
import cv2
from zipfile import ZipFile
import shutil

# the function which will unzip the file
def unzip():
    with ZipFile("path", 'r') as zip_ref:
        zip_ref.extractall('dest_path')

    # here I am extrcating the sub-folders name from the main folder 
    folders = []
    
    # glob module helps to retrive all the path of the files
    for i in glob.glob('path of the folder which contain 4 subfolders/*/*'):
        
        #here I am splitting the path,taking last index because i want subfolders name
        F = i.spilt('/')[-1]
        
        #appending all the folders name into list
        folders.append(F)

        #creating directory for all subfolders in one  main folder
    for i in folders:
        os.makedirs(f'folder_name/{i}')

        #data preprocessing,extracting all  the files from folder
    for images in glob.glob('path of the folders which contain images/*/*'):
        
        #reading the images using opencv. it will return numpy array of the image
        images = cv2.imread(images)
        
        #resizing the image
        resized = cv2.resize(images,(224,224))
        k = images.split('/')[1]
        s = images.split('/')[-1]
        
        # after preprocessing write all the images to new folders based on their folder name using opencv imwrite function
        if k in images:
            cv2.imwrite(f'new folder/{k}{s}',resized)

    # shutil module help to zipping the file
    shutil.make_archive('outputfolder','zip','outputfolder')
if __name__ == "__main__":
    unzip

