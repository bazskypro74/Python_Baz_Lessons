n = int(input("Введите число: "))
print(f"fizz_buzz({n}) →")


def fizz_buzz(n):
    for t in range(1, n+1):
        if (t % 3 == 0 and t % 5 == 0):
            print("FizzBuzz")
        elif t % 3 == 0:
            print("Fizz")
        elif t % 5 == 0:
            print("Buzz")
        else:
            print(t)


fizz_buzz(n)
