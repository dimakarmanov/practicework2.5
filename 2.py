def sum_and_product():
    input_array = input("Введите числа через пробел: ")
    numbers = list(map(int, input_array.split()))

    positive_sum = sum(num for num in numbers if num > 0)

    max_num = max(numbers)
    min_num = min(numbers)
    max_index = numbers.index(max_num)
    min_index = numbers.index(min_num)

    if max_index < min_index:
        start_index = max_index + 1
        end_index = min_index
    else:
        start_index = min_index + 1
        end_index = max_index

    product = 1
    for i in range(start_index, end_index):
        product *= numbers[i]

    return positive_sum, product

sum_positive, product_between = sum_and_product()
print("Сумма положительных элементов: ", sum_positive)
print("Произведение чисел между минимальным и максимальным элементами: ", product_between)