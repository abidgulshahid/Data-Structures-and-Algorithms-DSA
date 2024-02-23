
def hasDuplicateValue(array):
    steps = 0
    for i in range(len(array)): 
        for j in range( len(array)):
            steps = steps + 1
            print(i, j, array[i] , array[j])
            if i != j and array[i] == array[j]:
                print(steps)
                return True
    print(steps)
    return False

arr = [1,2,3,4,5,6 ]
print(hasDuplicateValue(array=arr))