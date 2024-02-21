def bubble_sort(list): 
    unsorted_until_index = len(list) - 1
    print(unsorted_until_index, 'unsorted_until_index')
    sorted = False
    while not sorted:
        sorted = True
        print(sorted, 'sorted')
        for i in range(unsorted_until_index):
            print(list[i],  list[i+1], 'list[i] > list[i+1]')
            if list[i] > list[i+1]:
                sorted = False
                print(list, 'before')
                list[i], list[i+1] = list[i+1], list[i]
                print("AFTER ", list)
        unsorted_until_index = unsorted_until_index - 1



list = [65, 55, 45, 35, 25, 15, 10]
bubble_sort(list=list)
print(list)