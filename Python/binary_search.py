
def binary_search(array, value):

    # first to know the length of a array
    lower_bound = 0
    high_bound = len(array) - 1 
    print(high_bound)
    while lower_bound <= high_bound: 
        print(high_bound, lower_bound)
        midpoint = (lower_bound + high_bound) / 2
        midpoint = int(midpoint)
        print(midpoint, 'midpount')
        value_at_midpoint = array[midpoint]
        print(value_at_midpoint, 'value at midpoint')
        
        if value < value_at_midpoint: 
            print(high_bound, midpoint , 'if')
            high_bound = midpoint + 1
        elif value > value_at_midpoint: 

            lower_bound = midpoint - 1
        
        elif value == value_at_midpoint:
            return value
        break
        
array = [2,4,5,7,8,9,66]
print(binary_search(array=array, value=9))