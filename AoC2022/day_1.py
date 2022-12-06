import numpy as np

def read_input(file_name):
	with open(file_name, 'r') as input_file:
		blocks = input_file.read().rstrip().split('\n\n')
		return [[int(s) for s in block.split('\n')] for block in blocks]

def calories(input, n):
	s = np.array([sum(i) for i in input])
	return sum(s[np.argpartition(s, -n)[-n:]])
	
if __name__ == "__main__":
	input = read_input('input_1.txt')
	# part 1
	print(calories(input, 1))
	# part 2
	print(calories(input, 3))
