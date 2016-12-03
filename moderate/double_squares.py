def double_square(X):
    numbers = range(0,2000)
    counter = 0
    for a in numbers:
        for b in numbers:
            if int(X) == (a ** 2) + (b ** 2):
                counter += 0.5
    if counter == 0.5:
        return 1
    else:
        return counter

print double_square("2500")