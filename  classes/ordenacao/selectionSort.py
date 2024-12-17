def selectionSort(array, size):
    
    for ind in range(size - 1):
        min_index = ind
        max_index = size-1
 
        for j in range(ind + 1, size):
            
            if array[j] > array[max_index]:
                max_index = j

            if array[j] < array[min_index]:
                min_index = j   
        
        (array[max_index], array[ind]) = (array[max_index], array[ind])
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)