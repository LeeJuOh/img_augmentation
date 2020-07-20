import glob
from os import listdir


def file_path_save():
    data_dir = 'C:/git/darknet/build/darknet/x64/data/val/'

    # filenames = []
    # files = sorted(glob.glob("C:/git/darknet/build/darknet/x64/data/val/*.jpg"))
    # size = len(files)
    # for i in range(size):
    #     print((i+1) ,' / ', size)
    #     f = open("C:/git/darknet/build/darknet/x64/data/valid.txt", 'a')
    #     print(files[i])
    #     f.write(files[i] + "\n")
    i = 0
    for file in listdir(data_dir):
        print((i + 1), data_dir + file)
        f = open("C:/git/darknet/build/darknet/x64/data/valid.txt", 'a')
        f.write(data_dir + file + "\n")
        i+=1

if __name__ == '__main__': file_path_save()

