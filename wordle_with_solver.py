import re
import random

OFFSET = 10
ITERATIONS = 2

with open("words.txt") as file:
    linesold = file.readlines()
    linesold = [line.rstrip() for line in linesold]

for i in range(ITERATIONS):
    lines = linesold[:]
    alphabet = [-1 for i in range(26)]
    letters = ""
    finalword = ["[a-z]" for i in range(5)]

    cword = random.choice(lines)
    word = "earth"
    print("earth")
    iteration = 0

    while True:
        iteration += 1
        wordlist = list(cword)
        resp = ""
        offset = 0
        for index, letter in enumerate(word):
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
        score = resp
        if score == "22222":
            break
        #new_word = input("Use:   ")
        new_word = "y"

        if new_word == "y":
            tmp_lines = linesold
        else:
            tmp_lines = lines

        for index, letter in enumerate(word.lower()):
            alphabet[ord(letter)-97] = int(score[index])
            if score[index] != "0":
                letters += letter
            if score[index] == "2":
                finalword[index] = letter.upper()

        if new_word == "y":
            tmp_lines = [x for x in tmp_lines if all(letter in x for letter in letters)]
            tmp_lines = [x for x in tmp_lines if not any(letter in x for letter in [chr(i+97) for i, x in enumerate(alphabet) if x == 0])]
            p = re.compile("".join(finalword), re.IGNORECASE)
            tmp_lines = [x for x in tmp_lines if p.match(x)]
        else:
            tmp_lines = [x for x in tmp_lines if any(letter in x for letter in letters)]
        indices = [chr(i+97) for i, x in enumerate(alphabet) if x == -1]
        count = [0 for i in range(len(indices))]

        for index, letter in enumerate(indices):
            for word in tmp_lines:
                if letter in word:
                    count[index] += 1

        count = [abs(len(tmp_lines)//2-i) for i in count]
        min_list = sorted(zip(indices,count), key=lambda t: t[1], reverse=True)

        best = -1
        best_line = ""
        for i in tmp_lines:
            score = 0
            for j,k in enumerate(min_list):
                if k[0] in i:
                    score += j
            if new_word == "y":
                for j,k in zip([chr(l+97) for l in alphabet],alphabet):
                    if j in i and k > 0:
                        score += len(min_list)+(k*OFFSET)
            if score > best:
                best = score
                best_line = i
            
        print(best_line,tmp_lines,cword)
        if new_word != "y":
            lines = tmp_lines
        word = best_line

    print("Solved in",iteration,"iterations")
