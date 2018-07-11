from random import uniform, randint

M = 30
N = 200

MAX_ENERGY = 50
START_ENERGY = 30

STEPS = 10
ALGORITHM_LENGTH = 64

TOTAL_COMMANDS = 23

START_CELLS_COUNT = 57

# commands
PEEK = 1 # 1-8
ATTACK = 2 # 9-12
MOVE = 3 # 13-16
FORK = 4 # 17-20
PHOTOSYNTHESIZE = 5 # 21
MINERALIZE = 6 # 22
ASK_LOCATION = 7 # 23
ASK_MINERALS = 8 # 24

DISTRIBUTION = [8, 4, 4, 1, 2, 2, 1, 1]

def random_command():
	borders = []
	partial_sum = 0
	for c in DISTRIBUTION:
		borders.append(partial_sum)
		partial_sum += c
	result = randint(0, partial_sum - 1)
	a = -1
	command_num = 1
	while borders[a] <= result:
		command_num += 1
		a += 1
	
	if command_num == PEEK:
		argument = randint(0, 8)
	elif command_num in set([ATTACK, MOVE, FORK]):
		argument = randint(0, 4)
	else:
		argument = None

	return (command_num, argument)


def SolarEnergy(x,M):
	rangeofenergy = M // 2
	energyout = rangeofenergy - x
	return energyout

class Cell(object):
	def __init__(self, algorithm, energy, start_x, start_y):
		self.x = start_x
		self.y = start_y
		self.energy = energy
		self.minerals = 0

	def step(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	def fork(self, direction):
		...
		...
		return Cell()

	def photosynthesize(self,M):
		self.energy += SolarEnergy(self.x,M)
		if self.energy >= MAX_ENERGY:
			aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

	def mineralsintez(self):
		self.energy += self.minerals * 4
		if self.energy >= MAX_ENERGY:
			aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		


class Board(object)
	def __init__(m, n):
		self.cell_list = []

	def add_cell(xpos,ypos,algorithm,energy):
		cell = Cell(algorithm,energy,xpos,ypos)
		self.cell_list.append(cell)


def gen_algorithm():
	return [random_command() for i in range(ALGORITHM_LENGTH)]


def main():
	board = Board(M, N)

	cells = []
	while len(cells) < START_CELLS_COUNT:
		x, y = (randint(0, M), randint(0, N))
		if filter(
			lambda cell: cell.x == x and cell.y == y,
			cells
		):
			continue
		











	# FIXME while true
	for i in range(STEPS):
		step()


