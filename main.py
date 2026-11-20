#Marshon Sellers 11/20/2026
print("Welcome to the Currency Converter!")
pesos = int(input("What do you have left in pesos?: "))
soles = int(input("What do you have left in soles?: "))
reais = int(input("what do you have left in reais:  "))

#Convert into USD
usd_pesos = pesos * 0.000291752
usd_soles = soles * 0.28931
usd_reais = reais * 0.168093

#Get the total amount in USD

currency = usd_pesos + usd_soles + usd_reais

print(f"You have ${currency:.2f} left to spend!")


