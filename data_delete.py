import os
from os import listdir

  # annotation 파일 경로
data_dir = 'C:/data/dataset/'
anno_dir = 'C:/data/annotations/'


for file in listdir(data_dir):
    path = anno_dir + file.replace(file.split('.')[-1], 'xml')

    try:
        fr = open(path, 'r')
        fr.close()

    except:
        path = data_dir + file
        print('----------------------------------')
        print('delete : ', path)
        jpgfile = path
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
            print(" jpg delete")
            print('----------------------------------')



for file in listdir(anno_dir):
    path = data_dir + file.replace(file.split('.')[-1], 'jpg')

    try:
        fr = open(path, 'r')
        fr.close()

    except:
        path = anno_dir + file
        print('----------------------------------')
        print('delete : ', path)
        jpgfile = path
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
            print(" xml delete")
            print('----------------------------------')