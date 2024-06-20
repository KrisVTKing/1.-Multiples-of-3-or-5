# If we list all the natural numbers 10 below that are multiples of 3 or 5 , we get 3 ,5 ,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers = range(1000)

def sort_numbers(numbers):
    sum = 0
    for number in numbers:
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    print(sum)
           
sort_numbers(numbers)