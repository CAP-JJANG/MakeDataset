import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import wave
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
from os import path

IMAGE_SIZE = 224

def is_folderpath(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# tempWav 파일 길이 얻는 함수
def get_wav_length(file_name):
    audio = wave.open(file_name)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames / float(rate)
    return round(duration,2) # 소수점 두번째 자리까지 반환


# tempWav 파일 합치는 함수

from pydub import AudioSegment

SILENT_FILE_PATH = "dataset/silent.wav"
file2 = AudioSegment.from_wav(SILENT_FILE_PATH)


def combine_file(short_file):
    file1 = short_file

    combined_file = file1 + file2
    return combined_file


from pydub import AudioSegment
import IPython.display as ipd


# 음성 속도 조절 함수
def change_speed(dir_path, speed_factor):
    for dirname, _, filenames in os.walk(dir_path):
        for wav_file in filenames:
            wav_file_path = dirname + "/" + wav_file
            wav_file = wav_file[:-4]
            # WAV 파일 로드
            sound = AudioSegment.from_wav(wav_file_path)
            sound = combine_file(sound)

            # 음성 속도 조절
            sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
                "frame_rate": int(sound.frame_rate * speed_factor)
            })

            sub_dir_pos = dirname.rfind('/')
            sub_dir = dirname[sub_dir_pos + 1]

            # 조절된 WAV 파일 저장
            new_filename = f"dataset/wav/{sub_dir}/{wav_file}_speed_{speed_factor:.2f}.wav"
            folder_path = f"dataset/wav/{sub_dir}"
            is_folderpath(folder_path)
            print(new_filename)
            sound_with_altered_frame_rate.export(new_filename, format="wav")
            #print(get_wav_length(wav_file_path), "! after: ", get_wav_length(new_filename))
            # print(f"Speed of {wav_file} has been changed to {speed_factor}. New file: {new_filename}")


DIR_PATH = "dataset/tempWav"
SPEED0 = 1.00
SPEED1 = 1.25
SPEED2 = 1.50
change_speed(DIR_PATH, SPEED0)
change_speed(DIR_PATH, SPEED1)
change_speed(DIR_PATH, SPEED2)

#ipd.Audio(WAV_FILE) # load a local WAV file
#ipd.Audio("/kaggle/working/wavfiles/a/a1_speed_3.00.tempWav") # load a local WAV file

