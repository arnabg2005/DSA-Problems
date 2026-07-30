row=int(input("Enter the number of rows : "))
for i in range(row):
    for j in range(row-i):
        print("* ",end='')
    print()