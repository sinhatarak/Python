num = 0
tot = 0.0
while True :
    sval = input("Enter a No.: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print("Invalid data")
        continue
    num = num + 1
    tot = tot + fval
print(tot,num,tot/num)
