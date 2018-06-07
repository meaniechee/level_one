# print 1-100
# multiples of 3, print "fizz"
# multiples of 5, print "buzz"
# multiples of 3 & 5, print "fizzbuzz"


for i in range(1,100):

	if i%3 and i%5 == 0:
		print("fizzbuzz")

	elif i%3 == 0:
		print("fizz")

	elif i%5 == 0:
		print("buzz")

	else:
		print("The number is {}".format(i))
