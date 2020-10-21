class Persona:

	def __init__(self, nombre, edad):
		self.nombre=nombre
		self.edad=edad
	def saluda(seld, otra_persona):
		return f'Hola {otra_persona.nombre} me llamo {self.nombre}'


#USO del método en la consola
"""
>>>david=Persona('David',35)
>>>erika=Persona('Erika',34)

>>>david.saluda(erika)
>>>'Hola Erika, me llamo David'
"""