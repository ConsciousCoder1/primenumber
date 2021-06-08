print('''
  __ ______ 
 /_ |____  |
  | |   / / 
  | |  / /  
  | | / /   
  |_|/_/    
             ''')

print("\nWelcome to PyPrime Number Checker!\n")

number = int(input("To check if a number is prime, provide a number:  "))


def check_number(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    
    if prime == True:
        print(f"{number} is a prime number.")
    if prime == False:
        print(f"{number} is NOT a prime number.")

check_number(number = number)
