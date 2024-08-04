txt = "My name is Mate"
txt_split = txt.split()
print(txt_split)
# split მეთოდი წინადადებაში შემავალ სიტყვებს გაყოფს ცალ-ცალკე სიტყვებად და სიის სახით გამოიყვანს ყველა სიტყვას

print(" ".join(txt_split))
# join მეთოდი აერთებს ლისტის ელემენტებს ერთ სტრინგად

print(txt.index("name"))
# index მეთოდი გაძლევს იმის საშუალებას, რომ გამოარკვიო სტრინგის ნებისმიერი ელემენტი რომელ ინდექსზე დგას



def manual_count(string):
    for x in range(len(string) + 1):
        count_char = 0
        count_char = count_char + x
    print(count_char)

manual_count("My name is Mate")


# islower() მეთოდი ამოწმებს ეს მოცემული სტრინგი არის დაწერილი პატარა ასოებით თუ არა, შემდეგ გამოიტანს bool-ს
fruit = "banana"
print(fruit.islower())

fruit_1 = "BANANA"
print(fruit.islower())
# ამ შემთხვევაში ეს გამოსახულება გამოიტანს False-ს, რადგან fruit_1-ის ცვლადში სტრინგი არის დიდი ასოებით ჩაწერილი

txt = "goa is best"
print(txt.islower())

# isupper() მეთოდი ამოწმებს ეს მოცემული სტრინგი არის თუ არა დიდი ასოებით ჩაწერილი, შემდეგ გამოიტანს bool-ს
print(fruit_1.isupper())

print(fruit.isupper())
# ამ შემთხვევაში ეს გამოსახულება გამოიტანს False-ს, რადგან fruit-ის ცვლადში სტრინგი არის პატარა ასოებით ჩაწერილი

# isnumeric() მეთოდი ამოწმებს სტრინგში ყველა სიმბოლო ნუმერულია თუ არა
str = "3344562526"
print(str.isnumeric())

str = "banana2009"
print(str.isnumeric())
# ამ შემთხვევაში ეს გამოსახულება გამოიტანს False-ს, რადგან str-ის ცვლადში სტრინგის ყველა სიმბოლო ნუმერაციას არ მოიცავს

str = "1121"
print(str.isnumeric())

str = "Goa"
print(str.isnumeric())

# isalpha() მეთოდი ამოწმებს სტრინგში არის თუ არა ყველა ასო მოცემული
str = "mate"
print(str.isalpha())

str = "salome1983"
print(str.isalpha())
# ამ შემთხვევაში ეს გამოსახულება გამოიტანს False-ს, რადგან str-ის ცვლადში სტრინგის ყველა სიმბოლო არ მოიცავს ასოებს


str = "GoaisBest"
print(str.isalpha())

str = "Mate Sapanadze"
print(str.isalpha())
# რადგანაც სტრინგში მოცემული სფეისი არ არის ალფაბეტიკური, ამ შემთხვევაშიც გამოიტანს False-ს

