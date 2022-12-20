"""Resize bulk Images using python"""
import argparse
import os
from time import time

parser = argparse.ArgumentParser()
parser.add_argument('-r','--resize', nargs='+', help="pass the resize resolution", type=int)
parser.add_argument("-s","--source", help="pass the source directory" )
parser.add_argument("-t","--target", help="pass the target directory" )
args = parser.parse_args()

pathOfImages = args.source
pathToSave = args.target
resizeResolution = tuple(args.resize)

try:
    import cv2
except ModuleNotFoundError:
    print("Opencv is not found")
    print("Installing Opencv")
    os.system("pip install opencv-python")
    import cv2

try:
    from tqdm import tqdm as progressBar
except ModuleNotFoundError:
    print("Tqdm is not found")
    print("Installing Opencv")
    os.system("pip install tqdm")
    from tqdm import tqdm as progressBar



files = os.listdir(pathOfImages)
Bar = progressBar(total=len(files),desc="Process")
initialTime = time()

for imageName in files:
  imagePath = os.path.join(pathOfImages,imageName)
  imageData = cv2.imread(imagePath)
  imageResized = cv2.resize(imageData,resizeResolution)
  if not os.path.exists(pathToSave):
    os.mkdir(pathToSave)
  cv2.imwrite(os.path.join(pathToSave,imageName),imageResized)
  Bar.update(1)
finalTime = time()
Bar.close()



print("Time Taken",finalTime-initialTime)
print("Done!")




