import math

class Flow:
	def __init__(self, seed, sharpness):
		self.seed = seed
		self.sharpness = sharpness

	def __call__(self, x, y):
		self.s_seed = self.seed / (10 * len(str(self.seed)))

		sx = x / (10 * len(str(x)) - 1)
		sy = y / (10 * len(str(y)) - 1)

		height = math.cos(math.atan(sx * sy + self.s_seed) * (math.atan(self.s_seed) + math.fmod(math.sin(sx * sy + self.s_seed), math.cos(sx * sy + self.s_seed))) * self.sharpness)
		return height

class Rice:
	def __init__(self, seed, sharpness):
		self.seed = seed
		self.sharpness = sharpness

	def __call__(self, x, y):
		self.s_seed = self.seed / (10 * len(str(self.seed)))

		sx = x / (10 * len(str(x)) - 1)
		sy = y / (10 * len(str(y)) - 1)

		height = math.cos(math.atan(sx * sy + self.s_seed) + math.fmod(math.sin(sx + sy + self.s_seed * 10), math.cos(sx * sy + self.s_seed * 10)))
		return height * self.sharpness