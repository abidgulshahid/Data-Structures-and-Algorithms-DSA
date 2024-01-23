array = []
for i in range(5):
    take_input = input("Value: ")
    array.append(take_input)

while True:
    remove_array = input("Remove Value? (y/n): ")
    if remove_array.lower() == "y": 
        if not array:
            print("Stack is empty")
        else:
            removed_value = array.pop()
            print("Removed Value: ", removed_value)
            print("Current Stack: ", array)


    elif remove_array.lower() == 'n':break
    else: print("Invalid Input. Please Enter 'y' or 'n'")

print("Final Array: ",array)
print("The time complexity of this algorith is: O(1) Constant TIme")