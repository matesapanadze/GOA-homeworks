car_information = {
    "name": "Jeep Compass",
    "year": "2019",
    "engine": "2.3"
}
print(car_information)

my_info = {
    "name": "Mate",
    "age": "15"
}

my_info.update({
    "surname": "Sapanadze",
    "email": "matesapanadze@gmail.com"
    })

print(my_info)

my_info["surname"] = "Sapanadze"; my_info["email"] = "matesapanadze@gmail.com"
print(my_info)

for x,y in my_info.items():
    print(x + ":", y)




new_dict = {}
for i in range(1,1001):
    new_dict[f"item_{i}"] = f"value {i}"
print(new_dict)
