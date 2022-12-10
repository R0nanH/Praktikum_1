from PIL import Image
import imagehash
import os
import time
from AVLTree import AVLTree
from AVLTree import node


def calculate_hamming_distance(key1, key2):
    hamming_distance = 0
    for element in range(0, len(key1)):
        if key1[element] is not key2[element]:
            hamming_distance = hamming_distance + 1
    return hamming_distance


def get_most_similar(avltree, key):
    if avltree.root is not None:
        return _get_most_similar(key, avltree.root)
    else:
        return None


def _get_most_similar(key, cur_node):
    cur_node_ham_dist = calculate_hamming_distance(cur_node.key, key)
    if cur_node.key is key:
        if cur_node.left_child is None and cur_node.right_child is None:
            return cur_node.parent
        elif cur_node.left_child is not None and cur_node.right_child is not None:
            if calculate_hamming_distance(cur_node.left_child.key, key) <= calculate_hamming_distance(cur_node.right_child.key, key):
                return cur_node.left_child
            else:
                return cur_node.right_child
        elif cur_node.left_child is None:
            return cur_node.right_child
        else:
            return cur_node.left_child
    else:
        print(cur_node_ham_dist)
        if cur_node_ham_dist <= calculate_hamming_distance(cur_node.left_child.key, key) and cur_node_ham_dist <= calculate_hamming_distance(cur_node.right_child.key, key):
            return cur_node
        elif key < cur_node.key and cur_node.left_child is not None:
            return _get_most_similar(key, cur_node.left_child)
        elif key > cur_node.key and cur_node.right_child is not None:
            return _get_most_similar(key, cur_node.right_child)


collisions = 0
imageDict = dict()
collisionDict = dict()
directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.dhash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
        collisionDict[fileDirectory] = imageDict.get(hashVal)
    imageDict[hashVal] = fileDirectory

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/BACKGROUND_Google/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.dhash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
        collisionDict[fileDirectory] = imageDict.get(hashVal)
    imageDict[hashVal] = fileDirectory

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/watch/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.dhash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
        collisionDict[fileDirectory] = imageDict.get(hashVal)
    imageDict[hashVal] = fileDirectory

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/Faces_easy/"
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.average_hash(Image.open(fileDirectory))
    if imageDict.get(hashVal) is not None:
        collisions = collisions + 1
        collisionDict[fileDirectory] = imageDict.get(hashVal)
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
    print(imageDict.get(imagehash.dhash(Image.open(item))))
    execTime = time.time() * 1000 - execTime
    print("Execution time:", execTime)

avlTree = AVLTree()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.dhash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/BACKGROUND_Google/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.dhash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/airplanes/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    hashVal = imagehash.dhash(Image.open(fileDirectory))
    hashValAsString = str(hashVal)
    avlTree.insert(hashValAsString, fileDirectory)

print(":::::::AVL-Tree:::::::")
for item in testList:
    startTime = time.time() * 1000
    foundNode = avlTree.find(str(imagehash.dhash(Image.open(item))))
    if foundNode is not None:
        print(foundNode.pBucket)
    else:
        print(foundNode)
    execTime = time.time() * 1000 - startTime
    print("Execution time:", execTime)

print(":::::::AVL-Tree(Most Similar):::::::")
for item in testList:
    startTime = time.time() * 1000
    print(get_most_similar(avlTree, str(imagehash.dhash(Image.open(item)))).pBucket)
    execTime = time.time() * 1000 - startTime
    print("Execution time:", execTime)

print(":::::::Check transform changes:::::::")
directoryAsStr = "C:/Users/Ronan/Documents/TH_Köln/Algorithmik/Praktikum/Praktikum_1/101_ObjectCategories/transforms/"
directory = os.fsencode(directoryAsStr)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileDirectory = directoryAsStr + filename
    print(file)
    print("Hashvalue: " + str(imagehash.dhash(Image.open(fileDirectory))))
