
import os
from shutil import copyfile
import glob
import pandas as pd

def create_data_dir(pathData,pathDataOrig):


    os.system("mkdir " + pathData)
    pathAudio = pathData + 'audio/'
    pathImage = pathData + 'image/'
    os.system("mkdir " + pathAudio)
    os.system("mkdir " + pathImage)

    emotions = ['anger','happiness', 'neutral', 'sadness']

    for emotion in emotions:
        pathAudioEmotion = pathAudio + emotion
        pathImageEmotion = pathImage + emotion
        os.system("mkdir " + pathAudioEmotion)
        os.system("mkdir " + pathImageEmotion)


    for emotion in emotions:
        print('Emotion: '+ emotion)
        emotionFile = pd.read_csv(emotion[0:3]+'.csv')   
        emotionFilenames = emotionFile['filenames']
        for filename_target in emotionFilenames:
            for filename in glob.iglob(pathDataOrig + '/**/' + filename_target + '.wav', recursive=True):
                copyfile(filename, os.path.join(pathAudio + emotion, filename_target + '.wav'))

    
