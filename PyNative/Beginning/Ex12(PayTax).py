income = int(input())

if income <= 10000: print("You don't have to pay taxes")
elif 10000<income<=20000:
    tax1 = (income-10000) * 0,1
    print("You have to pay ",tax1)
else:
    tax2 = 10000*0.1+(income-20000)*0.2
    print("You have to pay ",int(tax2)," USD")
