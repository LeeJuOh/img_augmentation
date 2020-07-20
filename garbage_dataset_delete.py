import os
fileName = "label_pet_"
fileName2 = "label_pet_"
annotationLocation = "C:/data/annotations/"  # annotation 파일 경로
datasetLocation = "C:/data/dataset/"



for i in range(0, 1500):
    try:
        fr = open(annotationLocation + fileName + str(i) + '_ko.xml', 'r')
        fr.close()

    except:

        jpgfile = datasetLocation + fileName + str(i) + '_ko.jpg'
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
            print(i, " jpg delete")



for i in range(0, 15000):
    try:
        fr = open(annotationLocation + fileName + str(i) + '.xml', 'r')
        fr.close()

    except:

        jpgfile = datasetLocation + fileName + str(i) + '.jpg'
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
            print(i, " jpg delete")

for i in range(0, 1500):
    try:
        fr = open(annotationLocation + fileName2 + "n_" + str(i) + ".xml", 'r')
        fr.close()

    except:

        jpgfile = datasetLocation + fileName2 + "n_" + str(i) + '.jpg'
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
            print(i, " ko jpg delete")


for i in range(0, 1500):
    try:
        fr = open(annotationLocation + fileName2 + "n_ko_" + str(i) + ".xml", 'r')
        fr.close()

    except:

        jpgfile = datasetLocation + fileName2 + "n_ko_" + str(i) + '.jpg'
        if os.path.isfile(jpgfile):
            os.remove(jpgfile)
            print(i, " ko jpg delete")