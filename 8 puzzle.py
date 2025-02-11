import numpy as np
import random
def create8puzzle():
    zeros = np.zeros((3, 3))
    list1 = [1,2,3,4,5,6,7,8,0]
    inversions = 1
    count = 0
    while inversions>0 and inversions%2 != 0:
        if inversions != 1:
            count+=1
        inversions=0
        random.shuffle(list1)
        for i in range(len(list1)):
            if list1[i]!=0:
                for j in range(i+1,len(list1)):
                    if list1[i]!=0:
                        if list1[i] > list1[j]:
                            inversions += 1

    for i in range(3):
        for j in range(3):
            zeros[i,j] = list1[i*3+j]
    print("Shuffled ",count," times")
    return zeros, count
max = 0
for i in  range(100):
    t,c = create8puzzle()
    if c > max:
        max = c
    print(t)
    print("----------------------")
    print()
print("Max shuffle count: ",max)


