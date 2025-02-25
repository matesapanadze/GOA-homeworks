def math_position(x, position):
    arr=[]
    while x > 0:
        sum = x // position
        arr.append(sum)
    return arr

print(math_position(5,2))
