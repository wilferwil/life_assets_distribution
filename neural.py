import random
import numpy as np

def derivada(n):
	return n*(1-n)

x = 0.85
y = 0.824
w = random.random()

for i in range(150):
	a = np.tanh(x*w)
	sem = x*w
	e = y-a
	w += x*derivada(e)
	print('sem:')
	print(sem)
	print('com:')
	print(a)
