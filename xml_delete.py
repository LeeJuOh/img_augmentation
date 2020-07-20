from xml.etree.ElementTree import parse
import os
  # annotation 파일 경로
anno_dir = 'C:/data/nolle/annotations/'

from os import listdir

for file in listdir(anno_dir):
    try:

        path = anno_dir +file
        tree = parse(path)
        root = tree.getroot()
        object = root.find('object')
        if object is None:

            xml_file = path
            if os.path.isfile(path):
                os.remove(path)
                print('-------------------------------------')
                print(file, ' xml delete')
                print('-------------------------------------')
        else:
            continue;

    except FileNotFoundError:
        continue;


