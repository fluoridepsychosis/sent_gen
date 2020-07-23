import ornate_noun
import random

def main():

    with open("prepositions.txt") as prepositionfile, open("relpronouns.txt") as relpronounsfile, open("verbs.txt") as verbsfile:
        # Creating empty sentence string for words to be appended to
        sentence = ""
        prepositionlist = []
        for line in prepositionfile:
            prepositionlist.append(line.rstrip())
        relprolist = []
        for line in relpronounsfile:
            relprolist.append(line.rstrip())
        verblist = []
        for line in verbsfile:
            verblist.append(line.rstrip())

        
        for i in range(100):
            print(fancy_noun(sentence, prepositionlist, relprolist, verblist))

def fancy_noun(sentence, prepositionlist, relprolist, verblist):

        sentence = ornate_noun.ornate_noun(sentence) + " "
        
        fancy_noun_choices = [0, 1, 2]
        choice = random.choice(fancy_noun_choices)

        if choice == 0:
            return sentence
        if choice == 1:
            return preposition(sentence, prepositionlist, relprolist, verblist)
        if choice == 2:
            return relpro(sentence, prepositionlist, relprolist, verblist)

       
def preposition(sentence, prepositionlist, relprolist, verblist):

    sentence = sentence + random.choice(prepositionlist) 
    return fancy_noun(sentence, prepositionlist, relprolist, verblist)

def relpro(sentence, prepositionlist, relprolist, verblist):
    sentence = sentence + random.choice(relprolist)

    relpro_choice = [0, 1]
    choice = random.choice(relpro_choice)

    if choice == 0:
        sentence = fancy_noun(sentence, prepositionlist, relprolist, verblist)
        return verb(sentence, prepositionlist, relprolist, verblist)
    else: 
        sentence = verb(sentence, prepositionlist, relprolist, verblist)
        return fancy_noun(sentence, prepositionlist, relprolist, verblist)

def verb(sentence, prepositionlist, relprolist, verblist):

    sentence = sentence + " " + random.choice(verblist)

    return sentence

main()