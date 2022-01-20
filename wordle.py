import random

with open("words.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

word = random.choice(lines)
answer = ""

while answer != word:
    answer = input("Guess: ")
    wordlist = list(word)
    resp = ""
    offset = 0
    for index, letter in enumerate(answer):
        if letter in wordlist:
            if wordlist[index-offset] == letter:
                resp += "2"
            else:
                resp += "1"
            del wordlist[wordlist.index(letter)]
            offset += 1
        else:
            resp += "0"
    print(resp)
