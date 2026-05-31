class Car:
	def __init__(self,brand, color):
		self.brand=brand
		self.color=color
	def show(self):
		print( f"Brand: {self.brand}")
		print( f"color: {self.color}")
s1=Car("BMW","RED")
s1.show()