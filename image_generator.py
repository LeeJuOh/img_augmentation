import numpy as np
import os
from os import listdir
np.random.seed(3)

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

data_datagen = ImageDataGenerator(rescale=1. / 255,
                                  rotation_range=5,
                                  # shear_range=0.2,
                                 # width_shift_range=0.1,
                                 #  height_shift_range=0.1,
                                 # zoom_range=1.2,
                                  horizontal_flip=True,
                                  vertical_flip=False,
                                  fill_mode='nearest')

filename_in_dir = []
data_dir = 'C:/Users/235/Desktop/test3/Chueotang/'  # 복제할 파일이 들어있는 폴더 경로
save_dir = 'C:/Users/235/Desktop/test3/Chueotang/'  # 복제후 파일이 들어있을 폴더 경로
# save_file_name = 'Kkanpunggi'  # 카테고리 이름


for file in listdir(data_dir):
    if 'jpg' in file.lower():
        print(file)
        f = file.split('.')
        print(f[0])
        print(f[1])
        img = load_img(data_dir + file)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        i = 0
        for batch in data_datagen.flow(x, batch_size=1, save_to_dir=save_dir, save_prefix=f[0] +'_' , save_format=f[1]):
            i += 1

            if i > 8:
                break