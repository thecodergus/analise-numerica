from numpy import *
import numpy
from scipy import optimize as T

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
		return poly1d(numpy.polyfit(x, y, len(a)))

	def get_value(self, x):
		return self.f(x)


# if __name__ == "__main__":
# 	x = [-1.839, -0.564, 2.228]
# 	y = [0.076, 3.303, 1.647]

# 	t = InterpolacaoSimples(x, y)

	
# 	for i in t.get_coeficientes():
# 		print("{:.11f},".format(i))

# if __name__ == "__main__":
# 	x = [1.532, 1.67, 1.839, 2.063, 2.239, 2.303, 2.504, 2.666, 2.842, 3.062, 3.215, 3.313, 3.562, 3.686, 3.842, 4.028, 4.181, 4.45, 4.572, 4.685, 4.892]
# 	f = lambda x: cos(x + sqrt(log(x**2)))
# 	t = InterpolacaoFuncao(f, x)

	
# 	for i in t.get_coeficientes():
# 		print("{:.11f},".format(i))

if __name__ == "__main__":	
	
	x = [0.0109, 0.8969, 1.7801, 2.8683, 4.004, 4.2499, 5.0442, 6.4043, 6.7618, 8.1742, 9.0051, 9.9303]
	y = [0.6838, 2.224, 3.959, 5.8476, 8.1818, 8.7214, 10.3173, 12.9015, 13.4349, 16.2593, 17.4278, 18.8074]
	values = [2.3136, 6.7516, 9.446]



	t = InterpolacaoAcharFuncao(x, y)

	for i in values:
		print("{:.11f},".format(t.get_value(i)))