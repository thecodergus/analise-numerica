from numpy import *

class InterpolacaoSimples:
	def __init__(self, a, b):
		self.x = array(a, dtype = "double")
		self.y = array(b, dtype = "double")
		self.grau = len(a)
		self.A = self.__grau_polinomio()

	def __grau_polinomio(self):
		return array([*map(lambda xi: self.x ** xi, range(self.grau))]).transpose()

	def get_coeficientes(self):
		return linalg.inv(self.A).dot(self.y)

class InterpolacaoFuncao:
	def __init__(self, f, x):
		self.x = array(x, dtype = "double")
		self.y = array(list(map(lambda a: f(a), x)), dtype = "double")
		self.grau = len(x)
		self.A = self.__grau_polinomio()

	def __grau_polinomio(self):
		return array(list(map(lambda xi: self.x ** xi, range(self.grau)))).transpose()

	def get_coeficientes(self):
		return linalg.inv(self.A).dot(self.y)

class InterpolacaoAcharFuncao:
	def __init__(self, a, b):
		self.x = array(a, dtype = "double")
		self.y = array(b, dtype = "double")
		self.f = self.__f(a, b)

	def __f(self, a, b):
		x = array(a, dtype = "double")
		y = array(b, dtype = "double")
		return poly1d(T.fit(x, y, len(a)))

	def get_value(self, x):
		return self.f(x)


if __name__ == "__main__":
	x = [-1.839, -0.564, 2.228]
	y = [0.076, 3.303, 1.647]

	t = InterpolacaoSimples(x, y)

	
	for i in t.get_coeficientes():
		print("{:.11f},".format(i))

# if __name__ == "__main__":
# 	f = lambda x: cos(x + sqrt(log(x**2)))
# 	x = [1.506, 2.011, 2.344, 2.637, 2.839, 3.3, 3.533, 3.919, 4.094, 4.612, 4.832]

# 	t = InterpolacaoFuncao(f, x)

	
# 	for i in t.get_coeficientes():
# 		print("{:.11f},".format(i))

# if __name__ == "__main__":
# 	x = [0.067, 0.548, 0.962, 1.577, 2.081, 2.578, 2.843, 3.5, 3.914]
# 	y = [0.546, 0.888, 1.369, 1.943, 1.828, 0.82, 0.217, 0.842, 1.981]
# 	values = [2.49, 2.667, 3.197, 3.875]

# 	t = InterpolacaoAcharFuncao(x, y)

# 	for i in values:
# 		print("{:.11f},".format(t.get_value(i)))