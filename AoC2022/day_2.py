def read_input(file_name):
	with open(file_name, 'r') as file:
		return [(ord(line[0])-ord('A'), ord(line[2])-ord('X')) for line in file]
	return []
	
def score_1(a, b):
	return b+1 + ((b-a+1)%3)*3

def score_2(a, b):
	return (a+b-1)%3+1 + b*3

def total_score(input, score_f):
	return sum(score_f(i[0], i[1]) for i in input)

if __name__ == '__main__':
	input = read_input('input_2.txt')
	# part 1
	print(total_score(input, score_1))
	# part 2
	print(total_score(input, score_2))
