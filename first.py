start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
times = int(input("Enter the number of times to repeat: "))
columns = int(input("Enter the number of columns: "))
s2 = start
flag = False
for k in range(start, end+1, columns):
    for i in range(1, times+1):
        for j in range(s2, s2+columns):
            if(j > end) :
                flag = True
                break
            print(f"{j}x{i} = {j*i} ", end = "\t")
        print()
        if flag:
            continue
    if flag:
        break
    s2 += columns
    # print()