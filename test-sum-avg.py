def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average


numbers_list = []
number_of_input = int(input("Please enter the number of numbers you will input: "))
for _ in range(number_of_input):
    num = int(input("Enter a number: "))
    numbers_list.append(num)

print("Numbers list:", numbers_list)
total_sum, avg = sum_and_average(numbers_list)
print("Sum:", total_sum)
print("Average:", avg)
