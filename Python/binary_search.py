def binary_search(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        midpoint = int((start + end) / 2)

        value_at_midpoint = array[midpoint]
        if value < value_at_midpoint:
            end = midpoint - 1
        elif value > value_at_midpoint:
            start = midpoint + 1
        else:
            return value_at_midpoint
    return "Not Found"


array = [3,5,7,8,11,12,22,33,34,56]
print(binary_search(array=array, value=7))
