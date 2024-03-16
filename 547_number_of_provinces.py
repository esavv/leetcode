class Solution(object):
	def findCircleNum(self, isConnected):
		visited = [False for _ in range(len(isConnected))]
		stack = []
		province_ct = 0
		for i in range(len(isConnected)):
			if visited[i]:
				continue
			stack.append(i)
			visited[i] = True
			while stack:
				city = stack.pop()
				for j in range(len(isConnected)):
					if not visited[j] and isConnected[city][j]:
						stack.append(j)
						visited[j] = True
			province_ct += 1
		return province_ct
