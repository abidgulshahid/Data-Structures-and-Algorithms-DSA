
def binary_search(array, value): 
    l = 0
    h = len(array) - 1
    while l <= h:
        mid = l+ (h-l) / 2 # Mid index
        midpoint = array[int(mid)] # mid value
        print(mid, midpoint)
        print(array[int(mid)] , value, 'array[int(mid)] == value')
        if array[int(mid)] == value:
            return mid
        elif  array[int(mid)] > value: 
            l = mid  + 1
        elif  array[int(mid)] < value:  
            h  = mid - 1 
    return -1


array = [5,7, 9,13,32,33 ,42, 54, 56, 88]
print(binary_search(array=array, value= 88))