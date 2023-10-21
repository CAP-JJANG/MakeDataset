import os
from pydub import AudioSegment


BASE_PATH = "dataset/m4a"  # M4A 파일이 있는 폴더 경로 지정
OUTPUT_PATH = "dataset/tempWav"  # WAV 파일을 저장할 폴더 경로 지정


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


for dirname, _, filenames in os.walk(BASE_PATH):
    i = 1
    for filename in filenames:
        m4a_file = os.path.join(dirname, filename)

        # 폴더 경로에서 라벨 명을 추출
        label = os.path.basename(dirname)

        # m4a 파일을 WAV 파일로 변환
        track = AudioSegment.from_file(m4a_file, format='m4a')

        folder_path = os.path.join(OUTPUT_PATH, label)
        ensure_folder_exists(folder_path)

        # 저장할 WAV 파일 경로 생성
        filepath = os.path.join(folder_path, f"{label}_{i}.wav")
        i += 1

        print(filepath)

        # WAV 파일 저장
        file_handle = track.export(filepath, format='wav')
