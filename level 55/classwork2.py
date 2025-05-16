def captainjack(gold_coin):
    ships_price = [ 150, 200, 250, 300, 350 ]
    for price in ships_price:
        if price > gold_coin:
            return "გემი აჯანყდება"
        else:
            return "იყიდა გემი"
        

print(captainjack(150))