def run_ex1():
    numbers = ""
    for number in range(500, 3000):
        while number % 7 == 0 and number % 5 != 0:
            numbers += str(number)
            break
    counter = 0
    old_pattern = '21'
    new_pattern = 'xx'
    numbers_length = len(numbers)
    for number in range(numbers_length - 1):
        if old_pattern in numbers:
            numbers = numbers.replace(old_pattern, new_pattern, 1)
            counter += 1

    print(numbers)
    print(f"Liczba zamian: {counter}")
