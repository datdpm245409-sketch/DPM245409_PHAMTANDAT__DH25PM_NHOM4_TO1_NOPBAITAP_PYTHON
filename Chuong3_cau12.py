for i in range(1, 11):
    for j in range(2, 10):
        print(f"{j}*{i:>2}={i*j:>2}", end="\t")
    print()