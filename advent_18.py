import numpy as np

list = [[2,2,2],[1,2,2],[3,2,2],[2,1,2],[2,3,2],[2,2,1],[2,2,3],[2,2,4],[2,2,6],[1,2,5],[3,2,5],[2,1,5],[2,3,5]] 
list1 = [[1,1,1],[1,1,2],[1,1,3],[1,2,1],[1,2,2],[1,2,3],[1,3,1],[1,3,2],[1,3,3],
        [2,1,1],[2,1,2],[2,1,3],[2,2,1],[2,2,3],[2,3,1],[2,3,2],[2,3,3],
        [3,1,1],[3,1,2],[3,1,3],[3,2,1],[3,2,2],[3,2,3],[3,3,1],[3,3,2],[3,3,3]]
x = np.shape(list1)
num_blocks = x[0]
sides = np.arange(num_blocks)
for i in range(0,num_blocks):
    sides[i] = 6
for i in range(0,num_blocks):
    arr1 = list1[i]
    for j in range(0,num_blocks):
        arr2 = list1[j]
        if j != i:
            if arr2[0] == arr1[0] and (arr2[2] == arr1[2]):
                if (arr2[1] + 1 == arr1[1]) or (arr2[1] - 1 == arr1[1]):
                    sides[i] = sides[i] - 1
            elif arr2[0] == arr1[0] and (arr2[1] == arr1[1]):
                if (arr2[2] + 1 == arr1[2]) or (arr2[2] - 1 == arr1[2]):
                    sides[i] = sides[i] - 1
            elif arr2[1] == arr1[1] and (arr2[2] == arr1[2]):
                if (arr2[0] + 1 == arr1[0]) or (arr2[0] - 1 == arr1[0]):
                    sides[i] = sides[i] - 1
total=0
for i in range(0,num_blocks):
    total = total + sides[i]
print(total)

