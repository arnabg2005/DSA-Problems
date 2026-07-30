row=int(input("Enter the number of rows : "))
ascii_value=65
for i in range(row):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(f"{alphabet} ",end='')
    ascii_value+=1
    print()