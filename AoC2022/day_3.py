from operator import and_
from functools import reduce

def read_input(file_name):
	with open(file_name) as input_file:
		return [[(ord(i)-ord('a'))%58+1 for i in line.strip()] for line in input_file]
	
def duplicate(*rucksacks):
	return reduce(and_, map(set, rucksacks)).pop()

def compartment_dupes(input):
	return sum(duplicate(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]) for rucksack in input)

def badges(input):
	return sum(duplicate(input[i], input[i+1], input[i+2]) for i in range(0, len(input), 3))
	
if __name__ == '__main__':
	input = read_input('input_3.txt')
	# part 1
	print(compartment_dupes(input))
	# part 2
	print(badges(input))
