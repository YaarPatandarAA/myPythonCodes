#Taken from https://www.geeksforgeeks.org/quick-sort/

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i += 1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low=0,high=None): 
    if high == None:
        high = len(arr)-1

    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

    return arr

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 0]
print quickSort(test)