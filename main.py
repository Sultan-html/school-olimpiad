# 1 задание
a = 5
b = 10
print(a + b)
# 2 задание
def summa():
    n_input = 5
    for i in range( n_input + 1):
        for n_input in range( i + 1):
            print(n_input + i + 5 , end=' ')
# summa()
# 3 задание
def square_number_ending_in_5(num):

    if num % 10 != 5:
        return "Число не оканчивается на 5!"


    base = num // 10
    result = base * (base + 1)


    return int(f"{result}25")

#
# number = int(input("Введите число, оканчивающееся на 5: "))
# print(f"Результат: {square_number_ending_in_5(number)}")
# # square_number_ending_in_5()
#
# num = int(input('Введите первое число для сравнения>> '))
# num_2 = int(input('Введите второе число для сравнения>> '))
# if num >= num_2:
#     print(f'число {num} больше числа {num_2}!')
# elif num <= num_2:
#     print(f'число {num} меньше числа {num_2}!')
# elif num == num_2:
#     print('числа равны!')
# else:
#     print('Пишите корректно!')
#



