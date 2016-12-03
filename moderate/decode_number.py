def decode_numbers(numbers):
    count = 1
    for idx, val in enumerate(numbers):
        if idx < len(numbers) - 1:
            combination = str(val) + str(numbers[idx+1])
            if int(combination) <= 26:
                count += 1
    if len(numbers) == 4:
        if int(numbers[0:2]) <= 26 and int(numbers[2:4]) <= 26:
            count += 1
    return count

print decode_numbers("1219")