def print_even_nums(nums):
    even_nums = []
    for x in nums:
        if (x % 2) == 0:
            even_nums.append(x)
    return even_nums

print(print_even_nums([20,34,25,27,30,98,120,243]))
print(print_even_nums([12,13,14,15,18,34]))






