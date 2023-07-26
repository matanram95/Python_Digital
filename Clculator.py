tomato = 3
cucumber = 2
cola = 5
chicken = 20
Welcome = input("Hello to my store, \n What is your name: ")
print("Nice to see you " + Welcome)
Tometo = int(input("How many tomatoes would you like?:\nThe price is three shekels per kilo: ")) * 3
Cucumber = int(input("How many Cucumber would you like?:\nThe price is Two shekels per kilo: ")) * 2
Cola = int(input("HHow many bottles of Coke would you like?:\nThe price is five shekels per bottle: ")) * 5
Chicken = int(input("How many kilos would you like to buy chicken?")) * 20
Summary = str(Tometo + Cucumber + Cola + Chicken)
print("You bought products in the amount of " + Summary + " shekel before VAT and after VAt")
Vat = 0.17 * float(Summary)
print(int(Vat) + int(Summary))
