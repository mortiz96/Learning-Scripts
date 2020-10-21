class Coordenada:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def calcular_distancia(self, coordenada):
		a = abs(self.x - coordenada.x)
		b = abs(self.y - coordenada.y)

		return (a**2 + b**2)**0.5 