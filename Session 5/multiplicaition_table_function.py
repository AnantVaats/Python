def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+2):
            print(i*j, end="\t")
        print()


multiplication_table(9)