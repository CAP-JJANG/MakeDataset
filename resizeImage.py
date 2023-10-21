import os
from PIL import Image


BASE_PATH = 'dataset/image' # Spectrogram이 저장되어 있는 폴더 경로 지정
OUTPUT_PATH = 'dataset/image224' # 크기 변환한 이미지 저장한 폴더 경로 지정


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


for dirname, _, filenames in os.walk(BASE_PATH):
    print(dirname, " is resizing...")
    for filename in filenames:
        if filename == ".DS_Store":
            continue

        label = dirname.split(os.sep)[-1]  # Get the label directory name

        start_pos = dirname.rfind(os.sep)
        filepath = os.path.join(dirname, filename)

        img = Image.open(filepath)
        img_resize = img.resize((224, 224))

        name_start_pos = filename.find('.')
        name_end_pos = filename.rfind('.')

        output_dir = os.path.join(OUTPUT_PATH, label)
        ensure_folder_exists(output_dir)

        output_filepath = os.path.join(output_dir, filename[:name_end_pos] + '.jpg')
        img_resize.save(output_filepath)
