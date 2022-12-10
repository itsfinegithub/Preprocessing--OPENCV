import os
import glob
import cv2
from zipfile import ZipFile
import shutil


def unzip():
    with ZipFile("path", 'r') as zip_ref:
        zip_ref.extractall('dest_path')


    folders = []
    for i in glob.glob('path of the folder which contain 4 subfolders'):
        F = i.spilt('/')[-1]
        folders.append(F)

    for i in folders:
        os.makedirs(f'folder_name/{i}')

    for images in glob.glob('path of the folders which contain images'):
        images = cv2.imread(images)
        resized = cv2.resize(images,(224,224))
        k = images.split('/')[1]
        s = images.split('/')[-1]

        if k in images:
            cv2.imwrite(f'new folder/{k}{s}',resized)

    shutil.make_archive('outputfolder','zip','outputfolder')
if __name__ == "__main__":
    unzip

