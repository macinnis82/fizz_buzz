import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv))

try:
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            n = int(arg)
    else:
        n = int(raw_input("Please enter an upper limit to count to:  "))

    print("Fizz buzz counting up to {0}".format(n))
    
    for n in range(1,n):
        if (n % 3 == 0 and n % 5 == 0):
            print("fizz buzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        else:
            print(n)
        
except ValueError:
    print "The argument needs to an integer!"         