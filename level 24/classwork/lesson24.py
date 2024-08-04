statement = "my name name is mate"
print(statement.capitalize())
# capitalize მეთოდი სტრინგში პირველ სიმბოლოს გაადიდებს

statement1 = statement.upper()
print(statement1)
# upper მეთოდი სტრინგის ყველა სიმბოლოს გაადიდებს

print(statement1.lower())
# lower მეთოდი სტრინგში მოცემულ დიდ სიმბოლოებს დააპატარავებს

print(statement.count("name"))
print(statement.count("name",6,12))
# count მეთოდი ითვლის მეთოდის ფრჩხილებში მოცემული სტრინგი რამდენჯერ არის ჩასმული წინადადებაში

print(statement.title())
# titile მეთოდი წინადადებებში მოცემულ ყველა სიტყვის პირველ ასოს გაადიდებს
# 