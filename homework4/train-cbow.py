# imports needed and set up logging
import gensim
import logging
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#input_file="../../dataset/dysautonomia_10000_sentence.txt"
input_file="./sentences_data/sentence.txt"

with open (input_file, 'rb') as f:
    for i,line in enumerate (f):
        #print(line)
        break

def read_input(input_file):

    logging.info("reading file {0}...this may take a while".format(input_file))


                
    #ps = PorterStemmer()

    with open (input_file, 'rb') as f:
        for i, line in enumerate (f):
           
            #全部轉成小寫
            line = line.lower()
        
            '''
            #去除特殊符號  b' 
            line = str(line).replace("b'",' ')
            line = str(line).replace("\r'",' ')
            line = str(line).replace("\n",' ')
            line = str(line).replace('/',' ')
            line = str(line).replace('.',' ')
            line = str(line).replace('\n','') 
            line = str(line).replace('/e/',' ')
            line = str(line).replace('(d)',' ')
            line = str(line).replace('s)',' ')
            line = str(line).replace('?]',' ')
            line = str(line).replace('?]',' ')
            line = str(line).replace('=-B',' ')
            line = str(line).replace('-C',' ')
            '''
            read_words1= re.sub(r'[^\w\s]','',str(line).replace('/', ' '))
            
            #print(i)
            #print(line)
            
            result = word_tokenize(read_words1)
            
            words = 0
            
            '''
            for i in range(len(result)):            
                if len(result[i]) > 0 and result[i] != '-' and result[i] != '–' and result[i] != ',':
                    words += 1
                    
                    #確認是否為數字千分號
                    pos=result[i][:-1].find(',')
                    #print(pos)            
                    if int(pos) > 0 and result[i][pos-1:pos].isdigit() != True :
                        words += 1
                    #print(res[i])
                
                #去除特殊符號字元單一數字
                if result[i] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                    result[i] = ''
                #去除特殊符號字元
                result[i] = result[i].replace('~','')
                result[i] = result[i].replace(',','')
                result[i] = result[i].replace('!','')
                result[i] = result[i].replace('@','')
                result[i] = result[i].replace('#','')
                result[i] = result[i].replace('$','')
                result[i] = result[i].replace('%','')
                result[i] = result[i].replace('^','')
                result[i] = result[i].replace('&','')
                result[i] = result[i].replace('*','')
                result[i] = result[i].replace('(','')
                result[i] = result[i].replace(')','')
                result[i] = result[i].replace('!','')
                result[i] = result[i].replace(':','')
                result[i] = result[i].replace('+','')
                result[i] = result[i].replace('=','')
                result[i] = result[i].replace('=-','')
                result[i] = result[i].replace(',','')
                result[i] = result[i].replace("'",'')
                result[i] = result[i].replace("'s",'')
                result[i] = result[i].replace('\n','')
                result[i] = result[i].replace(' ','')
                
                if len(result[i]) > 50:
                    result[i] = ''
                    
                if len(result[i]) < 2:
                    #print(result[i])
                    result[i] = ''    
                
                #加入Porter's algorithm
                #result[i] = ps.stem(result[i])
                #print(result[i])
                
                #去除Stopwords
                stop_words = set(stopwords.words('english'))
                if result[i] in stop_words:
                    #print(result[i])
                    result[i] = ''
            '''
            line = ''
            for k in range(len(result)):
                line = line +' '+result[k]

            if (i % 10000 == 0):
                logging.info ("Read {0} articles".format (i))
            # do some pre-processing and return a list of words for each review text
            #yield gensim.utils.simple_preprocess(line,deacc=True)
            yield word_tokenize(line)

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (input_file))
print(documents)

logging.info ("Done reading input file")

model = gensim.models.Word2Vec (documents, window=5, max_vocab_size=5000, min_count=2, workers=10)

model.train(documents,total_examples=len(documents),epochs=1200)

model.save("dysautonomia_word2vec-cbow-trained.model")
#model.save("dailymail_word2vec-cbow-trained.model")
