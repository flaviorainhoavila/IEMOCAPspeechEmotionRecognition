# IEMOCAP speech emotion Recognition

Automatic speech emotion recognition based on transfer learning from spectrograms using ResNET 

The dataset can be obtained from https://sail.usc.edu/iemocap/

In addition to audio, the dataset contains other forms of media like video. This notebook only deals with the audio part, and in order to separate the audio part from the rest, the first part of the notebook should be executed. The recommendation is to store the original downloaded IEMOCAP dataset in the folder 'IEMOCAPoriginal'. The relevant files for each class are stored in .csv files in this reposity. The notebook automatically searches for the files inside IEMOCAP and orgonaze them in the 'audio' folder, in which each class has its own subfolder.

