import string
from words import choose_word
from images import IMAGES
	def is_word_guessed(secret_word,letters_guessed):
		return false
def get_guessed_word(secret_woed,letters_guessed):
	index=0
	guessed_word = ""
	while(index<len(secret_word)):
		if secret_word[index]in letters_guessed:
			guessed_word += secret_word[index]
		else:
			guessed_word +=""
		index=index+1
	return guessed_word
def get_available_letters(letters_guessed):
	import string
	letters_left = string.ascii_lowercase
	return letters_left
def hangman(secret_word):
	print"welcome to the game hangman!"
	print " i am thinking of a word that is "+str(len(secret_word)) + "letters long."
	letters_guessed=[]
	while(True):
		available_letters = get_available_letters(letters_guessed)
		print "Available letters: " + available_letters
	guess = raw_input("please guess a letter:")
	letter = guess.lower()
	if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word,letters_guessed)
            print ""
		if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break
	else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print ""

secret_word = choose_word()
hangman(secret_word)
