array = []
intro_message = """
Add many valeus as you want

enter q to stop the program
"""


while True:
    take_input = input("Enter Value (q to stop): ") 
    if take_input == 'q': break
    elif take_input == 'd': 
        print('Current Array: ',array)
        array.pop(0)
    else:array.append(take_input)
    

print(array)