import os
import numpy as np
import matplotlib.pyplot as plt

# 이미지 폴더 경로 설정
image_folder_path = "dataset/image224/1"  # 스펙트로그램 이미지가 있는 폴더 경로 지정

# 사각형의 크기 (고정값)
# 가로
# rect_width = 174
# rect_height = 25
# 세로
rect_width = 25
rect_height = 174

# 사각형이 들어가는 범위 설정
# 가로
# rect_x_start = 28
# rect_x_end = 29  # 스펙트로그램 이미지의 가로 크기에 따라 설정 (0 ~ width-rect_width 사이의 값)
# rect_y_start = 28.2
# rect_y_end = 184  # 스펙트로그램 이미지의 세로 크기에 따라 설정 (0 ~ height-rect_height 사이의 값)
# 세로
rect_x_start = 28
rect_x_end = 175  # 스펙트로그램 이미지의 가로 크기에 따라 설정 (0 ~ width-rect_width 사이의 값)
rect_y_start = 26
rect_y_end = 27  # 스펙트로그램 이미지의 세로 크기에 따라 설정 (0 ~ height-rect_height 사이의 값)

print(rect_width, rect_height)

for dirname, _, filenames in os.walk(image_folder_path):
    # 폴더 내의 모든 이미지 파일 로드
    for file_name in filenames:
        # 속도 00인 원본만
        if '_1.00' not in file_name:
            continue
        if 'hmasked' in file_name:
            continue
        if 'vmasked' in file_name:
            continue
        if file_name.endswith(".png") or file_name.endswith(".jpg"):  # 이미지 파일 확장자에 따라 수정
            image_file_path = os.path.join(dirname, file_name)
            spec_image = plt.imread(image_file_path)

            # 스펙트로그램 이미지에 랜덤 마스킹 적용
            masked_spec_image = np.copy(spec_image)
            height, width, _ = masked_spec_image.shape
            num_rectangles = 1  # 가리개 사각형 개수
            for i in range(num_rectangles):
                x = np.random.randint(rect_x_start, rect_x_end)
                y = np.random.randint(rect_y_start, rect_y_end)
                masked_spec_image[y:y + rect_height, x:x + rect_width, :] = 0  # 마스킹된 영역을 검정색(0)으로 설정

                # 마스킹된 이미지 로컬에 저장
                # 가로
                # masked_image_file_name = "hmasked_" + file_name  # 저장할 이미지 파일명 지정
                # 세로
                masked_image_file_name = "vmasked_" + file_name  # 저장할 이미지 파일명 지정
                masked_image_file_path = os.path.join(dirname, masked_image_file_name)  # 저장할 이미지 파일 경로 지정
                plt.imsave(masked_image_file_path, masked_spec_image)
                print(f"Masked image saved: {masked_image_file_path}")

            # 마스킹된 이미지 로컬에 적용
            # 이미지 처리 코드 추가
            # 예시로 matplotlib를 사용하여 이미지를 로컬에 저장하는 코드를 추가합니다.
            # masked_image_file_path = os.path.join(image_folder_path, "masked_" + file_name)  # 저장할 이미지 파일 경로 지정
            # plt.imsave(masked_image_file_path, masked_spec_image)

            #이미지 처리 작업 예시: 마스킹된 이미지를 화면에 출력
            # plt.figure(figsize=(10, 5))
            # plt.subplot(1, 2, 1)
            # plt.imshow(spec_image)
            # plt.title("Original Spectrogram")
            # plt.subplot(1, 2, 2)
            # plt.imshow(masked_spec_image)
            # plt.title("Masked Spectrogram")
            # plt.show()
