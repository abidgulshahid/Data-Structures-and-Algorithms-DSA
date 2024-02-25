
def hasDuplicateValue(array):
    steps = 0
    print("i, j, array[i] array[j ]")
    for i in range(len(array)): 
        for j in range( len(array)):
            steps = steps + 1
            if i != j and array[i] == array[j]:
                print(steps)
                return True
    print(steps)
    return False

arr = [1,2,3,4,5,6,6 ]
print(hasDuplicateValue(array=arr))


def HasDuplicateValue(lst):
    temp_array = []
    steps = 0
    for i in range(len(lst)):
        steps = steps + 1
        if temp_array[lst[i]] == None:
            print(steps)
            temp_array[lst[i]] = 1
        else: 
            
            print(steps)
            return True
    print(steps)
    
print(HasDuplicateValue(lst=[1,2,3,4,5,6,7,8]))