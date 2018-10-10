# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # start an index
    i = 0
    
    #while index is less than length of the word
    while i < len(secret_word):
        #as long as you can find secret word letters in guess, continue checking
        if secret_word[i] in letters_guessed:
            i += 1
        #as soon as something is wrong, stop
        else:
            break
    # you've now reached the end of the word, if you're still here, good
    #if the index reached the end of the word, then secret word is guessed
    if i == len(secret_word):
        return True
    #otherwise you stopped so there is something incorrectly guessed
    else:
        return False 


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    i = 0
    guessed_word = ""
    
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            guessed_word = guessed_word + secret_word[i]
        else:
            guessed_word = guessed_word + "_ "
        i += 1
    return(guessed_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    i = 0
    full_list = string.ascii_lowercase
    available_letters = ""
    
    # while indexing over full alphabet:
    # if you see something that isn't already guessed, add it as an option
    # otherwise, don't add it
    while i < len(full_list):
    	if full_list[i] not in letters_guessed:
    		available_letters = available_letters + full_list[i]
    	else:
    		available_letters = available_letters + ""
    	i += 1
    return available_letters
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word = choose_word(wordlist)
    letters_guessed = ""
    alphabet = string.ascii_lowercase
    available_letters = get_available_letters(letters_guessed)
    warnings = 3
    guesses = 6
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    print("Available letters: ", available_letters)
    print("-----------------------")
    
    # count unique letters in secret_word to use for final score at end of game
    unique = 0
    for char in alphabet:
        if char in secret_word:
            unique += 1
        else:
            unique += 0

    # as long as word hasn't been guessed or guesses are left, keep game going
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:

        ## ROUND 1
    
        guess = str.lower(input("Please guess a letter: "))
        
        ## if input IS NOT valid
        if guess not in alphabet:
            print("Sorry, that wasn't a valid entry!")
            # if you have warnings left, take one away
            if warnings > 0:
                warnings = warnings - 1
                print("Sorry but you lose a warning now. You have", warnings, "left.")
            # otherwise if you have guesses left, take one away
            else:
                print("You have no warnings left so you lose a guess.")
                guesses = guesses - 1
        ## if input IS valid
        else:
            # see if the guess is correct, if so, update everything and move on to next round
            if guess in secret_word:
                letters_guessed = letters_guessed + guess
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            # incorrect guess
            else:
                # incorrect, repeat
                if guess in letters_guessed:
                    print("Incorrect guess, and you already tried that letter.")
                    # if you have warnings left, take one away
                    if warnings > 0:
                        warnings = warnings - 1
                        print("Sorry but you lose a warning now. You have", warnings, "left.")
                    # otherwise if you have guesses left, take one away
                    else:
                        print("You have no warnings left so you lose a guess.")
                        guesses = guesses - 1
                # incorrect, not a repeat
                else:            
                    # incorrect, not a repeat, vowel
                    if guess in vowels:
                        print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                        print("Also, it's a vowel. Double penalty.")
                        # if you have at least 2 warnings, take both away.
                        # if 1 warning, take 1 away and 1 guess away
                        # if 0 warnings and 2 guesses left, take both guesses away.
                        # if only 1 guess left, game is over!
                        if warnings > 1:
                            warnings = warnings - 2
                            print("You lose 2 warnings. You have", warnings, "left.")
                        # otherwise if you have guesses left, take one away
                        elif warnings < 2 and warnings > 0:
                            warnings = warnings - 1
                            guesses = guesses - 1
                            print("You lose 1 warning and 1 guess. You have", warnings, "left.")
                        elif guesses > 1:
                            guesses = guesses - 2
                            print("You have no warnings left so you lose 2 guesses.")
                        else:
                            print("You have insufficient warnings and guesses left. Game over!")
                            guesses = 0
                    # incorrect, not a repeat, not a vowel                    
                    else:
                        print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                        guesses = guesses - 1
                letters_guessed = letters_guessed + guess
            print("You have", guesses, "guesses left.")
            print("Letters already guessed: ", letters_guessed)
            print("Available letters: ", get_available_letters(letters_guessed))
            print("-----------------------")

    if is_word_guessed(secret_word, letters_guessed) == True:
        print("You won!")
        print("Your total score is:", guesses*unique)
    else:
        print("You are lame! You lost! The word was", secret_word, "!!!")
    
#    return letters_guessed, available_letters
    
#    pass
# -----------------------------------

    
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    def match_with_gaps(my_word, other_word):
        '''
        my_word: string with _ characters, current guess of secret word
        other_word: string, regular English word
        returns: boolean, True if all the actual letters of my_word match the 
            corresponding letters of other_word, or the letter is the special symbol
            _ , and my_word and other_word are of the same length;
            False otherwise: 
        '''
        #my_word = current GUESS of secret word
        my_word = get_guessed_word(secret_word, letters_guessed)
        my_word_stripped = my_word.replace("_ ", "_")
        i = 0
        #If lengths are equal, proceed
        if len(other_word) == len(my_word_stripped):
            for i in range(0, len(other_word), 1):
                #if letter is an exaxct match, you're good, keep going
                if other_word[i] == my_word_stripped[i]:
                    #if equal, proceed to next letter               
                    i += 1
                elif my_word_stripped[i] == "_" and other_word[i] in available_letters:
                    # if letter is in available letters as a possible letter being hidden by underscore, proceed
                    i += 1
                # otherwise it can't possibly be a match
                else:
                    break
            # if you reached the end of the word then they match
            if i == len(other_word):
                return True
            else:
                return False
        else:
            return False

    def show_possible_matches(my_word):
        '''
        my_word: string with _ characters, current guess of secret word
        returns: nothing, but should print out every word in wordlist that matches my_word
                 Keep in mind that in hangman when a letter is guessed, all the positions
                 at which that letter occurs in the secret word are revealed.
                 Therefore, the hidden letter(_ ) cannot be one of the letters in the word
                 that has already been revealed.
    
        '''
        match_count = 0
        # for each word in the wordlist
        for i in range(0, len(wordlist), 1):
        	#if my_word and i'th word in wordlist return True for match_with_gaps, print word
            if match_with_gaps(my_word, wordlist[i]) == True:
                print(wordlist[i])
                match_count += 1
            else:
                match_count = match_count
        if match_count < 1:
            print("No matches found")
            return None
        else:
            return None
    
    ### BEGINNING OF ACTUAL HANGMAN GAME
    
    secret_word = choose_word(wordlist)
    letters_guessed = ""
    alphabet = string.ascii_lowercase
    available_letters = get_available_letters(letters_guessed)
    warnings = 3
    guesses = 6
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    print("Available letters: ", available_letters)
    print("-----------------------")
    
    # count unique letters in secret_word to use for final score at end of game
    unique = 0
    for char in alphabet:
        if char in secret_word:
            unique += 1
        else:
            unique += 0

    # as long as word hasn't been guessed or guesses are left, keep game going
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:

        ## ROUND 1
    
        guess = str.lower(input("Please guess a letter: "))
        
        ## if input IS NOT valid
        if guess not in alphabet and guess != "*":
            print("Sorry, that wasn't a valid entry!")
            # if you have warnings left, take one away
            if warnings > 0:
                warnings = warnings - 1
                print("Sorry but you lose a warning now. You have", warnings, "left.")
            # otherwise if you have guesses left, take one away
            else:
                print("You have no warnings left so you lose a guess.")
                guesses = guesses - 1
        # otherwise if guess is an asterisk, show possible matches as a hint
        elif guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        # otherwise guess is valid...
        else:
            # see if the guess is correct, if so, update everything and move on to next round
            if guess in secret_word:
                letters_guessed = letters_guessed + guess
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            # incorrect guess
            else:
                # incorrect, repeat
                if guess in letters_guessed:
                    print("Incorrect guess, and you already tried that letter.")
                    # if you have warnings left, take one away
                    if warnings > 0:
                        warnings = warnings - 1
                        print("Sorry but you lose a warning now. You have", warnings, "left.")
                    # otherwise if you have guesses left, take one away
                    else:
                        print("You have no warnings left so you lose a guess.")
                        guesses = guesses - 1
                # incorrect, not a repeat
                else:            
                    # incorrect, not a repeat, vowel
                    if guess in vowels:
                        print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                        print("Also, it's a vowel. Double penalty.")
                        # if you have at least 2 warnings, take both away.
                        # if 1 warning, take 1 away and 1 guess away
                        # if 0 warnings and 2 guesses left, take both guesses away.
                        # if only 1 guess left, game is over!
                        if warnings > 1:
                            warnings = warnings - 2
                            print("You lose 2 warnings. You have", warnings, "left.")
                        # otherwise if you have guesses left, take one away
                        elif warnings < 2 and warnings > 0:
                            warnings = warnings - 1
                            guesses = guesses - 1
                            print("You lose 1 warning and 1 guess. You have", warnings, "left.")
                        elif guesses > 1:
                            guesses = guesses - 2
                            print("You have no warnings left so you lose 2 guesses.")
                        else:
                            print("You have insufficient warnings and guesses left. Game over!")
                            guesses = 0
                    # incorrect, not a repeat, not a vowel                    
                    else:
                        print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                        guesses = guesses - 1
                letters_guessed = letters_guessed + guess
            print("You have", guesses, "guesses left.")
            print("Letters already guessed: ", letters_guessed)
            print("Available letters: ", get_available_letters(letters_guessed))
            print("-----------------------")

    if is_word_guessed(secret_word, letters_guessed) == True:
        print("You won!")
        print("Your total score is:", guesses*unique)
    else:
        print("You are lame! You lost! The word was", secret_word, "!!!")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
