import argparse

def reverse_string(word):

	# list slicing approach
	# result = word[::-1]

	# alternative approach without list slicing approach
	index = len(word)-1
	result = ''
	while (index) >= 0:
		result += word[index]
		index -= 1

	return result

def reverse_sentence(sentence):

	# split the sentence up on white spaces
	tokens = sentence.split(" ")

	# reverse each word in the array
	reversed_words = [reverse_string(x) for x in tokens]

	# reverse entire array contents 
	result_array = reversed_words[::-1]

	# iterate throurgh result array and concatenate strings
	result_string = ' '.join(word for word in result_array)

	return result_string


def main():

	parser = argparse.ArgumentParser(description='Reverse strings(s) program')
	parser.add_argument("string", help="Enter the string you would like to reverse")
	parser.add_argument("-r", "--r", help="Select this option to reverse a single word", action="store_true")
	parser.add_argument("-w", "--w", help="Select this option to reverse a string word for word", action="store_true")
	parser.add_argument("-i", "--input", help="Select this option to reverse the contents of a file")

	args = parser.parse_args()

	# reverse single word located in input file 
	if args.r and args.input:
		with open(args.input, 'r') as f:
			result = reverse_string(f.read())
			print(result)
	# reverse string of words located in input file
	elif args.w and args.input:
		with open(args.input, 'r') as f:
			result =reverse_sentence(f.read())
			print(result)
	# reverse single word from command line argument
	elif args.r:
		result = reverse_string(args.string)
		print(result)
	# reverse string of words from command line argument
	elif args.w:
		result = reverse_sentence(args.string)
		print(result)
	else: # in the case that user forgets to enter parameter default to the standard reverse function
		result = reverse_string(args.string)
		print(result)


if __name__ == '__main__':
	main()