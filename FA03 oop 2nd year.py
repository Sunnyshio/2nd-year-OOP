number = input().split()
numbers = list(number)

WinningDigits = {10,11,8,1,5,20}
WinningCount = money = 0

un = numbers[0]
numbers.pop(0)

def NoDuplicates(numbers):
    if len(numbers) != len(set(numbers)):
        return True
    else:
        return False

if len(numbers) == 6:
    if NoDuplicates(numbers) == False:
        UniqueNumber = set(int(n) for n in numbers)
        Lottery = UniqueNumber.intersection(WinningDigits)
        for num in Lottery:
            money = money + 100
            WinningCount = WinningCount + 1
        if WinningCount >= 1:
            print(f"{un} won {money} pesos!")
        else:
            print(f"{un} won nothing!")
    else:
        print("No Duplicates")
else:
    print("Should be 6 numbers")
