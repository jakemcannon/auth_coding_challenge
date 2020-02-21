
def reverse_string(word):

	# list slicing approach
	result = word[::-1]

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

reverse_sentence("hello world")

