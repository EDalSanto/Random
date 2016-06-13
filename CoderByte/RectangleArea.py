def RectangleArea(strArr):
	pts = [ eval(p.replace(" ",",")) for p in strArr ] # Python eval used to remove string literal status
	X = [ p[0] for p in pts ]
	Y = [ p[1] for p in pts ]
	width = max(X) - min(X)
	height = max(Y) - min(Y)
	return width * height

print RectangleArea(["(-1 -1)","(0 0)","(-1 0)","(0 -1)"])
