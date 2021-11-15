from gensim.models import Word2Vec
from tabulate import tabulate

#   --------------------------------------------------------------
#   I N F O
# Author: Evangelos Stamos
#       https://github.com/estamos
#
#       Developed as a part of thesis
#       "Big Data Analytics using Machine Learning Algorithms"
#
#       "Word2vec | A CBOW and Skipgram Comparative Study"
#
# v1.0 | 2021-04-21
#
#   - Multiple input words separated with spaces
#   - Pretty print results
#   - Set global PRECISION
#
# v1.1 | 2021-04-27
#
#   --------------------------------------------------------------
#   G L O B A L S
CBOW_MODEL = "covid_word2vec-cbow-trained.model"
SKIPGRAM_MODEL = "covid_word2vec-skipgram-trained.model"
PRECISION = 4
#   --------------------------------------------------------------
#   F U N C T I O N S

#1
def find_similarity ():
    words_input = input("Enter two words separated with spaces : ")
    words = words_input.lower().split()
    while len(words_input) == 0 or len(words) < 2 or len(words) > 2:
        print("\n You must enter 2 words!\n")
        words_input = input("Enter two words separated with spaces : ")
        words = words_input.lower().split()
    for i in range(0, len(words)):  # 2 = len(words)
        while (words[i].lower() not in cbow.wv or words[i].lower() not in skipgram.wv):
            print("\n The word" + words[i] + "does not exist in vocabulary!\n")
            words[i] = input("Enter a word instead which is included in vocabulary : ").lower()
    print("\n The similarity between " + str(words[0]) + " and " + str(words[1]) + " is : \n")
    print(tabulate([["CBOW","SKIPGRAM"],
                    [cbow.wv.similarity(words[0], words[1]),
                     skipgram.wv.similarity(words[0], words[1])]],
                     headers="firstrow", floatfmt="." + str(PRECISION) + "f",
                     tablefmt="fancy_grid"))
#2
def the_most_similar (word):
    print("\n The most similar word to " , word , " : \n")
    print(tabulate([["CBOW","SKIPGRAM"],
    [cbow.wv.most_similar(positive = word, topn = 1)[0][0], skipgram.wv.most_similar(positive = word, topn = 1)[0][0]],
    [round(cbow.wv.most_similar(positive = word, topn = 1)[0][1], PRECISION),
    round(skipgram.wv.most_similar(positive = word, topn = 1)[0][1], PRECISION)]],
    headers="firstrow", tablefmt="fancy_grid"))
    #print(f" {cbow.wv.most_similar(positive = word, topn = 1)[0][1]:.4f}    {skipgram.wv.most_similar(positive = word, topn = 1)[0][1]:.4f}")

#3
def does_not_match ():
    words_input = input("Enter words separated with spaces : ")
    words = words_input.lower().split()
    while len(words_input) == 0 or len(words) < 3:
        print("\n Word that does not match others make sense if you enter at least 3 words!\n")
        words_input = input("Enter words separated with spaces : ")
        words = words_input.lower().split()
    for i in range(0, len(words)):
        while (words[i] not in cbow.wv or words[i] not in skipgram.wv):
            print("\n The word" + words[i] + "does not exist in vocabulary!\n")
            words[i] = input("Enter a word instead which is included in vocabulary : ").lower()
    print("\n Word that does not group ", words, " :")
    print(tabulate([["CBOW","SKIPGRAM"],
    [cbow.wv.doesnt_match(words), skipgram.wv.doesnt_match(words)]],
    headers="firstrow", tablefmt="fancy_grid"))
    #print(cbow.wv.doesnt_match(words), "  ", skipgram.wv.doesnt_match(words))

#4
def n_most_similar ():
    words_input = input("Enter a word or words separated with spaces : ")
    words = words_input.lower().split()
    while len(words_input) == 0:
        print("\n You must enter a word!\n")
        words_input = input("Enter a word or words separated with spaces : ")
        words = words_input.lower().split()
    for i in range(0, len(words)):
        while (words[i] not in cbow.wv or words[i] not in skipgram.wv):
            print("\n The word" + words[i]  + " does not exist in vocabulary!\n")
            words[i] = input("Enter a word instead which is included in vocabulary : ").lower()
    n = input("How many similar words to search for : ")
    while (not n.isdigit() or len(n) == 0 or int(n) == 0):
        print("\n You must enter an integer!\n")
        n = input("How many similar words to search for : ")
    n = int(n)
    if n == 1:
        return the_most_similar(words)
    table = [["#", "CBOW", "SKIPGRAM", "CBOW SIMILARITY","SKIPGRAM SIMILARITY"]]

    for i in range(0, n):
        table.append([cbow.wv.most_similar(words, topn = n)[i][0],
                           skipgram.wv.most_similar(words, topn = n)[i][0],
                           cbow.wv.most_similar(words, topn = n)[i][1],
                           skipgram.wv.most_similar(words, topn = n)[i][1]])
    print("\n", n, "most similar words to " , words, ": \n")

    print(tabulate(table, showindex="always", headers="firstrow",
                   floatfmt="." + str(PRECISION) + "f", tablefmt="fancy_grid"))
    #print(tabulate(skipgram.wv.most_similar(words, topn = n), showindex="always", floatfmt="." + str(PRECISION) + "f", tablefmt="fancy_grid"))
#   --------------------------------------------------------------
#   Initialize info
print("Word2Vec - CBOW & Skipgram Comparative Tool\n")

print("Loading CBOW trained model\n")
cbow = Word2Vec.load(CBOW_MODEL)
print(" CBOW trained model loaded\n")

print(" Loading Skipgram trained model\n")
skipgram = Word2Vec.load(SKIPGRAM_MODEL)
print(" Skipgram trained model loaded\n")
#   --------------------------------------------------------------
#   Tool menu

on = True
while on:
    print(""" -------------------------------------
    1.  Similarity between 2 words
    2.  The most similar word
    3.  Does not match group
    4.  n most similar words
    5.  Exit""")
    print(" -------------------------------------")
    option = input("Enter option : ")
    if option == "1":
        print("\n Similarity between 2 words")
        print("-------------------------------------")
        find_similarity()
    elif option == "2":
        print("\n The most similar word to a word")
        print("-------------------------------------")
        words_input = input("Enter a word or words separated with spaces : ")
        words = words_input.lower().split()
        while len(words_input) == 0:
            print("\n You must enter a word!\n")
            words_input = input("Enter a word or words separated with spaces : ")
            words = words_input.lower().split()
        for i in range(0, len(words)):
            while (words[i] not in cbow.wv or words[i] not in skipgram.wv):
                print("\n The word " + words[i] + " does not exist in vocabulary!\n")
                words[i] = input("Enter a word instead which is included in vocabulary : ")
        # Multiple input supported | word1 word2 ..
        the_most_similar(words)
    elif option == "3":
        print("\n Word that does not match others")
        print("-------------------------------------")
        does_not_match()
    elif option == "4":
        print("\n n Most similar words")
        print("-------------------------------------")
        n_most_similar ()
    elif option == "5":
      print("\nExited successfully\n")
      on = None
    else:
       print("\n The option you entered is not valid!")
