def find_major_element(test_string):
    list_for_checking = range(100)
    test_numbers = test_string.split(",")
    half_of_numbers_list_length = (len(test_numbers) / 2.0)

    for number in list_for_checking:
        counter = 0
        for number_to_check in test_numbers:
            if int(number_to_check) == int(number):
                counter += 1
        if counter > half_of_numbers_list_length:
            return number
    return "None"

example_1 = "92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19,21,21,21,19,19,19"

print find_major_element(example_1)
