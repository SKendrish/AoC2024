import numpy as np

def createNPArray(file):
    arr = []
    for line in data:
        temp = []
        for char in line:
            if char != "\n":
                temp.append(char)
        arr.append(temp)
    
    nparr = np.array(arr)
    return nparr

def createPoses(array, str):
    poses = np.where(array == str)

    Poses = []

    for i in range(len(poses[0])):
        row = int(poses[0][i])
        column = int(poses[1][i])
        mytuple = (row, column)
        Poses.append(mytuple)

    return Poses
        
def replaceElements(array, poses, str):
    for tuple in poses:
        array[tuple[0]][tuple[1]] = str

    return array


with open('example.txt', 'r') as f:
    data = f.readlines()

    npArray = createNPArray(data)

    XPoses = createPoses(npArray, "X")
    MPoses = createPoses(npArray, "M")
    APoses = createPoses(npArray, "A")
    SPoses = createPoses(npArray, "S")

    a = np.zeros((10,10), dtype=str)

    a = replaceElements(a, XPoses, 'X')
    a = replaceElements(a, MPoses, 'M')
    a = replaceElements(a, APoses, 'A')
    a = replaceElements(a, SPoses, 'S')

    print(a)




    

        
    
    