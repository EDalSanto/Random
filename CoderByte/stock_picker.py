def stock_picker(arr):
	"""
	Takes an array stock prices and findx max profit possible
	"""
	max_profit = 0
	for index,price in enumerate(arr[:-1]):
		buy_price = price
		for j in arr[index+1:]:
			sell_price = j
			if sell_price > buy_price:
				p = sell_price - buy_price
				if p > max_profit:
					max_profit = p
	return max_profit

arr = [45, 24, 35, 31, 40, 38, 11]
print stock_picker(arr) == 16
