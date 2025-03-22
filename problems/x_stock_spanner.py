class StockSpanner:
	def __init__(self):
		self.history = []
		self.max = float("-inf")

	def next(self, price):
		if price >= self.max:
			span = len(self.history) + 1
			self.history.append([price, span])
			self.max = price
			return span

		span = 1
		idx = len(self.history) - 1
		while idx >= 0 and price >= self.history[idx][0]:
			span += self.history[idx][1]
			idx -= self.history[idx][1]
		self.history.append([price, span])
		return span