
import random
wordList=[ ] 


with open("Eng_dictionary.txt") as word_file:
   for word in word_file:
        wordList.append(word)
        
print(wordList)
print(random.choice(wordList))
print("ham" in wordList)
