nums = [21,43,87,65]
min_num = nums[0]
for num in nums:
    if min_num >= num:
        min_num = num
print(min_num)

nums = [12,23,14,15]
max_num = nums[0]
for num in nums:
    if max_num <= num:
        max_num = num
print(max_num)

phone_brands = ["iphone", "samsung", "blackberry", "nokia", "huawei", "xiaomi"]
print(phone_brands[1])
print(phone_brands[-3])
print(phone_brands[5])

int_lists = [11,22,45,66,54]
str_lists = ["porsche", "jeep", "bmw", "mercedes", "lamborghini"]
new_list = []
new_list.append(str_lists[0])
new_list.append(int_lists[0])
new_list.append(str_lists[1])
new_list.append(int_lists[1])
new_list.append(str_lists[2])
new_list.append(int_lists[2])
new_list.append(str_lists[3])
new_list.append(int_lists[3])
new_list.append(str_lists[4])
new_list.append(int_lists[4])
print(new_list)


lists = ["clothes","shoes","trainers", 5,10,15,20,25]
str_lists = lists[:3]
int_lists = lists[3:]
print(str_lists)
print(int_lists)

nums1 = [11,12,13,14,15,16,17,18,19]
nums2 = [21,22,23,24,25,26,27,28,29]
nums3 = [31,32,33,34,35,36,37,38,39]
nums4 = [41,42,43,44,45,46,47,48,49]
sum = 0
for num in nums1:
    if (num % 2) == 0:
        even_num = num
        sum = sum + even_num
print(sum)
sum = 0       
for num in nums1:
    if (num % 2) == 1:
        odd_num = num
        sum = sum + odd_num
print(sum)
sum = 0
for num in nums2:
    if (num % 2) == 0:
        even_num = num
        sum = sum + even_num
print(sum)
sum = 0
for num in nums2:
    if (num % 2) == 1:
        odd_num = num
        sum = sum + odd_num
print(sum)
sum = 0
for num in nums3:
    if (num % 2) == 0:
        even_num = num
        sum = sum + even_num
print(sum)
sum = 0
for num in nums3:
    if (num % 2) == 1:
        odd_num = num
        sum = sum + odd_num
print(sum)
sum = 0
for num in nums4:
 if (num % 2) == 0:
        even_num = num
        sum = sum + even_num
print(sum)
sum = 0
for num in nums4:
 if (num % 2) == 1:
        odd_num = num
        sum = sum + odd_num
print(sum)






        

