from copy import deepcopy

def get_stacks(stack_lines):
	n_stacks = (len(stack_lines[0])+1)//4
	stacks = [[] for _ in range(n_stacks)]
	for line in stack_lines[::-1]:
		for i in range(n_stacks):
			c = line[1+i*4]
			if c.isalpha():
				stacks[i].append(c)
	return stacks
	
def get_moves(move_lines):
	moves = []
	for line in move_lines:
		move = line.split(' ')
		moves.append((int(move[1]), int(move[3]), int(move[5])))
	return moves

def read_input(file_name):
	with open(file_name, 'r') as input_file:
		parts = input_file.read().split('\n\n')
		stacks = get_stacks(parts[0].split('\n'))
		moves = get_moves(parts[1].strip().split('\n'))
		return stacks, moves
	
def crate_mover_9000(stacks, move):
	stacks[move[2]-1].extend(stacks[move[1]-1][-1:-move[0]-1:-1])
	stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
	
def crate_mover_9001(stacks, move):
	stacks[move[2]-1].extend(stacks[move[1]-1][-move[0]:])
	stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
	
def execute(stacks, moves, crate_mover):
	tmp = deepcopy(stacks)
	for move in moves:
		crate_mover(tmp, move)
	return tmp

if __name__ == '__main__':
	stacks, moves = read_input('input_5.txt')
	# part_1
	print(''.join(s[-1] for s in execute(stacks, moves, crate_mover_9000)))
	# part_2
	print(''.join(s[-1] for s in execute(stacks, moves, crate_mover_9001)))
