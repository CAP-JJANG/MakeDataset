import os
import glob
from PIL import Image

# 이미지 크기 변환
PATH = 'dataset/image224/0'
i = 0

def is_folderpath(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for dir, _ ,filenames in os.walk(PATH):
    for filename in filenames:
        start_pos = dir.rfind('/')
        filepath = dir +'/' + filename

        img = Image.open(filepath)
        img_resize = img.resize((224, 224))
        title, ext = os.path.splitext(filepath)

        start_pos = dir.rfind('/')
        alpha = dir[start_pos+1]

        name_start_pos = filename.find('.')
        name_end_pos = filename.rfind('.')

        #idx_start_pos, idx_end_pos = 0, 0
        if 'hmasked' in filename or 'vmasked' in filename:
            idx_start_pos = filename[8:].find('_') + 8 + 1
            idx_end_pos = filename[idx_start_pos:].find('_')
            print(filename[:idx_end_pos])
        # else:
        #     idx_start_pos = filename[:name_end_pos].find('_') + 1
        #     idx_end_pos = filename[idx_start_pos:].find('_')
        #
        # print(filename[idx_start_pos:])
        # idx_end_pos = filename[idx_start_pos:].find('_')
        #
        # print(filename[idx_start_pos:idx_end_pos])

        #
        # #print('dataset/image224/' + alpha + "/" + filename[:name_start_pos]+ '_'+filename[name_end_pos-2:name_end_pos] + '.jpg')
        # filepath = 'test/' + alpha + "/" + filename[:name_end_pos] + '.jpg'
        # print(filepath)
        # folder_path = 'test/' + alpha
        #
        # filepath=''
        # folder_path=''
        #
        # if filename
        #
        # is_folderpath(folder_path)
        # img_resize.save(filepath)
