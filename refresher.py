ref1 = 100
ref2 = 200

ref_total = [ref1, ref2]
food = "ice-cream"

if ref1 < 150:
	print("Noh")

else:
	print("Yas")


ref3 = {"Number": ref_total, "Food": food}

def nameFunc(one,two):
	print("{},{},buckle my shoe.".format(one,two))

raise Exception(SystemExit)

try:
	#YOURCODEHERE
except Exception:
	#your workaround here

for i in range(5):
	nameFunc(i,i+1)