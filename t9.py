from fuzzywuzzy import fuzz


class T9:
	def __init__(self):
		file = open("dictionary.txt", "r")
		self.words = [word.replace("\n", "") for word in file.readlines()]
		file.close()

		self.dictionary = dict()
		for i in range(1072, 1104):
			self.dictionary[chr(i)] = []
		
		self.letters = [chr(letter) for letter in range(1072, 1104)]

		for word in self.words:
			for i in range(1072, 1104):
				if word.startswith(chr(i)):
					self.dictionary[chr(i)].append(word)

	def fix(self, sentence):
		for symbol in [",", ".", "!", "'", '"', ";", ":", "(", ")"]:
			sentence = sentence.replace(symbol, f" {symbol} ")
		sentence
		words = [word.lower() for word in sentence.split()]
		err_words = []

		for i in range(len(words)):
			try:
				if words[i] in [",", ".", "!", "'", '"', ";", ":", "(", ")"]:
					pass
				else:
					self.words.index(words[i])
			except:
				err_words.append([i, words[i]])

		if len(err_words) != 0:
			ratio_values = []
			for err_word in err_words:
				for j in range(1072, 1104):
					if err_word[1].startswith(chr(j)):
						for word in self.dictionary[chr(j)]:
							ratio_value = fuzz.ratio(err_word[1], word)
							ratio_values.append(ratio_value)
						ratio_max_value = max(ratio_values) 
						word_index = int(ratio_values.index(ratio_max_value))
						fixed_word = self.dictionary[chr(j)][word_index] 
						ratio_values = []
						break
				words[err_word[0]] = fixed_word

		result = " ".join(words)
		for symbol in [",", ".", "!", "'", '"', ";", ":", "(", ")"]:
			result = result.replace(f" {symbol} ", symbol)

		return len(err_words), ", ".join([err_word[1] for err_word in err_words]), result