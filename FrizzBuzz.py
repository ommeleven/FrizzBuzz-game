def fizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and  i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzz()

def ss(number_list, n):
    found = False

    for i in number_list:
        if i == n:
            found = True
            break
        return found

numbers = range(1, 101)
result = ss(numbers, 15)
print(result)


