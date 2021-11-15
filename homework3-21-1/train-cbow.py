# imports needed and set up logging
import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

input_file="../../dataset/dysautonomia_10000_sentence.txt"

with open (input_file, 'rb') as f:
    for i,line in enumerate (f):
        print(line)
        break

def read_input(input_file):

    logging.info("reading file {0}...this may take a while".format(input_file))

    with open (input_file, 'rb') as f:
        for i, line in enumerate (f):
            #print(i)
            #print(line)
            

            if (i % 10000 == 0):
                logging.info ("Read {0} articles".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (input_file))
logging.info ("Done reading input file")

model = gensim.models.Word2Vec (documents, window=10, min_count=2, negative=5, workers=10)

model.train(documents,total_examples=len(documents),epochs=20)
model.save("dysautonomia_word2vec-cbow-trained.model")
