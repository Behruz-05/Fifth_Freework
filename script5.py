yourpurchase = int(input("Enter your purchase amount: "))
twentydiscount = 1/5 * yourpurchase
finalpurchasetwenty = yourpurchase - twentydiscount
tendiscount = 1/10 * yourpurchase
finalpurchaseten = yourpurchase - tendiscount
if yourpurchase >= 100: print(f"Total purchase with discount: {finalpurchasetwenty}")
if yourpurchase >= 50: print(f"Total purchase with discount: {finalpurchaseten}")
else: print(f"Total purchase: {yourpurchase}")