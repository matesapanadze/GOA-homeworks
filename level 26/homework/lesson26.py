def array(nums_list):
    new_list = []
    for num in nums_list:
        if num % 2 == 0:
            new_list.append(int(num / 2))
        elif num % 2 == 1:
            new_list.append(int(num * 2))
    return new_list

print(array([1, 2, 3, 4]))
print(array([5, 10, 3, 5]))



