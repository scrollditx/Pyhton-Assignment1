# WAP to create a two level of Indentation.

x = int(input("Enter a number: "))

if x > 10:
    print("Stage 1: X is greater than 10")
    if x > 20:
        print("Stage 2: X is greater than 20")
    else:
        print("Stage 2: X is between 10-20")
else:
    print("Stage 1: X is 10 or less")
    if x < 5:
        print("Stage 2: X is between 5-10")
    else:
        print("Stage 3: X is 5 or less")