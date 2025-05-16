def even_or_odd(number):
    return lambda number: "Even" if number % 2 == 0 else "Odd"
    

print(even_or_odd(2))