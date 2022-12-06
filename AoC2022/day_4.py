def read_input(file_name):
	with open(file_name, 'r') as input_file:
		return [tuple(tuple(int(section) for section in elf.split('-')) for elf in pair.strip().split(',')) for pair in input_file]

def overlap(a, b):
	return min(a[1], b[1]) - max(a[0], b[0])
	
def contains(a, b):
	return overlap(a, b) == min(a[1]-a[0], b[1]-b[0])

def all_contains(input):
	return sum(contains(pair[0], pair[1]) for pair in input)

def all_overlaps(input):
	return sum(overlap(pair[0], pair[1]) >= 0 for pair in input)

if __name__ == '__main__':
	input = read_input('input_4.txt')
	print(all_contains(input))
	print(all_overlaps(input))
