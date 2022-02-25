#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist


def getletter(num):
  while True:
    letter= input("Player "+ str(num)+" give a letter: ").upper()
    if not letter.isalpha():
      print("Whoa, only letters are allowed!")
    elif len(letter)!=1:
      print("One letter, please!")
    else:
      return letter


def checkwordfrag(curr, dict):
    for word in dict:
      if curr==word:
        return False
      elif word.startswith(curr):
        return True
    return False 

def play(dict):
  word=""
  playernum= 1
  while True:
    letter=getletter(playernum)
    word+=letter
    print("Player "+str(playernum)+" chose "+ letter+", giving the fragment "+ word +"\n")
    if checkwordfrag(word, dict)==False:
      print("Oh no! Player " +str(playernum)+" has lost!")
      break
    
    if playernum==1:
      playernum=2
    else:
      playernum=1

def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")
    print("Welcome to the spooky game of Ghost! Yay!")
    play(words)
    

main()

