person = {
    "name": "Mate",
    "age": 25,
    "city": "Kutaisi",
    "work": "programmer"
}

txt = f"{person["name"]} is {person["age"]} years old and works as a {person["work"]} in {person["city"]}"
print(txt)
 

lessons_table = {
    "Georgian": 9,
    "English": 10,
    "Math": 7,
    "Geography": 8
}
sum = 0
for x, y in lessons_table.items():
    sum = sum + y
print(sum / len(lessons_table.items()))


# Shopping Card Project
newdict = {}
for i in range(1,7):
    newdict[f"item_{i}"] = input(f"enter item {i}: ")
txt = "I wanna buy them:", newdict
print(txt)