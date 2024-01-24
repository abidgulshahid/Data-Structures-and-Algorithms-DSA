def binary_search(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        midpoint = int((start + end) / 2)

        print(midpoint)
        value_at_midpoint = array[midpoint]
        print('value_at_midpoint', value_at_midpoint)
        if value < value_at_midpoint:
            print("LESS THAN", value_at_midpoint)
            end = midpoint - 1
            print("END", end)
        elif value > value_at_midpoint:
            print("> MID", value_at_midpoint)
            start = midpoint + 1
            print("START", start)
        else:
            return value_at_midpoint
    return "Not Found"


array = [1, 2, 3, 4, 5, 6, 77, 88]
print(binary_search(array=array, value=77))
