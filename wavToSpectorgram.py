import numpy as np
import pandas as pd
import librosa, librosa.display
import matplotlib.pyplot as plt
import os

FIG_SIZE = (15, 10)
DATA_NUM = 30

paths = []
abel_gubuns = []

def is_folderpath(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for dirname, _, filenames in os.walk("dataset/wav/"):
    for filename in filenames:
        if dirname!='dataset/wav/9':
            continue

        # load audio file with Librosa
        file_path = dirname + '/' + filename

        paths.append(file_path)
        sig, sr = librosa.load(file_path, sr=22050)

        # 에너지 평균 구하기
        sum = 0

        for i in range(0, sig.shape[0]):
            sum += sig[i] ** 2

        mean = sum / sig.shape[0]

        # 피크인덱스 찾기
        for i in range(0, sig.shape[0]):
            if (sig[i] ** 2 >= mean):
                peekIndex = i
                break

        START_LEN = 1102
        END_LEN = 20948
        if peekIndex > 1102:
            startPoint = peekIndex - START_LEN
            endPoint = peekIndex + 22050
        else:
            startPoint = peekIndex
            endPoint = peekIndex + END_LEN

        # 단순 푸리에 변환 -> Specturm
        fft = np.fft.fft(sig[startPoint:endPoint])

        # 복소공간 값 절댓갑 취해서, magnitude 구하기
        magnitude = np.abs(fft)

        # Frequency 값 만들기
        f = np.linspace(0, sr, len(magnitude))

        # 푸리에 변환을 통과한 specturm은 대칭구조로 나와서 high frequency 부분 절반을 날려고 앞쪽 절반만 사용한다.
        left_spectrum = magnitude[:int(len(magnitude) / 2)]
        left_f = f[:int(len(magnitude) / 2)]

        # STFT -> Spectrogram
        hop_length = 512  # 전체 frame 수
        n_fft = 2048  # frame 하나당 sample 수

        # calculate duration hop length and window in seconds
        hop_length_duration = float(hop_length) / sr
        n_fft_duration = float(n_fft) / sr

        # STFT
        stft = librosa.stft(sig[startPoint:endPoint], n_fft=n_fft, hop_length=hop_length)

        # 복소공간 값 절댓값 취하기
        magnitude = np.abs(stft)

        # magnitude > Decibels
        log_spectrogram = librosa.amplitude_to_db(magnitude)

        FIG_SIZE = (10, 10)

        # display spectrogram
        plt.figure(figsize=FIG_SIZE)
        librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, cmap='magma')

        dir_pos = filename.find('_')
        name_end_pos = filename.rfind('.')
        abel_gubuns.append(filename[0])
        # save spectrogram image

        folder_path = "dataset/image/" + filename[:dir_pos]
        is_folderpath(folder_path)
        plt.savefig(folder_path + '/' + filename[:name_end_pos] + '.jpg')
        plt.close()
        # plt.show()

pd.set_option('display.max_colwidth', 200)  # column의 width 설정
data_df = pd.DataFrame({'path': paths, 'label': abel_gubuns})
print('data_df shape:', data_df.shape)
data_df.head()  # DataFrame 앞 5개 출력
