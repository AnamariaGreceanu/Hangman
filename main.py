from random_word import RandomWords
import time

print("Enter your name ")
print("Welcome",input())


def wordLoading():
    print("Your word is...")
    time.sleep(2)
    word=RandomWords().get_random_word()
    print(word)
    return word

def display():
    guessed_word=""
    for letter in word:
        if letter in used_letters or letter==word[0] or letter==word[len(word)-1]:
            guessed_word+=(letter)
        else:
            guessed_word+=("_")
    print(guessed_word)
    print("Lives:",str(lives))
    print("You have used the following letters ", used_letters)
    return guessed_word

words_found=[]

while True:
    word=wordLoading()
    lives=5
    used_letters=[] 
    display()

    while lives>0:
        guess=input("\nEnter a letter or the entire word: ").lower()
        if guess==word:
            print("\nCongratulations, you guessed the word!")
            break
        elif len(guess)>1:
            lives-=1
            display()
        elif guess in word and guess in [word[0],word[len(word)-1]]:
            print("The letter was given by the game!")
        elif guess in word:
            used_letters.append(guess)
            guessed_word=display()
            if "_" not in guessed_word:
                print("\nCongratulations, you guessed the word!")
                break
        else:
            lives-=1
            used_letters.append(guess)
            display()
    if lives==0:
        print("You lost:( The word was '"+ word+"'")
    else:
        words_found.append(word)

    print("\nGuessed words in this session:",words_found)
    answer=input("Do you still want to play?('yes'/any other key for 'no'): ").lower()
    if answer=="yes":
        continue
    else:
        break