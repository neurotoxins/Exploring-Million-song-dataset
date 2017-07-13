import numpy as numpy


def generateAllWords():
	full_words = open('full_word_list.txt', 'r')

	word_list = open('all_word_file.txt', 'w')

	for line in full_words:
		if not line.strip().startswith("#"):
			word_arr = line.split('<SEP>')
			if int(word_arr[1]) > 5:
				line_arr = [word_arr[0]] * int(word_arr[1])

				new_line = ' '.join(line_arr)

				word_list.write(new_line)


	word_list.close()
	full_words.close()


generateAllWords()