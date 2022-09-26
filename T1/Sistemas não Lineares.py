from sympy.abc import *
from sympy import *
import sympy

class T2:
	def __init__(self, f):
		f = list(map(lambda a: simplify(a), f))
		self.f = self.__f(f)
		self.jacobi = self.__jacobiMatrix(f)

	def __f(self, f):
		return list(map(
					lambda a: lambdify((x, y), f[a]),
					range(len(f))
		))

	def __df(self, f, variavel = x, grau = 1):
		return lambdify((x, y), diff(f, variavel, grau))

	def __jacobiMatrix(self, f):
		return [
			[self.__df(f[0], x), self.__df(f[0], y)],
			[self.__df(f[1], x), self.__df(f[1], y)],
		]
		# return list(map(
		# 	lambda a: list(map(
		# 		lambda b: self.,
		# 	   a)),
		# 	f
		# ))

	def newton2D(self, valores, iter = 100):
		x0, y0 = valores

		for _ in range(iter):
			F = Matrix(list(map(lambda a: a(x0, y0), self.f)))
			jacobi_inv = Matrix(list(map(lambda a: list(map(lambda b: b(x0, y0), a)), self.jacobi))).inv()
			x0 = x0 - (F[0] * jacobi_inv[0] + F[1] * jacobi_inv[1])
			y0 = y0 - (F[0] * jacobi_inv[2] + F[1] * jacobi_inv[3])

		return (x0, y0)

if __name__ == "__main__":
	# Inputo do Moodle
	func1 = x**2 + y**2 - 5
	func2 = x**2 + x * y**3 - 3
	x0 = -1.7204
	y0 = 1.2619
	iterations = [1, 2, 3, 4, 5]


	# Meu Input
	f = [
		func1,
		func2
	]

	valores = (x0, y0)

	t = T2(f)

	for i in iterations:
		r = t.newton2D(valores, i)
		print("{:.11f},".format(r[0]))
		print("{:.11f},".format(r[1]))