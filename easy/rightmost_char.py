def find_rightmost_char(test_string):
    char = str(test_string.split(',')[1])
    reversed_word = test_string.split(',')[0][::-1]
    for letter in reversed_word:
        if letter == char:
            print str((len(reversed_word) - 1) - (reversed_word.index(char)))
            break
    else:
        print "-1"
find_rightmost_char("What is your name,m")