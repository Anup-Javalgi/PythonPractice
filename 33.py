# 2D Keypad of calculator

num_pad = ( ('AC', '%', 'CE', '÷'),
            (7   , 8  , 9   , 'x'),
            (4   , 5  , 6   , '-'),
            (1   , 2  , 3   , '+'),
            ('^' , 0  , '.' , '=') )

print("<-------KEYPAD------->")
for row in num_pad:
    for item in row:
        print(item, end="  ")
    print()