import sys
import timeit
from collections import defaultdict

def read_input(file_name):
	with open(file_name, 'r') as input_file:
		return input_file.read().strip()

#def start_of_block(buffer, n):
#	for i in range(n, len(buffer)):
#		if len(set(buffer[i-n:i])) == n:
#			return i

def update(window, a, r):
	window[a] += 1
	if window[r] <= 1:
		del window[r]
	else:
		window[r] -= 1

def start_of_block(buffer, n):
	window = defaultdict(int)
	for i in range(n):
		window[buffer[i]] += 1
	for i in range(n, len(buffer)):
		if len(window) == n:
			return i
		update(window, buffer[i], buffer[i-n])
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_name = sys.argv[1]
	else:
		file_name = 'input_6.txt'
		
	input = read_input(file_name)
	# part 1
	print(timeit.timeit(lambda: start_of_block(input, 4), number=1000))
	print(start_of_block(input, 4))
	# part 2
	print(timeit.timeit(lambda: start_of_block(input, 14), number=1000))
	print(start_of_block(input, 14))
	
