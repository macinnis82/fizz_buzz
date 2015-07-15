n=100
print("Fizz buzz counting up to {0}".format(n))

for n in range(1,n):
    # while n % 3 != 0 & n % 5 != 0:
    #     print(n)
    if (n % 3 == 0 and n % 5 == 0):
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)