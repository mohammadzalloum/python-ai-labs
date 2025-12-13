#R1
num = int(input("enter number"))
if num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0 and num % 3 == 0:
    print(f"number {num}  divisible by 5 and 3")


#R3
try:
    num = int(input("enter number"))
except ValueError:
    num = int(input("enter number not text"))
#R2
for num in range (1, num+1):
    if num%3 == 0:
        print("fizz")
    elif num%5 == 0:
        print("FizzBuzz")
    elif num%5 == 0 and num%3 == 0:
        print(f"number {num}  divisible by 5 and 3")
