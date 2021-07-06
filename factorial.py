# find the factorial of a number using recursion

def factorial(num):
    # if the given value is 1 then the output value is value
    if num == 1:
        return 1

    # if not 1 then calculate the factorial using the recursion method e.g 3(1st)*2(2nd)*1(3rd)
    # repeats the function factorial until the number is equals to 1 and returns the final output
    else:
        return num * factorial(num-1)

# enter the any number from the user end
value = int(input("Enter any number to find the factorial of that particular num: "))
print(factorial(value))