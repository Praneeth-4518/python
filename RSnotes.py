def rs(amount):
    # Initialize counters
    n2k = n500 = n200 = n100 = n50 = n20 = n10 = 0

    if amount >= 2000:
        n2k = amount // 2000
        amount %= 2000

    if amount >= 500:
        n500 = amount // 500
        amount %= 500

    if amount >= 200:
        n200 = amount // 200
        amount %= 200

    if amount >= 100:
        n100 = amount // 100
        amount %= 100

    if amount >= 50:
        n50 = amount // 50
        amount %= 50

    if amount >= 20:
        n20 = amount // 20
        amount %= 20

    if amount >= 10:
        n10 = amount // 10
        amount %= 10

    totalnotes = n2k + n500 + n200 + n100 + n50 + n20 + n10
    print("Total notes in the amount:", totalnotes)
    print(f"2000 x {n2k}, 500 x {n500}, 200 x {n200}, 100 x {n100}, 50 x {n50}, 20 x {n20}, 10 x {n10}")
rs(int(input("amount:")))    

                       
                                                


