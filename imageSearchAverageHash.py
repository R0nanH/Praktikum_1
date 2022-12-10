from PIL import Image
import imagehash
import os
import time
from AVLTree import AVLTree
from AVLTree import node

collisions = 0
imageDict = dict()
collisionDict = dict()
directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
        collisionDict[fileDirectory] = imageDict.get(hashVal)
    imageDict[hashVal] = fileDirectory

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/BACKGROUND_Google/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
    imageDict[hashVal] = fileDirectory

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/watch/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
    imageDict[hashVal] = fileDirectory

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces_easy/"
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
    imageDict[hashVal] = fileDirectory

testList = [
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/image_0026.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/image_0178.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/image_0632.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/image_0023.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/image_0346.jpg",
    "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces/image_0435.jpg"
]
print(":::::::Hashtable:::::::")
print("Total collisions: ", collisions)
print(collisionDict.items())
for item in testList:
    execTime = time.time() * 1000
    print(imageDict.get(imagehash.average_hash(Image.open(item))))
    execTime = time.time() * 1000 - execTime
    print("Execution time:", execTime)

avlTree = AVLTree()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/BACKGROUND_Google/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/watch/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces_easy/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

print(":::::::AVL-Tree:::::::")
for item in testList:
    startTime = time.time() * 1000
    foundNode = avlTree.find(str(imagehash.average_hash(Image.open(item))))
    if foundNode is not None:
        print(foundNode.pBucket)
    else:
        print(foundNode)
    execTime = time.time() * 1000 - startTime
    print("Execution time:", execTime)


print(":::::::AVL-Tree(Most Similar):::::::")
for item in testList:
    startTime = time.time() * 1000
    print(avlTree.find_most_similar(str(imagehash.average_hash(Image.open(item)))).pBucket)
    execTime = time.time() * 1000 - startTime
    print("Execution time:", execTime)


print(":::::::Check transform changes:::::::")
directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/transforms/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    print(file)
    print("Hashvalue: " + str(imagehash.average_hash(Image.open(fileDirectory))))


