import os
import cv2 as cv
import numpy as np
from PIL import Image
import winsound

recognizer = cv.face.LBPHFaceRecognizer_create()
path = 'dataSet'
duration = 50
freq = 440

def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv.imshow("Training", faceNp)
        cv.waitKey(10)
    return IDs, faces


Ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.write('trainingData.yml')
winsound.Beep(freq, duration)
cv.destroyAllWindows()