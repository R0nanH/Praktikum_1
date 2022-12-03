from PIL import Image
import imagehash
import os
import time
from AVLTree import AVLTree
from AVLTree import node

imageDict = dict()
directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    imageDict[hashVal] = fileDirectory

# directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/"
# for file in os.listdir(directory):
# filename = os.fsdecode(file)
# fileDirectory = directoryAsStr + filename
# hashVal = imagehash.average_hash(Image.open(fileDirectory))
# imageDict[hashVal] = fileDirectory

testList = [
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/image_0026.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/image_0178.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/image_0632.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/image_0023.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/image_0346.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/image_0435.jpg"
]
print(":::::::Hashtable:::::::")
for item in testList:
    execTime = round(time.time() * 1000)
    print(imageDict.get(imagehash.average_hash(Image.open(item))))
    execTime = round(time.time() * 1000) - execTime
    print("Execution time:", execTime)

avlTree = AVLTree()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)


def get(image):
    avlTree.find(image)


print(":::::::AVL-Tree:::::::")
for item in testList:
    startTime = round(time.time() * 1000)
    if avlTree.search(str(imagehash.average_hash(Image.open(item)))):
        print(avlTree.find(str(imagehash.average_hash(Image.open(item)))).pBucket)
        execTime = round(time.time() * 1000) - startTime
        print("Execution time:", execTime)
    else:
        execTime = round(time.time() * 1000) - startTime
        print("None")
        print("Execution time:", execTime)


print(":::::::AVL-Tree(Most Similar):::::::")
for item in testList:
    startTime = round(time.time() * 1000)
    print(avlTree.find_most_similar(str(imagehash.average_hash(Image.open(item)))).pBucket)
    execTime = round(time.time() * 1000) - startTime
    print("Execution time:", execTime)

