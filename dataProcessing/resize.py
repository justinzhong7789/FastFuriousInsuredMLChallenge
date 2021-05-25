
import os
from PIL import Image

trainAddr = "../dataset/trainImages"
testAddr = "../dataset/testImages"

desiredSize = (224, 224)

def resize(folder, desiredSize):
    for image in os.listdir(folder):
        imagePath = os.path.join(folder, image)
        im = Image.open(imagePath)
        resized = im.resize(desiredSize)
        resized.save(imagePath)

if __name__ == "__main__":
    resize(trainAddr, desiredSize)
    resize(testAddr, desiredSize)
    