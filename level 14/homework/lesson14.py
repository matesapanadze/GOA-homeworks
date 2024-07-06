numbers = [1,2,3,4,5,6]
last_num  = numbers.pop()
print(last_num)

names = ["lile", "nia", "lizi", "mari"]
index = 0
popped_value = names.pop(0)
print(names)
new_index = 0
names.insert(new_index, popped_value)
print(names)

tuples = [("banana",), ("chery",), ("blackberry",), ("blueberry")]
tuples.pop(0)
print(tuples)


nums = [1,2,3,4,5,5,5,4,3,2,3,4,5,5,5]
print(nums.count(5))

name = input("name: ")
print(len(name))


nums = [1,2,3,4,5,6,7,8,9,10,12,34,43,12]
min_num = min(nums)
print(min_num)


nums = [1,2,3,4,5,6,7,8,9,10,12,34,43,0,12]
min_num = nums[0]
for num in nums:
    if min_num > num:
        min_num = num
    
print(min_num)

nums = [1,2,3,7,6,8,0]
print(min(nums))

nums = [1,2,3,7,6,9,8]
max_num = nums[0] 
for num in nums:
    if max_num < num:
      max_num = num
print(max_num)

   
















