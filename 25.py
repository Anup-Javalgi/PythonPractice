# for loop in python

#for to print num from 1 to 10
for i in range(0, 11):
    print(11-(i+1))
print("Happy new year!")

for i in range(1, 11, 2):
    print(11-i)
print("Happy new year!")

credit_card_num = "1234-5678-9012-3456"
for x in credit_card_num:
    print(x)
    # break

for x in range(1, 21):
    if x==13:
        continue
    elif x==20:
        break
    else:
        print(x)