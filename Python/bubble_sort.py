def bubble_sort(list): 
    unsorted_until_index = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
                print(list)          
        unsorted_until_index = unsorted_until_index - 1



list = [25,23,21,15,10,5]
bubble_sort(list=list)
