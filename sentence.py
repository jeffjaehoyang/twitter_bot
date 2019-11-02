import random 

def categorize():
	f = open("/Users/Jeff/Dropbox/Coding/twitter_bot/gutenberg.txt","r")
	contents = f.read()
	listify = contents.split()
	start = []
	end = []
	for word in listify:
		if word.isupper():
			listify.remove(word)
		elif word[0].isupper():
			start.append(word)
		elif word.endswith("."):
			end.append(word)
	f.close()

	return [start, end, listify]

def generate_sentence(start, end, rest):
	sentence = random.choice(start).replace('.', '') + ' ' \
	+ random.choice(rest).lower().replace('.', '') + ' ' \
	+ random.choice(end) 
	return sentence

def run():
	return generate_sentence(categorize()[0], categorize()[1], categorize()[2])