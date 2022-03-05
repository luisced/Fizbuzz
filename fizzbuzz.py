# put 100 numbers in a list

li = [i for i in range(1, 101)]


for x in (li):

    if x % 5 == 0 and x % 3 == 0:
        li[x - 1] = "FizzBuzz"
    elif x & 3 == 0:
        li[x-1] = "Fizz"
    elif x % 5 == 0:
        li[x-1] = "Buzz"

print(li)


def fizzbuzz(n):
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(fizzbuzz(100))
