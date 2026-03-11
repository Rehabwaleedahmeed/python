num = int(input("Enter number: "))
for i in range(num):
    print(" " * (num - i - 1), "*" * (i + 1))