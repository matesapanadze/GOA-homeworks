i = 20
while i >= 1:
    print(i)
    i = i - 1


i = 0
while i <= 10:
    print(i)
    i = i + 2

i = 1
sum = 0

while i <= 10:
    print(sum)
    sum = sum + i
    i = i + 1

correct_password = "mate1234"
user_input = ''
while user_input != correct_password:
    user_input = input("please enter the password: ")

    if user_input == correct_password:
     print("password is correct")
    else:
      print("password is incorrect")


i = 1
while i <= 9:
   print(i)
   i = i + 2


age = 0
while age <= 18:
    age = int(input("please enter your age: "))
    if age >= 18:
     print("You succesfully signed in this program")
    else:
     print("You can't sign in this program")

day = int(input("please enter the number: "))
if day == 1:
    print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("You Lost")

num = int(input("please enter the number, in order to find out, this number is odd or even: "))
if (num % 2) == 0:
    print("this number is even")
else:
    print("this number is odd")

user_age = int(input("please enter your age: "))
if user_age >= 5 and user_age <= 13:
    print("You are a child")
elif user_age >= 13 and user_age <=18:
    print("You are teenager")
else:
    print("You are an adult")

user_age = int(input("please enter your age: "))
if user_age > 18:
    print("You can take part in the election")
else:
    print("You can't participate in the election")




 



























 






    
    


