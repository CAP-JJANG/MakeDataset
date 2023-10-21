import os
import glob
from PIL import Image

# 이미지 크기 변환
PATH = 'dataset/image/1'
i = 0

def is_folderpath(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for dir, _ ,filenames in os.walk(PATH):
    print(dir," is resizing...")
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

        #print('dataset/image224/' + alpha + "/" + filename[:name_start_pos]+ '_'+filename[name_end_pos-2:name_end_pos] + '.jpg')
        filepath = 'dataset/image224/' + alpha + "/" + filename[:name_end_pos] + '.jpg'
        print(filepath)
        folder_path = 'dataset/image224/' + alpha
        is_folderpath(folder_path)
        img_resize.save(filepath)
