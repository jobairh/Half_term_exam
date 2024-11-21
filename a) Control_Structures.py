
for a in range(15):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
        continue
    elif a % 3 == 0:
        print("Fizz")
        continue
    elif a % 5 == 0:
        print("Buzz")
        continue
    else:
        print(a) 