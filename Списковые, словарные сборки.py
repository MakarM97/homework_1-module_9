my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = [x ** 2 for x in my_list if x % 2]
print(list(result))