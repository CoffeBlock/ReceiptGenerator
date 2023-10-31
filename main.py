item = []
itemPrice = []
itemUnit = []
itemAmount = []
itemlist = 0
price = []
itemx = 0
itemy = 0

with open("item.txt", "r") as item:
	item = item.readlines()

item = [i.replace('\n','') for i in item]

with open("itemPrice.txt", "r") as itemPrice:
	itemPrice = itemPrice.readlines()

itemPrice = [i.replace('\n','') for i in itemPrice]

with open("itemUnit.txt", "r") as itemUnit:
	itemUnit = itemUnit.readlines()

itemUnit = [i.replace('\n','') for i in itemUnit]

with open("itemAmount.txt", "r") as itemAmount:
	itemAmount = itemAmount.readlines()

itemAmount = [i.replace('\n','') for i in itemAmount]

def CalPrice():
	global itemlist
	global price
	itemx = itemPrice[itemlist]
	itemy = itemAmount[itemlist]
	itemx = float(itemx)
	itemy = float(itemy)
	price.append(itemx * itemy)	

def PrintReceipt():
	CalPrice()
	global itemlist
	global price
	out = f"{item[itemlist]} {itemUnit[itemlist]} {itemPrice[itemlist]}   |    {itemAmount[itemlist]}     |    {price[itemlist]}"
	print(out)
	out = f"{item[itemlist]} {itemUnit[itemlist]} {itemPrice[itemlist]}   |    {itemAmount[itemlist]}     |    {price[itemlist]}\n"
	f.write(out)
	

print("Store info:".center(53))
print("name: SweetyMart".center(53))
print("address: 123321 Funny St, Farmland, V0V 4N4".center(53))
print("tel:604-555-1234".center(53))
print("website: www.sweetymark.ca".center(53))
print("".center(53))
print("".center(53))
print("Cashier ID: goody-mark".center(53))
print("Date time also should be on the receipt".center(53))
print("".center(53))
print("*****************************************************")
print("Item        | Unit    | Price  |  Amount  |    Total")

with open('Receipt.txt', 'w') as f:
	f.write("Store info:".center(53) + "\n")
	f.write("name: SweetyMart".center(53) + "\n")
	f.write("address: 123321 Funny St, Farmland, V0V 4N4".center(53) + "\n")
	f.write("tel:604-555-1234".center(53) + "\n")
	f.write("website: www.sweetymark.ca".center(53) + "\n")
	f.write("".center(53) + "\n")
	f.write("".center(53) + "\n")
	f.write("Cashier ID: goody-mark".center(53) + "\n")
	f.write("Date time also should be on the receipt".center(53) + "\n")
	f.write("".center(53) + "\n")
	f.write('*****************************************************\n')
	f.write('Item        | Unit    | Price  |  Amount  |    Total\n')

	
	while not itemlist == 6:
		itemx = float(itemPrice[itemlist])
		itemy = float(itemPrice[itemlist])
		PrintReceipt()
		itemlist = itemlist +1
	f.write("*****************************************************\n")
	total = sum(price)
	f.write(f"                                               {total}\n")
print("*****************************************************")
total = sum(price)
print("                                              ", total)