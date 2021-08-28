number = input().split()
username = number[0]
numberlist = [10, 11, 8, 1, 5, 20]

NumberDuplicates = 0
money = 0

for x in number[1:6]:
    if int(x) in numberlist:
        NumberDuplicates += 1
    money = NumberDuplicates * 100

if len(number) > 7:
    print("Should be 6 numbers")

elif len(number) < 7:
    print("Should be 6 numbers")

elif len(number) != len(set(user)):
    print("No Duplicates")

elif NumberDuplicates >= 1:
    print(f"{username} won {money} pesos!")
else:
    print(f"{username} won nothing!")
