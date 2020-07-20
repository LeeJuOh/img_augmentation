import xml.etree.ElementTree as ET
from os import listdir
import cv2
import numpy as np
import imgaug as ia
from imgaug import augmenters as iaa
from pascal_voc_writer import Writer
# from files import *



# dataset, annotation에서 파일 read_anntation 함수 사용해서 다 긁음
def read_train_dataset(data_dir):
    images = []


    for file in listdir(data_dir):
        if 'jpg' in file.lower() :
            images.append(cv2.imread(data_dir + file, 1))

    images = np.array(images)
    return images



ia.seed(1)

# data_dir = 'C:/Users/235/Desktop/test/'
# save_data_dir ='C:/Users/235/Desktop/test/'
data_dir = 'C:/data/test'
save_data_dir ='C:/data/test'

images= read_train_dataset(data_dir)

for index in range(6) : # 한장당 늘리려는 개수

    print(len(images))
    for idx in range(len(images)):
        image = images[idx]

        # 이 옵션들이 다 랜덤 범위값으로 모두 랜덤하게 생겨서 한장을 복제함
        seq = iaa.Sequential([
            iaa.Fliplr(0.5),  # horizontally flip 50% of all images, 좌우반전 확률
            # iaa.Flipud(0.5),  # vertically flip 20% of all images, 상하반전 확률
            # iaa.LinearContrast((0.95, 1.05)), #대조 범위 약간 색감 찐하게하거나 흐리게 색을 변형
            iaa.Multiply((0.75, 1), per_channel=0.1), #밝기 범위
            iaa.Affine(
                scale={"x": (0.75, 1.0), "y": (0.75, 1.0)}, #줌 아웃
                # translate_percent={"x": (-0.01, 0.01), "y": (-0.01 ,0.01)}, #줌 아웃시 px 이동, scale이랑 같게줘야함
                rotate=(-10, 10) # 회전 >> 이걸 크게주면 없어지는 이미지의 범위 있을수잇음, 모서리

                # shear=(-20, 20)
            )
        ])

        seq_det = seq.to_deterministic()
        image_aug = seq_det.augment_images([image])[0]

        new_image_file = save_data_dir + 'after_'+str(index) +'.jpg'
        cv2.imwrite(new_image_file, image_aug)

