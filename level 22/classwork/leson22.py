

# def greet():
#     print("Hello Mate!")

# greet()
# greet()
# greet()
# greet()


# def greet(name):
#     print("Welcome " + name)

# greet("Mate")

# # პითონში ჩაშენებული ფუნქციების გარდა ასევე შეგვიძლია შვქმნათ და ჩავამატოთ ჩვენს მიერ შექმნილი ფუნქციები
# # def - ის გამოყენებით ჩვენ შეგვიძ₾ია ვუთხრათ კომპიუტერს ამ ფუნქციის დეფინიციის, ანუ მნიშვნელობის შესახებ

def even_odd(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(str(number) + " is even")
        else:
            print(str(number) + " is odd")


even_odd([1, 2, 3, 4, 5, 6, 7])