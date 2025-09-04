def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==2 or j==2:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
pattern(int(input("enter a +ve number:"))) 