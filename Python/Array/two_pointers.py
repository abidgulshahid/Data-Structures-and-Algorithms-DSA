def TwoSum(num, target): 
    left, right= 0, len(num) -1
    while left < right:
        print(num[left], num[right])
        if num[left] + num[right] == target:
            return [left, right]
        elif num[left] + num[right] < target:
            left += 1
        else:
            right -= 1
    return False

num = [2,7,11,15]
target = 17
print(TwoSum(num, target))