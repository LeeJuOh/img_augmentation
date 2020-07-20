from xml.etree.ElementTree import parse
import os
fileName = "label_pet_"
fileName2 = "label_pet_"
folder_path = "C:/data/annotations/"  # annotation 파일 경로


for i in range(0, 15000) :
    try:
        file_path = folder_path + fileName + str(i) + '.xml'
        tree = parse(file_path)
        root = tree.getroot()
        object = root.find('object')
        if object is None:

            xml_file = file_path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(i,' xml delete')
        else:
            continue;

    except FileNotFoundError:
        continue;


for i in range(0, 1500) :
    try:
        file_path = folder_path + fileName + str(i) + '_ko.xml'
        tree = parse(file_path)
        root = tree.getroot()
        object = root.find('object')
        if object is None:

            xml_file = file_path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(i,' xml delete')
        else:
            continue;

    except FileNotFoundError:
        continue;


for i in range(0, 1500) :
    try:
        file_path = folder_path + fileName2 + "n_" +  str(i) + '.xml'
        tree = parse(file_path)
        root = tree.getroot()
        object = root.find('object')
        if object is None:
            print('garbage')
            xml_file = file_path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(i,' n xml delete')
        else:
            continue;

    except FileNotFoundError:
        continue;

for i in range(0, 1500) :
    try:
        file_path = folder_path + fileName2 + "n_ko_" +  str(i) + '.xml'
        tree = parse(file_path)
        root = tree.getroot()
        object = root.find('object')
        if object is None:
            print('garbage')
            xml_file = file_path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(i,' n xml delete')
        else:
            continue;

    except FileNotFoundError:
        continue;