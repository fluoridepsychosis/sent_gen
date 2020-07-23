import random

def main():
    sentence = ""
    for i in range(50):
        with open("outputfile.txt", "w") as outputfile:
            outputfile.write(ornate_noun(sentence))

def ornate_noun(sentence):

    # Initialising lists for words storage
    nounlist = []
    adjectivelist = []
    articlelist = []

    with open("english-nouns.txt") as nounfile, open("adjectives.txt") as adjectivefile, open("article.txt") as articlefile:

        # Reading wordlist files into lists
        for line in nounfile:
            nounlist.append(line.rstrip())
        
        for line in adjectivefile:
            adjectivelist.append(line.rstrip())

        for line in articlefile:
            articlelist.append(line.rstrip())

        # Creating lists of numbers to allow for random path conditional statements
        begin_choice_list = [0, 1, 2]
        begin_choice = random.choice(begin_choice_list)
        

        # This is the initial choice i.e. "begin" that chooses which function is called first
        if begin_choice == 0:
            return noun(sentence, nounlist)
        elif begin_choice == 1:
            return adjective(sentence, nounlist, adjectivelist)
        else:
            return article(sentence, nounlist, adjectivelist, articlelist)


def noun(sentence, nounlist):

    return (sentence  + " " + random.choice(nounlist))
    
    
def adjective(sentence, nounlist, adjectivelist):

    adjective_choice = [0, 1]
    choice = random.choice(adjective_choice)

    sentence = (sentence + " " + random.choice(adjectivelist))

    if choice == 0:
        return adjective(sentence, nounlist, adjectivelist)
    else:
        return noun(sentence, nounlist)

def article(sentence, nounlist, adjectivelist, articlelist):

    article_choice = [0, 1]
    choice = random.choice(article_choice)
    sentence = random.choice(articlelist)

    if choice == 0:
        return noun(sentence, nounlist)
    else:
        return adjective(sentence, nounlist, adjectivelist)


if __name__ == "__main()__":
    main()
