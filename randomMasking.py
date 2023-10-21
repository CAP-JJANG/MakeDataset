import os
import numpy as np
import matplotlib.pyplot as plt

# 이미지 폴더 경로 설정
BASE_PATH = "dataset/image224"

# 사각형의 크기 (고정값)
# 가로
rect_width_h = 174
rect_height_h = 25
# 세로
rect_width_v = 25
rect_height_v = 174

# 사각형이 들어가는 범위 설정
# 가로
rect_x_start_h = 28
rect_x_end_h = 29  # 스펙트로그램 이미지의 가로 크기에 따라 설정 (0 ~ width-rect_width 사이의 값)
rect_y_start_h = 28.2
rect_y_end_h = 184  # 스펙트로그램 이미지의 세로 크기에 따라 설정 (0 ~ height-rect_height 사이의 값)
# 세로
rect_x_start_v = 28
rect_x_end_v = 175  # 스펙트로그램 이미지의 가로 크기에 따라 설정 (0 ~ width-rect_width 사이의 값)
rect_y_start_v = 26
rect_y_end_v = 27  # 스펙트로그램 이미지의 세로 크기에 따라 설정 (0 ~ height-rect_height 사이의 값)


def is_folderpath(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


output_path = "dataset/image224"  # 마스킹된 이미지를 원본 이미지 폴더에 저장

for root, dirs, filenames in os.walk(BASE_PATH):
    for filename in filenames:
        if '_1.00' not in filename:  # 속도 1.00인 원본 이미지만 처리
            continue
        if 'hmasked' in filename or 'vmasked' in filename:  # 이미 처리된 이미지는 건너뜁니다.
            continue

        image_file_path = os.path.join(root, filename)
        spec_image = plt.imread(image_file_path)

        # 스펙트로그램 이미지에 랜덤 마스킹 적용
        masked_spec_image_h = np.copy(spec_image)
        masked_spec_image_v = np.copy(spec_image)
        num_rectangles = 1  # 가리개 사각형 개수

        for i in range(num_rectangles):
            # 랜덤 마스킹 - 가로
            x = np.random.randint(rect_x_start_h, rect_x_end_h)
            y = np.random.randint(rect_y_start_h, rect_y_end_h)
            masked_spec_image_h[y:y + rect_height_h, x:x + rect_width_h, :] = 0  # 마스킹된 영역을 검정색(0)으로 설정

            # 마스킹 된 이미지 로컬에 저장
            masked_image_file_name = "hmasked_" + filename  # 저장할 이미지 파일명 지정
            masked_image_file_path = os.path.join(root, masked_image_file_name)  # 저장할 이미지 파일 경로 지정
            plt.imsave(masked_image_file_path, masked_spec_image_h)

            # 랜덤 마스킹 - 세로
            x = np.random.randint(rect_x_start_v, rect_x_end_v)
            y = np.random.randint(rect_y_start_v, rect_y_end_v)
            masked_spec_image_v[y:y + rect_height_v, x:x + rect_width_v, :] = 0  # 마스킹된 영역을 검정색(0)으로 설정

            # 마스킹 된 이미지 로컬에 저장
            masked_image_file_name = "vmasked_" + filename  # 저장할 이미지 파일명 지정
            masked_image_file_path = os.path.join(root, masked_image_file_name)  # 저장할 이미지 파일 경로 지정
            plt.imsave(masked_image_file_path, masked_spec_image_v)
