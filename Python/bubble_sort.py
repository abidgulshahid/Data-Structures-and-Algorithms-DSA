def bubble_sort(list): 
    unsorted_until_index = len(list) - 1
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
                counter = counter + 1
        unsorted_until_index = unsorted_until_index - 1
    print('Total Phases: ',counter)


list = [25,23,21,15,10,5]
bubble_sort(list=list)
print('Sorted Array: ',list)
