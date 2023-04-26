numbers = [1, 1, 2, 3, 5, 8, 13, 25, 34, 55]

# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

result = [num for num in numbers if num % 2 == 0]
print(result)