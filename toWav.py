import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from pydub import AudioSegment

def is_folderpath(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for dirname, _, filenames in os.walk("dataset/m4a"):
    for filename in filenames:
        if dirname!='dataset/m4a/0':
            continue

        m4a_file = os.path.join(dirname, filename)
        start_pos = m4a_file.rfind('/')
        alpha = m4a_file[start_pos-1:start_pos]

        i = 1123
        # if (i != 0):
        #     if (before_alpha != alpha):
        #         i = 1
        #     else:
        #         i += 1
        # else:
        #     i += 1

        before_alpha = alpha

        # print(start_pos, end_pos, imsi_breed)

        filepath = "dataset/tempWav/" + str(alpha) + "/" + str(alpha) + "_" + str(i) + ".wav"
        folder_path = "dataset/tempWav/" + str(alpha)
        is_folderpath(folder_path)
        print(filepath)
        track = AudioSegment.from_file(m4a_file, format='m4a')
        file_handle = track.export(filepath, format='wav')