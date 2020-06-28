#9. Write a Python function that takes a number as a parameter and check the number is prime or not

def check_prime(my_num):
    print("Given number : %s" %my_num)
    if my_num > 1:
        for i in range(3, my_num):
            if(my_num % i == 0):
                return "Not Prime number"
        return "Prime number"
    else:
        return "Not Prime number"


print(check_prime(2345))

