import xml.etree.ElementTree as ET
from os import listdir
import cv2
import numpy as np
import imgaug as ia
from imgaug import augmenters as iaa
from pascal_voc_writer import Writer
# from files import *

#  annotation  박스 정보 긁기
def read_anntation(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    bounding_box_list = []

    file_name = root.find('filename').text
    for obj in root.iter('object'):

        object_label = obj.find("name").text
        for box in obj.findall("bndbox"):
            x_min = int(box.find("xmin").text)
            y_min = int(box.find("ymin").text)
            x_max = int(box.find("xmax").text)
            y_max = int(box.find("ymax").text)

        bounding_box = [object_label, x_min, y_min, x_max, y_max]
        bounding_box_list.append(bounding_box)

    return bounding_box_list, file_name

# dataset, annotation에서 파일 read_anntation 함수 사용해서 다 긁음
def read_train_dataset(data_dir, anno_dir):
    images = []
    annotations = []

    for file in listdir(data_dir):
        if 'jpg' in file.lower() or 'png' in file.lower():
            images.append(cv2.imread(data_dir + file, 1))
            annotation_file = file.replace(file.split('.')[-1], 'xml')
            bounding_box_list, file_name = read_anntation(anno_dir + annotation_file)
            annotations.append((bounding_box_list, annotation_file, file_name))

    images = np.array(images)

    return images, annotations



ia.seed(1)

data_dir = 'C:/data/dpdata/'
anno_dir = 'C:/data/dpanno/'

# save_data_dir2 ='C:/data/save_data/'
# save_anno_dir2 = 'C:/data/save_anno/'
save_data_dir ='C:/data/dataset/'
save_anno_dir = 'C:/data/annotations/'

images, annotations = read_train_dataset(data_dir,anno_dir)

for index in range(1) : # 한장당 늘리려는 개수

    for idx in range(len(images)):
        image = images[idx]
        boxes = annotations[idx][0]

        ia_bounding_boxes = []
        for box in boxes:
            ia_bounding_boxes.append(ia.BoundingBox(x1=box[1], y1=box[2], x2=box[3], y2=box[4]))

        bbs = ia.BoundingBoxesOnImage(ia_bounding_boxes, shape=image.shape)

        # 이 옵션들이 다 랜덤 범위값으로 모두 랜덤하게 생겨서 한장을 복제함
        seq = iaa.Sequential([
            iaa.Fliplr(0.5),  # horizontally flip 50% of all images, 좌우반전 확률
            # iaa.Flipud(0.5),  # vertically flip 20% of all images, 상하반전 확률
            iaa.LinearContrast((0.97, 1.03)), #대조 범위 약간 색감 찐하게하거나 흐리게 색을 변형
            iaa.Multiply((0.8, 1), per_channel=0.1), #밝기 범위
            iaa.Affine( 
                scale={"x": (0.75, 1.0), "y": (0.75, 1.0)}, #줌 아웃
                # translate_percent={"x": (-0.01, 0.01), "y": (-0.01 ,0.01)}, #줌 아웃시 px 이동, scale이랑 같게줘야함
                rotate=(-10, 10) # 회전 >> 이걸 크게주면 없어지는 이미지의 범위 있을수잇음, 모서리

                # shear=(-20, 20)
            )
        ])

        seq_det = seq.to_deterministic()

        image_aug = seq_det.augment_images([image])[0]
        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]

        new_image_file = save_data_dir + 'after_'+str(index) + "_" + annotations[idx][2]
        cv2.imwrite(new_image_file, image_aug)

        # new_image_file2 = save_data_dir2 + 'after_'+str(index) + "_" + annotations[idx][2]
        # cv2.imwrite(new_image_file2, image_aug)

        h, w = np.shape(image_aug)[0:2]
        voc_writer = Writer(new_image_file, w, h)

        for i in range(len(bbs_aug.bounding_boxes)):
            bb_box = bbs_aug.bounding_boxes[i]
            voc_writer.addObject(boxes[i][0], int(bb_box.x1), int(bb_box.y1), int(bb_box.x2), int(bb_box.y2))

        # voc_writer.save(dir + 'after_' + annotations[idx][1])
        voc_writer.save(save_anno_dir + 'after_' +str(index) + "_" + annotations[idx][1])