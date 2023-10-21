import os
import wave
from pydub import AudioSegment

BASE_PATH = "dataset/tempWav"  # 원본 WAV 파일이 있는 폴더 경로 지정
OUTPUT_PATH = "dataset/wav"  # 속도 변환한 WAV 파일을 저장할 폴더 경로 지정
SILENT_FILE_PATH = "dataset/silent.wav"
silent_audio = AudioSegment.from_wav(SILENT_FILE_PATH)
SPEEDS = [1.00, 0.90, 1.10]
IMAGE_SIZE = 224


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# tempWav 파일 길이 얻는 함수
def get_wav_duration(file_name):
    audio = wave.open(file_name)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames / float(rate)
    return round(duration, 2)  # Return with two decimal places


# tempWav 파일 합치는 함수
# speed를 조절했을때 peak 이후 1초가 나오는 것을 보장하기 위해 묵음 파일과 합쳐 파일 길이를 늘린다.
def combine_with_silence(short_audio):
    combined_audio = short_audio + silent_audio
    return combined_audio


# 음성 속도 조절 함수
def adjust_audio_speed(input_dir, speed_factor):
    for dirname, _, filenames in os.walk(input_dir):
        for wav_file in filenames:
            if wav_file == ".DS_Store":
                continue

            wav_file_path = os.path.join(dirname, wav_file)
            sub_dir = os.path.basename(dirname)

            # Load the WAV file
            audio = AudioSegment.from_wav(wav_file_path)
            audio = combine_with_silence(audio)

            # 음성 속도 조절
            adjusted_audio = audio._spawn(audio.raw_data, overrides={
                "frame_rate": int(audio.frame_rate * speed_factor)
            })

            # Save the adjusted WAV file
            new_filename = os.path.join(OUTPUT_PATH, sub_dir,
                                        f"{os.path.splitext(wav_file)[0]}_speed_{speed_factor:.2f}.wav")
            folder_path = os.path.join(OUTPUT_PATH, sub_dir)
            ensure_folder_exists(folder_path)
            print(new_filename)
            adjusted_audio.export(new_filename, format="wav")


for speed in SPEEDS:
    adjust_audio_speed(BASE_PATH, speed)
