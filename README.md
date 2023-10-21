## :raised_hands: 소개
**[ENG]**

This repository contains the process of creating a dataset for learning CSD-Model (a model that receives an acoustic signal and predicts what alphabet the corresponding acoustic signal is).

 About 50 people recorded the unique acoustic signals generated by writing lowercase alphabets on a table with Android voice recording, collecting about 900 acoustic data per class. We implemented a function that cuts the acoustic file by one second from the peak point by finding the peak point where the sudden explosive signal occurs in the collected dataset. A sound file cut to 1 second was saved as a wave file and converted into a spectrogram, an image in the form of a time-frequency graph.

 To augment the dataset, we created a 3-fold image of the original data by converting the wave file to 1.25x and 1.50x and then to a spectrogram image. In addition, random masking was performed once, horizontally and vertically from the original spectrogram to create three times the image of the original data, augmenting the dataset to about 4500 per class.

<br>

**[KOR]**

CSD-Model(음향 신호를 받아 해당 음향 신호가 무슨 알파벳인지 예측하는 모델) 학습을 위한 데이터셋을 만드는 과정을 담은 레포지토리입니다.

  약 50명의 사람들을 통해 Android 음성녹음 기능으로 테이블 위에서 알파벳 소문자를 썼을 때 생기는 고유한 음향 신호를 녹음하여, 클래스당 약 900개의 음향 데이터를 수집했습니다. 수집한 데이터셋에서 갑자기 폭발적인 신호가 발생하는 Peak 지점을 찾아 Peak 지점부터 음향 파일을 1초를 자르는 함수를 구현했습니다. 1초로 잘린 음향 파일을 wav 파일로 저장하고, 시간-주파수 그래프 형태의 이미지인 스펙트로그램으로 변환했습니다. 

  데이터셋 증강을 위해, wav 파일을 1.25배속과 1.50배속 한 후 스펙트로그램 이미지로 변환하여 원본 데이터의 3배 이미지를 생성했습니다. 뿐만 아니라, 원본 스펙트로그램에서 가로, 세로 한 번씩 랜덤 마스킹을 진행하여 원본 데이터의 3배 이미지를 생성하여 클래스당 약 4500개로 데이터셋을 증강했습니다.


<br><br>
## 💪 주요 기능 및 순서
**[ENG]**
1. toWav.py
   
   Find the peak point where the sudden explosive signal occurs in the collected acoustic signal and cut 1 second from the peak and save it as a wave file.
2. toSpeedWav.py
   
   1.25x, 1.50x wave files.
3. WavToSpectrogram.py
   
   Use the Librosa library to convert the wave files obtained in #1 and #2 into spectrogram images.
4. resizeImage.py
   
   Convert the image size to 224 X 224.
5. randomMasking.py
    
   Random masking is performed once in a horizontal or vertical manner from the original spectrogram image.

<br>

**[KOR]**
1. toWav.py
   
   수집한 음향 신호에서 갑자기 폭발적인 신호가 발생하는 Peak 지점을 찾아 Peak부터 1초를 잘라 wav 파일로 저장합니다.
2. toSpeedWav.py
   
   wav 파일을 1.25배속, 1.50배속합니다.
3. WavToSpectrogram.py
   
   1번과 2번에서 얻은 wav 파일을 Librosa 라이브러리를 이용해 스펙트로그램 이미지로 변환합니다.
4. resizeImage.py
   
   이미지 크기를 224 X 224로 변환합니다.
5. randomMasking.py
   
   원본 스펙트로그램 이미지에서 가로, 세로 한 번씩 랜덤 마스킹을 진행합니다.
   
   

<br><br>
## 🦾 주요 기술

* PyCharm IDE
* Python 3.9.13
* Ipython 8.15.0
* Librosa 0.10.1
* Matplotlib 3.7.2
* Numpy 1.25.2
* Pandas 2.1.1
* Pillow 10.0.1
* Pydub 0.25.1


<br><br>
## ⭐️ 설치 방법
1. clone [github 리포지토리 주소]
2. 가상환경 생성
    1. python -m venv venv 또는 python3 -m venv venv
3. 가상환경 실행
    1. Windows
        1. venv\Scripts\activate
    2. macOS 및 Linux
        1. source venv/bin/activate
4. pip 최신버전으로 업그레이드
   python -m pip install --upgrade pip
    또는
   python3 -m pip install --upgrade pip
5. 패키지 설치
    1. pip install -r requirements.txt
    2. pip3 install -r requirements.txt <br>
6. 순서대로 프로젝트 Run

<br><br>
## 🤖 라이센스
This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/CAP-JJANG/MakeDataset/blob/main/LICENSE) file for details.  
[OSS Notice](https://github.com/CAP-JJANG/MakeDataset/blob/main/OSS-Notice.md) sets forth attribution notices for third party software that may be contained in this application.

