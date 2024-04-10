# 這記帳程式讓使用者重複輸入商品名稱，表示他購買過的東西
# 要重複輸入表示要用迴圈
# while loop 比 for loop 更適合用在， 不知道要用幾次的情況
products = []
# 讀取檔案
with open('products.csv', 'r', encoding = 'utf-8') as f:
	# 讀取___當作f
	for line in f:
		# f 檔裡的每一line
		if '商品,價格' in line:
			continue # 繼續
			# 如果____有出現在line裡的話則跳下一迴
		name, price = line.strip().split(',')
		# .strip() = 除掉換行符號(\n)
		# .split = 切割
		# 以','作為切割的標準
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格: ') # 寫在break下的原因，若名稱輸入q，則不會再跳出這句	
	price = int(price) # 價格設為整數而非字串
	products.append([name, price]) # 為下列的縮寫
	# p = [] 
	# p.append(name)
	# p.append(price)
	# products.append(p) # p清單裝進products清單
# 二微清單 = 清單中還有清單
print(products)

# 存取二維清單
# product[0][1] # products清單中的第0格中的第1格

# 印出所有購買紀錄
# for loop
for p in products:
	print(p[0], '的價格是', p[1])
# 字串可以合併
# 'abc' + '123' = 'abc123'
# 'abc' * '3' = 'abcabcabc'

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	# encoding = 使用___編碼
	# 打開並寫入 當作f 
	# csv檔可以用excel打開
	# w = write = 寫入, r = read = 讀取
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		# 用加法當作字串的合併，上面等於四個字串相加, 而後丟給f.write這個功能
		# str = string 改為字串
		# ',' 氏為了在csv檔內作分隔
		# '\n' 為換行功能
