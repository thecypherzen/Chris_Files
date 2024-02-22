#!/usr/bin/env python3

col_width = 15
def char_pad(item, char=' ', max_width=col_width):
	if item is None:
		return
	if not isinstance(item, str):
		item = str(item)

	spaces = max_width - len(item)
	while spaces:
		print(char, end='')
		spaces -= 1

sentences = ["I apologize for the delay in responding.",\
			 "Your account setup is incomplete.", \
			"Finish setting up your account and create a password using the button below.", \
			"By adding a password, you will be able to sign in to Plum to access your Plum Profile and manage your account at any time.", "Thank you for reaching out to the Payments Team.",\
			"Double Data available for customers on  Unlimited plans if they migrate to a doMore Monthly Data Capped Plan today.", \
			"Terms and Conditions apply.",\
			"We would like to inform you that we have created a practice quiz mandatory for all Project Uolo  participants.",\
			"Our team is working diligently to generate all the invoices for this project.",\
			"I think that is too slow for a ‘support’ system.",\
			"Thank you very much, albeit your response is coming so freaking late, 8 days later!",\
			"What's the relevance and usefullness of help if it comes too late?",\
			"It’ll be a good idea if there can be an improvement in this regard, should it be that I am not the only one who has complained.",\
			"It's a beautiful day", "Thank you for sunshine",\
			"What a great day to be alive!",\
			"I terribly hate this job. It's like hell! I'll never recommend this to anyone, not even an enemy."]

words_list = [ "Classfy", "Classfication", "Classes", \
				"classed", "Classified", "Declass", "Classy",\
				"code", "coding", "just", "justice", "judge",\
				"judging", "judgement", "doing", "done", "do",\
				"coder", "coded", "codex", "codec", "stem",\
				"stems", "stemming", "stemmed", "stemmer" ]

# 1. using stopwords
#from nltk.corpus import stopwords

#stop_words = list(stopwords.words("english"))
#print(stop_words)
#print("length: ", (len(stop_words)))

# 2. stemming && lemmatization
#from nltk.stem import WordNetLemmatizer, PorterStemmer
#lemma = WordNetLemmatizer()
#stema = PorterStemmer()

#for word in words_list:
#	res_lemma = lemma.lemmatize(word,'n')
#	res_stema = stema.stem(word)
#	print(word, res_lemma, res_stema)

# 3. Sentiment Analysis
#def sentiment_rating(score=0.0):
#	rating = "Highly Positive"
#	if score < 0.0 and score >= -0.5:
#		rating = "Negative"
#	elif score < -0.5:
#		rating = "Highly Negative"
#	elif score == 0.0:
#		rating = "Neutral"
#	elif score > 0.0 and score <= 0.5:
#		rating = "Positive"
#	return rating


#from nltk.sentiment import SentimentIntensityAnalyzer as sia
#sia = sia()
#for sentence in sentences:
#	score = round(sia.polarity_scores(sentence)['compound'], 1)
#	print(f"Sentiment score: {score}\
#	{sentiment_rating(score)}")

# 4. Word meanings and definitions
from nltk.corpus import wordnet

m_word = "computer"
try:
	synsets = wordnet.synsets(m_word)
	if synsets:
		for synset in synsets:
			for i, _ in enumerate(synset):
				name = synset[i].name()
				meaning = synset[i].definition()
				print(f"{name}\tDef: {meaning}")
	else:
		print("no definition found")
except Exception as e:
	print(str(e))
# part of speech tagging
