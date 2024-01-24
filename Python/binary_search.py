
def binary_search(array, value): 
    l = 0
    h = len(array)
    while l <= h:
        mid = (l + h) / 2 
        midpoint = array[int(mid)]
        print(mid, midpoint)
        break;

array = [5,7, 9,13,32,33 ,42, 54, 56, 88]
print(binary_search(array=array, value= 42))