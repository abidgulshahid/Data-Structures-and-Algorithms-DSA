'''

LINEAR SEARCH IMPLEMENTATION


'''
def linear_search_on_ordered_list(array, value):
    counter = 0
    for arr in array:
        counter = counter + 1 
        if arr == value: 
            return (counter, value)
        elif arr > value: 
            break
    return "Not Found"


array = [11,22,33,44,55,66,77,88]
print(linear_search_on_ordered_list(array=array, value=77))