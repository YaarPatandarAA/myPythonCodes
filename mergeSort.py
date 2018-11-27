#Taken from https://www.geeksforgeeks.org/merge-sort/
#TODO: Comments added to understand what is happening

def mergeSort(arr):
    if len(arr) > 1:        #check is arr has elements
        mid = len(arr)/2    #decide middle of array

        left = arr[:mid]    #split array
        right = arr[mid:]   #left and right

        mergeSort(left)     #recursive call on left
        mergeSort(right)    #and right to split to one element

        i = j = k = 0

        while i < len(left) and j < len(right):     #merge array
            if left[i] < right[j]:                  #is array still in bounds
                arr[k] = left[i]                    #copy over from right or left side
                i+=1                                #which ever is smaller
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len(left):                        #copy over remainer elements
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1



arr = [21, 4, 1, 3, 9, 20, 25]
print arr

mergeSort(arr)
print arr