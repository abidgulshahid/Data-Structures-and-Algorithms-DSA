
def hasDuplicateValue(array):
    for i in range(len(array)): 
        for j in range( len(array)):
            print(i, j, array[i] , array[j])
            if i != j and array[i] == array[j]:
                return True
    return False

arr = [1,2,3,4,5,6,6 ]
print(hasDuplicateValue(array=arr))