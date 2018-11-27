import random

def bubbleSort(array):
    j = 0
    while j < (len(array) - 1):
        print array
        for i in range(len(array)-1):
            if array[i] >= array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
        
        j+=1

    print array

# elements = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 0, 15, 5, 5, 5, 5, 5]
# bubbleSort(elements)

ele = []
for i in range(10):
    ele.append(random.randint(0,36))
bubbleSort(ele)