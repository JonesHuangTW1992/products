# 這記帳程式讓使用者重複輸入商品名稱，表示他購買過的東西
# 要重複輸入表示要用迴圈
# while loop 比 for loop 更適合用在， 不知道要用幾次的情況
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格: ') # 寫在break下的原因，若名稱輸入q，則不會再跳出這句	
	products.append([name, price]) # 為下列的縮寫
	# p = [] 
	# p.append(name)
	# p.append(price)
	# products.append(p) # p清單裝進products清單
# 二微清單 = 清單中還有清單
print(products)

# 存取二維清單
# product[0][1] # products清單中的第0格中的第1格

# for loop
for p in products:
	print(p)
	print(p[0], '的價格是', p[1])

