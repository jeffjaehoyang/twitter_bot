import random 

def categorize():
	f = open("gutenberg.txt","r")
	contents = f.read()
	listify = contents.split()
	start = []
	end = []
	body = []
	for word in listify:
		if word[0].isupper() and not word.isupper():
			start.append(word)
		elif word.endswith(".") and not word.isupper():
			end.append(word)
		elif not word.isupper(): 
			body.append(word)

	f.close()

	return [start, end, body]

def generate_sentence(start, end, rest):
	sentence = random.choice(start).replace('.', '') + ' ' \
	+ random.choice(rest).lower().replace('.', '') + ' ' \
	+ random.choice(end) 
	return sentence

def run():
	return generate_sentence(categorize()[0], categorize()[1], categorize()[2])