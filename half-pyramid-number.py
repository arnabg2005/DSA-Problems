row=int(input("Enter the number of rows : "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(f"{j}",end='')
    print()