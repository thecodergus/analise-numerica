from sympy.abc import *
import sympy
from sympy import *
import math

class T1:
	def __init__(self, f, symbol=x) -> None:
		self.f = sympy.lambdify(symbol, f)
		self.df = sympy.lambdify(symbol, self.__df(f, symbol))

	def __df(self, f, s=x):
		return sympy.diff(f, s)

	def bissecao(self, intervalo, interacoes=100):
		a, b = intervalo

		for _ in range(interacoes):
			aprox = (a + b) / 2

			if(self.f(b) * self.f(aprox) < 0):
				a = aprox
			if(self.f(a) * self.f(aprox) < 0):
				b = aprox

		return aprox

	def newton(self, x0, interacoes=100):
		for _ in range(interacoes):
			x0 -= self.f(x0) / self.df(x0)

		return x0

	def posicao_falsa(self, intervalo, interacoes=100):
		a, b = intervalo

		for _ in range(interacoes):
			fa, fb = self.f(a), self.f(b)
			c = (a * fb - b * fa) / (fb - fa)

			if(c == 0):
				break
			elif(self.f(c) * fa < 0):
				b = c
			else:
				a = c

		return c

	def secante(self, intervalo, interacoes=100):
		x0, x1 = intervalo
		x2 = 0

		for i in range(interacoes):
			fx0, fx1 = self.f(x0), self.f(x1)

			x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
			c = fx0 * fx1

			x0, x1 = x1, x2

			if(c == 0):
				break

		return x2


if __name__ == "__main__":
	g = 8.81
	t = 0.88
	xt = 4.32
	f = (-(g / 2 * w**2) * (sinh(w*t) - sin(w*t))) - xt

	Funcoes = T1(f, w)
	testes = {
		"bissecao": {
			"interacoes": [2, 4, 8, 12],
			"intervalo": [
				-5.13,0.67
			]
		},
		"newton": {
			"interacoes": [1, 3, 5],
			"intervalo": -1.16
		},
		"secante": {
			"interacoes": [1, 2, 5],
			"intervalo": [
				-4.56,
				-1.26
			]
		},
		"posicao_falsa": {
			"interacoes": [2, 4, 7, 11],
			"intervalo": [
				-5.91,0.18
			]
		}
	}

	for fun in testes.keys():
		for interacao in testes[fun]["interacoes"]:
			print("{:.11f},".format(eval("Funcoes.{}({}, {})".format(
				fun, testes[fun]["intervalo"], interacao))))
