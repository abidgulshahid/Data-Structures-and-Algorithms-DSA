
def hasDuplicateValue(array):
    steps = 0
    existingNumbers = list()
    for i in range(len(array)):
       print(array[i])
       print(existingNumbers[array[i]])
    return False

arr = [1,2,3,4,5,6,6]
print(hasDuplicateValue(array=arr))