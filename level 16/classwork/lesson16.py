names = ["mate", "salome", "saba", "davit", "mari"]
print(names[1:4])


lists = [5,4,3,"mate", 1.5, "apple", True, False]
print(lists)
lists_half = lists[:4]
new_lists = []
new_lists.append(lists_half)
print(new_lists)


lists = ["computer", "phone", "IPad", 3, 1.4, False]
print(lists.index(lists[0]))
print(lists.index(lists[1]))
print(lists.index(lists[2]))


nums = [1,2,3,4,5]
max_num = max(nums)
min_num = min(nums)
max_num_index = nums.index(max_num)
min_num_index = nums.index(min_num)
nums.pop(max_num_index)
print(nums)
nums.pop(min_num_index)
print(nums)
new_lists = []
new_lists.append(max_num)
new_lists.append(min_num)
print(new_lists)

first_ints = [22, 33, 12, 24, 50, 45, 19,]
second_ints = [10, 23, 78, 67, 90, 70, 34 ]
max_num1 = max(first_ints)
max_num2 = max(second_ints)
min_num1 = min(first_ints)
min_num2 = min(second_ints)
new_int1 = max_num1 - min_num1
new_int2 = max_num2 - min_num2
new_list = []
new_list.append(new_int1)
new_list.append(new_int2)
print(new_list)

nums = [10,20,30,40,50,60,70,80,90]
sum = 0
for num in nums:
    sum = sum + num
print(sum)

lists = ["hot", "dog", 5, 7, 20, 34, 12, 28]
str_lists = lists[:2]
new_str  = ""
for str in str_lists:
    new_str = new_str + str
print(new_str)
int_lists = lists[2:]
sum = 0
for num in int_lists:
    sum = sum + num
print(sum)


first_nums = [100,200,300,400,500,600,700,800,900]
second_nums = [12,34,56,78,21,31,45,36]
sum1 = 0
sum2 = 0
for num1 in first_nums:
    sum1 = sum1 + num1
print(sum1)
for num2 in second_nums:
    sum2 = sum2 + num2
print(sum2)

lists = ["mate", "gigi", "lile", "ioane"]
reversed_lists = []
for i in range(len(lists) -1, -1, -1):
    reversed_lists.append(lists[i])
print(reversed_lists)

lists = ["mate", "gigi", "lile", "ioane"]
print(lists[::-1])

str = "mate"
reversed_str = ""
for i in range(len(str) -1,-1,-1):
    reversed_str = reversed_str + str[i]
print(reversed_str)


str = "ioane"
print(str[::-1])
  



    


