def fizz_buzz(test):
    fizz, buzz, limit = (int(i) for i in test.split())
    for i in range (1, limit + 1):
        if i % fizz == 0 and i % buzz == 0:
            print "FB",
        elif i % fizz == 0:
            print "F",
        elif i % buzz == 0:
            print "B",
        else:
            print i,

example_1 = "15 9 56"

fizz_buzz(example_1)