#sort words to generate an output depended on the amount of k's and b's in the input.
#single input, if k's > b's = kiki. If b's > k = boba. if b's = k's = boki. if there's neither then = none.
x, y = input("").count("b", "k")
if x > y:
    print("boba")
if x < y:
    print("kiki")
if x == y:
    print("boki")