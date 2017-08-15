# tax calculator

# tax calc function
def tax_calc(income,tax):
	income = float(income)
	tax = int(tax)

	incomeAfterTax = income * (1-(tax/100))

	return incomeAfterTax

# ask user for input
print('What\'s your $$$?')
user_income = input()

print("Whut tax bracket?")
user_tax = input()

# calculate how much I owe ze government
try:
	result = tax_calc(user_income, user_tax)
	result2 = float(user_income) - result
	print("Grats! Your income is %.2f. You are now %.2f poorer." %(result,result2))
except Exception:
	print("Please input a valid number. :)")