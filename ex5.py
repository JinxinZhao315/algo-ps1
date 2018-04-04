# Type your code for insertion sort (Exercise 5) here
numbers_str = input('Type a list of numbers you want to sort, seperated by comma: ')
numbers_list = []


for char in numbers_str.split(','):
    numbers_list.append(int(char))


for j in range(1,len(numbers_list)):
    key = numbers_list[j]
    i = j - 1
    while i >= 0 and numbers_list[i]>key:
        numbers_list[i+1] = numbers_list[i]
        i -= 1
    numbers_list[i+1] = key

print(numbers_list)

