# R3
play = True
while (play == True):
    try:
        num = int(input("enter number"))
    except ValueError:
        num = int(input("enter integer number"))

    if num <= 0:
        try:
            num = int(input("enter number"))
        except ValueError:
            num = int(input("enter integer number and bigger then 0"))
    else:
        print("number vailod")
        play = False

#R1
def recursive(num):
    if num ==0 or num==1:
        print("number is 0 or 1 out of function")
        return num
    else:
        num = num - 1
        print(num)
        recursive(num)

recursive(num)

#R2
f = 1
def factorial(num):
    global f
    if num ==0 :
        print(f" = {f}")
        return f
    else:
        f = f * num
        # print(f"factorial {f}")
        num = num - 1
        print(f" {num+1}", end="")
        factorial(num)

factorial(num)






