cars = []

for car in range(5):
    car = "jeep"
    cars.append(car)
    print(car)
    print(cars)

musics = ["radioactive", "save your tears", "eyes closed"]
fav_music = musics[0]
print(fav_music)

user_info = ["mate", "sapanadze", "january", 7, 2009]
user_info[4] = 15
print(user_info)

fav_fruits = ["apple", "banana", "apricot", "grapes", "orange"]
fav_fruits.append("peach")
fav_fruits.pop(1)
print(fav_fruits)

#max
numbers = [4,3,8,5,7,6]

max_num = numbers[0]
for number in numbers:
    if max_num < number:
        max_num = number 
print(max_num)


#min
numbers = [4,3,8,5,7,6]
min_num = numbers[0]
for number in numbers:
    if min_num > number:
        min_num = number 
print(min_num)

#sum
numbers = [1,2,3,4,5]
sum = 0
for number in numbers:
    sum = sum + number
print(sum)

names = ["mate", "ioane", "martha" "martha", "mate", "ioane", "ioane", "martha", "mate"]
count = 0
for name in names:
    if name == names[0]:
        count = count + 1
        
print(count)

numbers = [1,2,3,4,5]
numbers.pop(4)
numbers.pop(0)
print(numbers)











  
        






