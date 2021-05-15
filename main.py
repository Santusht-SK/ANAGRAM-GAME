import random
import english_words
from english_words import english_words_lower_set #this imports a randomizer and a dictionary for randomizing letters and to make sure the word the user enters is in the english dictionary.

characters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z" #variable = all letters
vowels_assigned = "a", "e", "i", "o", "u"
global score_assigned

score_assigned = {"a":1, "b":2, "c":1, "d":2, "e":1, "f":2, "g":1, "h":2, "i":1, "j":2, "k":1, "l":1, "m":1, "n":1, "o":2, "p":2, "q":3, "r":1, "s":1, "t":1, "u":1, "v":4, "w":5, "x":6, "y":7, "z":8} #assigning letters to scores using dictionaries 

number_of_word_attempts = 10 #assigning multiple variables to 0
total = 0
def randomizer(characters,vowels_assigned): #a function that creates 7 randomized letters and saves it using return.
  global seven_given_letters
  six_given_letters = random.sample(characters,6)
  vowel_given = random.sample(vowels_assigned,1)
  seven_given_letters = six_given_letters + vowel_given
  return seven_given_letters
    
def getword(part1, part2):
  if part1 == True:
   print ("\nHere are your letters, good luck!\n",*randomizer(characters, vowels_assigned))
   global word1
   global total
   global number_of_word_attempts
   
   status = "right"
   user_word = str(input("Enter a word with only lowercase letters using your letters.\n"))
  
 
  

   
   
  for character in user_word:
    if character.lower() not in seven_given_letters:
      status = 'wrong'
      number_of_word_attempts -= 1
      print ("This does not use only the 7 letters given. ")
      print("Number of attempts:", number_of_word_attempts)
      print("Score:", total)
      break 
    elif user_word.isalpha() == False or user_word.islower() ==False:
      number_of_word_attempts -= 1
      total += 0 
      print ("This is an invalid guess as you did not only use LOWERCASE letters.")
      print("Number of attempts:", number_of_word_attempts)
      print("Score:", total)
      break
    elif user_word not in english_words_lower_set or len(user_word) ==1:
     number_of_word_attempts -= 1
     print ("This is an invalid guess as it is not in the English Dictionary.")
     print("Score:", total)
     print("Number of attempts:", number_of_word_attempts)
     break 
    else:
      for letter in user_word:
        total += score_assigned[letter]
      number_of_word_attempts -= 1
      print("Score:", total)
      print("Number of attempts:", number_of_word_attempts)
      break
 

screenoption = input("Welcome to the ANAGRAM GAME.\nIf you want to read the instructions, please type ""'instructions""' (Do not type in the apostrophes).\nMake sure from here on out you type everything in LOWERCASE letters. Please type in ""'play""' to start\n\n")
if screenoption == "play":
  getword(True, True)

elif screenoption == "instructions":
  print ("\n\nThe instructions of the game are pretty simple.\nYou will be given 7 random letters.\nYou will then be instructed to make a guess using the 7 random letters.\nDepending on the number of letters, etc, you will be given a score.\nAfter a word is entered, you will recieve an update on your score and attempts.\nThe game will end once you have reached 30 points or if you run out of attempts.\nYou only have 10 attempts!\n")

  
  
  call_instruction_once = 1
  def instructions_call():
    global call_instruction_once
    if call_instruction_once == 1:
      print("When you are done, please enter the word ""'play'"" in lowercase letters in order to play the game.\nIf you want to see the amount of points each letter stores, please enter '""check letter values""'. \n")
      call_instruction_once += 1

    playnow = input()
    if playnow == "play":
      getword(True, True)
    elif playnow == "check letter values":
      score_values = score_assigned.items()
      for letter in score_values:
        print(*letter)
      print("\nPlease input ""'play""' or ""'check letter values""'")
      instructions_call() 
    else:
      print("Please input ""'play""' or ""'check letter values""'")
      instructions_call()
  instructions_call()  


while total < 30:
  getword(True, True)
  if total > 30 and number_of_word_attempts>=0:
     print("Congrats! You won the game with", number_of_word_attempts, "turns left!\n")
     break
  if number_of_word_attempts == 0 and total<30:
    print("You Lost!")
    break
 
    



  

  





